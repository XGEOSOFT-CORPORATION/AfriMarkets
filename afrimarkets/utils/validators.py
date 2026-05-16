"""
Utility functions and helpers for AfriMarkets
"""
import re
from datetime import datetime


def validate_ticker_format(ticker: str) -> bool:
    """
    Valide le format d'un ticker.
    
    Args:
        ticker: Symbole du ticker
    
    Returns:
        True si le format est valide
    """
    # Les tickers sont généralement des chaînes alphanumériques (1-10 caractères)
    pattern = r'^[A-Z0-9]{1,10}$'
    return bool(re.match(pattern, ticker.upper()))


def validate_market_code(market_code: str) -> bool:
    """
    Valide le format d'un code de marché.
    
    Args:
        market_code: Code du marché
    
    Returns:
        True si le format est valide
    """
    valid_codes = ["BRVM", "NGX", "GSE", "JSE", "MSE", "EGX", "TSE", "ALL"]
    return market_code.upper() in valid_codes


def normalize_ticker(ticker: str) -> str:
    """Normalise un ticker en majuscules"""
    return ticker.upper().strip()


def normalize_date(date_input) -> datetime.date:
    """
    Normalise une date (string, datetime ou date).
    
    Args:
        date_input: Date à normaliser
    
    Returns:
        datetime.date object
    """
    if isinstance(date_input, str):
        return datetime.strptime(date_input, "%Y-%m-%d").date()
    elif isinstance(date_input, datetime):
        return date_input.date()
    return date_input


def format_currency(value: float, currency: str = "USD", decimals: int = 2) -> str:
    """
    Formate une valeur en devise.
    
    Args:
        value: Valeur à formater
        currency: Code de devise (USD, EUR, XOF, NGN, etc.)
        decimals: Nombre de décimales
    
    Returns:
        Chaîne formatée avec symbole de devise
    """
    symbols = {
        "USD": "$",
        "EUR": "€",
        "XOF": "CFA",
        "NGN": "₦",
        "ZAR": "R",
        "MAD": "DH",
        "EGP": "£",
        "TND": "د.ت",
    }
    symbol = symbols.get(currency, currency)
    return f"{symbol} {value:,.{decimals}f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Formate une valeur en pourcentage"""
    return f"{value:.{decimals}f}%"
