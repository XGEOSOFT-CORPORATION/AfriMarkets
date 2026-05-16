"""
Quick Start - Démarrer rapidement avec AfriMarkets

Ce script montre les utilisations les plus courantes du package.
"""

# ============================================================================
# 1. IMPORTS
# ============================================================================

from afrimarkets import get_tickers, get_data
import pandas as pd


# ============================================================================
# 2. RÉCUPÉRER LES TICKERS
# ============================================================================

# Un seul marché
print("\n=== BRVM Market Info ===")
brvm = get_tickers("BRVM")
print(brvm)
print(f"Shares: {brvm.list_shares}")
print(f"Indexes: {brvm.list_indexes}")

# Tous les marchés
print("\n=== All Available Markets ===")
all_markets = get_tickers("ALL")
for code, market in all_markets.items():
    print(f"  {code}: {market.market_full_name} ({len(market.list_shares)} shares)")


# ============================================================================
# 3. RÉCUPÉRER LES DONNÉES OHLCV
# ============================================================================

# Un ticker
print("\n=== Get Data for SNTS (BRVM) ===")
df = get_data("BRVM", ticker="SNTS", from_date="2023-01-01", to_date="2023-12-31")
print(df.head())

# Plusieurs tickers
print("\n=== Multiple Tickers (NGX) ===")
df = get_data("NGX", ticker=["ZENITHBANK", "GTCO"], from_date="2023-06-01")
print(df.head())

# Tous les tickers d'une catégorie
print("\n=== All Shares (BRVM) ===")
df = get_data("BRVM", ticker="ALL SHARES")
print(df.head())

# Format large (wide format)
print("\n=== Wide Format (by_row) ===")
df = get_data("BRVM", ticker="ALL SHARES", output_format="by_row")
print(df.head())


# ============================================================================
# 4. UTILISATION DES ADAPTATEURS DIRECTEMENT
# ============================================================================

from afrimarkets.core.registry import MarketRegistry

print("\n=== Direct Adapter Usage ===")
adapter = MarketRegistry.get_adapter("BRVM")
print(f"Adapter: {adapter}")
market = adapter.get_tickers()
print(f"Market: {market}")


# ============================================================================
# 5. UTILISER LES UTILITAIRES
# ============================================================================

from afrimarkets.utils import (
    validate_ticker_format,
    validate_market_code,
    format_currency,
    format_ohlcv_dataframe,
)

print("\n=== Utilities ===")
print(f"Is 'SNTS' a valid ticker? {validate_ticker_format('SNTS')}")
print(f"Is 'BRVM' a valid market? {validate_market_code('BRVM')}")
print(f"Format 100 USD: {format_currency(100, 'USD')}")
print(f"Format 50000 XOF: {format_currency(50000, 'XOF')}")


# ============================================================================
# 6. DONNÉES FORMATÉES
# ============================================================================

from afrimarkets.utils import format_ohlcv_dataframe, add_calculated_columns

df = get_data("BRVM", ticker="SNTS", from_date="2023-01-01", to_date="2023-01-31")
df = format_ohlcv_dataframe(df)
df = add_calculated_columns(df)
print("\n=== Formatted Data with Calculated Columns ===")
print(df[["Date", "Ticker", "Close", "Daily_Return", "High_Low_Range"]].head())


print("\n✓ All examples completed successfully!")
