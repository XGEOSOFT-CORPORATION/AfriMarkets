"""
Data models for AfriMarkets
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class OHLCVData:
    """
    Représente une barre OHLCV (Open, High, Low, Close, Volume)
    """
    date: datetime
    ticker: str
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: Optional[int] = None
    
    @property
    def daily_return(self) -> float:
        """Calcule le rendement du jour en pourcentage"""
        if self.open_price == 0:
            return 0.0
        return ((self.close_price - self.open_price) / self.open_price) * 100
    
    @property
    def high_low_diff(self) -> float:
        """Calcule la différence entre le high et le low"""
        return self.high_price - self.low_price
    
    @property
    def high_low_pct(self) -> float:
        """Calcule la volatilité intra-jour en pourcentage"""
        if self.low_price == 0:
            return 0.0
        return (self.high_low_diff / self.low_price) * 100


@dataclass
class Ticker:
    """Représente un ticker (action, indice, obligation)"""
    symbol: str
    name: str
    market_code: str
    ticker_type: str  # "SHARE", "INDEX", "BOND"
    isin: Optional[str] = None
    sector: Optional[str] = None
    description: Optional[str] = None
