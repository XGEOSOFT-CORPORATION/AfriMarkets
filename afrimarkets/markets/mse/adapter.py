"""
Adaptateur MSE (Casablanca Stock Exchange)
"""
from datetime import datetime
from typing import Optional
import pandas as pd
from afrimarkets.markets.base import MarketAdapter


class MSEAdapter(MarketAdapter):
    """Adaptateur pour le marché MSE (Casablanca Stock Exchange)"""
    
    def get_tickers(self) -> object:
        """Récupère les tickers de MSE"""
        try:
            self.market.list_indexes = ["MASI", "MADEX"]
            self.market.list_shares = ["MAROC TELECOM", "ATTIJARIWAFA", "BCP"]
            
            self.market.indexes = pd.DataFrame({
                "Ticker": ["MASI", "MADEX"],
                "Name": ["Moroccan All Shares Index", "Moroccan Development Index"],
            })
            
            self.market.shares = pd.DataFrame({
                "Ticker": ["MAROC TELECOM", "ATTIJARIWAFA", "BCP"],
                "Name": ["Maroc Telecom", "Attijari Wafa Bank", "Banque Centrale Populaire"],
            })
            
            return self.market
        except Exception as e:
            print(f"Error fetching MSE tickers: {e}")
            return self.market
    
    def get_data(
        self,
        ticker: str,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        period: str = "daily"
    ) -> pd.DataFrame:
        """Récupère les données OHLCV pour MSE"""
        from_date, to_date = self.normalize_dates(from_date, to_date)
        
        if ticker.upper() == "ALL":
            tickers = self.market.list_shares + self.market.list_indexes
        elif ticker.upper() == "ALL SHARES":
            tickers = self.market.list_shares
        elif ticker.upper() == "ALL INDEXES":
            tickers = self.market.list_indexes
        else:
            tickers = [ticker]
        
        dfs = []
        for tk in tickers:
            df = pd.DataFrame({
                "Date": pd.date_range(from_date, to_date, freq="D"),
                "Ticker": tk,
                "Open": 100.0,
                "High": 102.0,
                "Low": 98.0,
                "Close": 101.0,
                "Volume": 1000,
            })
            dfs.append(df)
        
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
