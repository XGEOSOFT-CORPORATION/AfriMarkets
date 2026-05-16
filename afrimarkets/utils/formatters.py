"""
Formatters - Utility functions for formatting data
"""
import pandas as pd
from datetime import datetime


def format_ohlcv_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formate un DataFrame OHLCV.
    
    - Convertit les colonnes de prix en float
    - Convertit la colonne Date en datetime
    - Trie par Date et Ticker
    
    Args:
        df: DataFrame à formater
    
    Returns:
        DataFrame formaté
    """
    df = df.copy()
    
    # Colonnes à convertir en float
    price_cols = ["Open", "High", "Low", "Close"]
    for col in price_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Convertir Volume en entier
    if "Volume" in df.columns:
        df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce").astype("Int64")
    
    # Convertir Date en datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    
    # Trier
    if "Date" in df.columns and "Ticker" in df.columns:
        df = df.sort_values(["Date", "Ticker"]).reset_index(drop=True)
    
    return df


def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute des colonnes calculées au DataFrame OHLCV.
    
    Ajoute:
    - Daily_Return: Rendement du jour (%)
    - High_Low_Range: Différence entre High et Low
    - Price_Change: Variation Close vs Open
    
    Args:
        df: DataFrame OHLCV
    
    Returns:
        DataFrame avec colonnes calculées
    """
    df = df.copy()
    
    if all(col in df.columns for col in ["Open", "High", "Low", "Close"]):
        # Rendement du jour
        df["Daily_Return"] = ((df["Close"] - df["Open"]) / df["Open"] * 100).round(4)
        
        # Étendue High-Low
        df["High_Low_Range"] = (df["High"] - df["Low"]).round(4)
        
        # Variation Close vs Open
        df["Price_Change"] = (df["Close"] - df["Open"]).round(4)
    
    return df


def pivot_to_wide_format(df: pd.DataFrame, value_col: str = "Close") -> pd.DataFrame:
    """
    Convertit un DataFrame long en format large (wide).
    
    Args:
        df: DataFrame en format long
        value_col: Colonne à pivoter ("Close", "Volume", etc.)
    
    Returns:
        DataFrame en format large avec Date en index et Tickers en colonnes
    """
    if "Date" not in df.columns or "Ticker" not in df.columns:
        raise ValueError("DataFrame must have 'Date' and 'Ticker' columns")
    
    if value_col not in df.columns:
        raise ValueError(f"Column '{value_col}' not found in DataFrame")
    
    return df.pivot_table(
        index="Date",
        columns="Ticker",
        values=value_col,
        aggfunc="first"
    )


def format_ticker_display(ticker: str, market_code: str = "") -> str:
    """
    Formate un ticker pour l'affichage.
    
    Args:
        ticker: Symbole du ticker
        market_code: Code du marché (optionnel)
    
    Returns:
        Ticker formaté pour l'affichage
    """
    formatted = ticker.upper().strip()
    if market_code:
        formatted = f"{market_code}:{formatted}"
    return formatted
