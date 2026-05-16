"""
AfriMarkets — Unified access to African stock market data

A comprehensive Python package for accessing, analyzing, and visualizing
financial data from African stock exchanges.

Main API:
    get_tickers(market_code): Fetch tickers for a market
    get_data(market_code, ticker, ...): Fetch OHLCV data

Supported Markets:
    - BRVM (Côte d'Ivoire)
    - NGX (Nigeria)
    - GSE (Ghana)
    - JSE (South Africa)
    - MSE (Morocco)
    - EGX (Egypt)
    - TSE (Tunisia)

Examples:
    >>> from afrimarkets import get_tickers, get_data
    >>> 
    >>> # Get market tickers
    >>> brvm = get_tickers("BRVM")
    >>> print(brvm.list_shares)
    >>> 
    >>> # Get OHLCV data
    >>> df = get_data("BRVM", ticker="SNTS", from_date="2023-01-01")
    >>> 
    >>> # All markets
    >>> all_markets = get_tickers("ALL")
"""

__version__ = "0.1.0"
__author__ = (
    "Olabiyi Aurel Géoffroy Odjo, "
    "Koffi Frederic Sessie, "
    "Abdoul Oudouss Diakité, "
    "Steven P. Sanderson II"
)
__license__ = "MIT"

# Import core components
from afrimarkets.core.market import Market
from afrimarkets.core.registry import MarketRegistry, MARKET_CONFIGS
from afrimarkets.core.dispatcher import MarketDispatcher

# Import all market adapters (auto-registers them)
import afrimarkets.markets

# Main public API
def get_tickers(market_code: str = "ALL"):
    """
    Récupère les tickers d'un marché ou de tous les marchés.
    
    Args:
        market_code: Code du marché ("BRVM", "NGX", etc.) ou "ALL"
    
    Returns:
        Market object ou dict de Market objects si market_code="ALL"
    
    Raises:
        ValueError: Si le marché n'existe pas
    
    Examples:
        >>> # Un marché
        >>> brvm = get_tickers("BRVM")
        >>> print(brvm.list_shares)
        
        >>> # Tous les marchés
        >>> all_markets = get_tickers("ALL")
        >>> for code, market in all_markets.items():
        ...     print(f"{code}: {len(market.list_shares)} shares")
    """
    return MarketDispatcher.get_tickers(market_code)


def get_data(
    market_code: str,
    ticker: str = "ALL",
    period: str = "daily",
    from_date=None,
    to_date=None,
    output_format: str = "by_col"
):
    """
    Récupère les données OHLCV d'un marché.
    
    Args:
        market_code: Code du marché ("BRVM", "NGX", etc.)
        ticker: Ticker ou "ALL", "ALL SHARES", "ALL INDEXES"
        period: Fréquence ("daily", "weekly", "monthly")
        from_date: Date de début (default: 89 jours avant aujourd'hui)
        to_date: Date de fin (default: aujourd'hui)
        output_format: "by_col" (long), "by_row" (wide), "all" (both)
    
    Returns:
        DataFrame ou dict de DataFrames selon output_format
    
    Raises:
        ValueError: Si le marché n'existe pas ou aucune données
    
    Examples:
        >>> # Un ticker
        >>> df = get_data("BRVM", ticker="SNTS")
        >>> 
        >>> # Plusieurs tickers
        >>> df = get_data("NGX", ticker=["ZENITHBANK", "GTCO"])
        >>> 
        >>> # Format large
        >>> df = get_data("BRVM", output_format="by_row")
        >>> 
        >>> # Format long avec dates
        >>> df = get_data(
        ...     "BRVM",
        ...     ticker="ALL SHARES",
        ...     from_date="2023-01-01",
        ...     to_date="2023-12-31"
        ... )
    """
    return MarketDispatcher.get_data(
        market_code,
        ticker=ticker,
        period=period,
        from_date=from_date,
        to_date=to_date,
        output_format=output_format
    )


# Public exports
__all__ = [
    # Main API
    "get_tickers",
    "get_data",
    # Core classes
    "Market",
    "MarketRegistry",
    "MARKET_CONFIGS",
    "MarketDispatcher",
]
