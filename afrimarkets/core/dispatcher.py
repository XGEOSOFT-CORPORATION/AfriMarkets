"""
Central dispatcher pour get_data() et get_tickers()
Routage automatique vers l'adaptateur approprié
"""
from typing import Union, List, Optional, Literal
from datetime import datetime, date
import pandas as pd
from .registry import MarketRegistry


class MarketDispatcher:
    """Dispatcher centralisé pour tous les appels API"""
    
    @staticmethod
    def get_tickers(market_code: str = "ALL") -> Union[dict, object]:
        """
        Dispatcher pour récupérer les tickers.
        
        Args:
            market_code: Code du marché ou "ALL" pour tous
        
        Returns:
            - Si market_code = "ALL": Dict de Market objects
            - Sinon: Single Market object
            
        Raises:
            ValueError: Si le marché n'existe pas
            
        Examples:
            >>> from afrimarkets.core.dispatcher import MarketDispatcher
            >>> 
            >>> # Un marché
            >>> brvm = MarketDispatcher.get_tickers("BRVM")
            >>> 
            >>> # Tous les marchés
            >>> all_markets = MarketDispatcher.get_tickers("ALL")
        """
        market_code = market_code.upper()
        
        if market_code == "ALL":
            # Retourne tous les marchés
            result = {}
            for code in MarketRegistry.list_markets():
                try:
                    adapter = MarketRegistry.get_adapter(code)
                    result[code] = adapter.get_tickers()
                except Exception as e:
                    print(f"⚠ Error fetching {code}: {e}")
            return result
        
        else:
            # Retourne un seul marché
            if not MarketRegistry.is_registered(market_code):
                raise ValueError(
                    f"Market '{market_code}' not available. "
                    f"Available: {', '.join(MarketRegistry.list_markets())}"
                )
            
            adapter = MarketRegistry.get_adapter(market_code)
            return adapter.get_tickers()
    
    @staticmethod
    def get_data(
        market_code: str,
        ticker: Union[str, List[str]] = "ALL",
        period: str = "daily",
        from_date: Union[datetime, date, str, None] = None,
        to_date: Union[datetime, date, str, None] = None,
        output_format: Literal["by_col", "by_row", "all"] = "by_col"
    ) -> Union[pd.DataFrame, dict]:
        """
        Dispatcher pour récupérer les données OHLCV.
        
        Args:
            market_code: Code du marché ("BRVM", "NGX", etc.)
            ticker: "ALL", "ALL SHARES", "ALL INDEXES", ou liste de tickers
            period: "daily", "weekly", "monthly"
            from_date: Date de début (default: 89 jours avant aujourd'hui)
            to_date: Date de fin (default: aujourd'hui)
            output_format: "by_col" (long), "by_row" (wide), ou "all" (both)
        
        Returns:
            DataFrame ou dict de DataFrames selon output_format
            
        Raises:
            ValueError: Si le marché n'existe pas
            
        Examples:
            >>> from afrimarkets.core.dispatcher import MarketDispatcher
            >>> 
            >>> # Un ticker
            >>> df = MarketDispatcher.get_data("BRVM", ticker="SNTS")
            >>> 
            >>> # Plusieurs tickers
            >>> df = MarketDispatcher.get_data("NGX", ticker=["ZENITHBANK", "GTCO"])
            >>> 
            >>> # Format large
            >>> df = MarketDispatcher.get_data("BRVM", output_format="by_row")
        """
        market_code = market_code.upper()
        
        if not MarketRegistry.is_registered(market_code):
            raise ValueError(
                f"Market '{market_code}' not available. "
                f"Available: {', '.join(MarketRegistry.list_markets())}"
            )
        
        adapter = MarketRegistry.get_adapter(market_code)
        
        # Convertir ticker en liste si nécessaire
        if isinstance(ticker, str):
            tickers = [ticker]
        else:
            tickers = ticker
        
        # Récupérer les données pour chaque ticker
        dfs = []
        for tk in tickers:
            try:
                df = adapter.get_data(
                    ticker=tk,
                    from_date=from_date,
                    to_date=to_date,
                    period=period
                )
                if df is not None and not df.empty:
                    dfs.append(df)
            except Exception as e:
                print(f"⚠ Error fetching {tk}: {e}")
        
        if not dfs:
            raise ValueError(f"No data retrieved for {market_code} ticker(s): {tickers}")
        
        result = pd.concat(dfs, ignore_index=True)
        
        # Formatage de sortie
        if output_format == "by_row":
            result = _convert_to_wide(result)
        elif output_format == "all":
            result = {
                "by_col": result,
                "by_row": _convert_to_wide(result)
            }
        
        return result


def _convert_to_wide(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convertit long format en wide format.
    
    Transforme:
    Date       | Ticker  | Open  | Close | ...
    2023-01-01 | SNTS    | 100   | 102   | ...
    2023-01-01 | SGBCI   | 200   | 205   | ...
    
    En:
    Date       | SNTS_Open | SNTS_Close | SGBCI_Open | SGBCI_Close | ...
    2023-01-01 | 100       | 102        | 200        | 205         | ...
    """
    if "Date" not in df.columns or "Ticker" not in df.columns:
        return df  # Retour le DataFrame tel quel si format invalide
    
    # Pivot sur Date et Ticker
    return df.pivot_table(
        index="Date",
        columns="Ticker",
        values=["Open", "High", "Low", "Close", "Volume"],
        aggfunc="first"
    )
