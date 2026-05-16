"""
Constants - Constantes globales pour AfriMarkets
"""

# Codes de marché supportés
SUPPORTED_MARKETS = ["BRVM", "NGX", "GSE", "JSE", "MSE", "EGX", "TSE"]

# Devises par marché
MARKET_CURRENCIES = {
    "BRVM": "XOF",  # Franc CFA
    "NGX": "NGN",   # Naira nigérian
    "GSE": "GHS",   # Cedi ghanéen
    "JSE": "ZAR",   # Rand sud-africain
    "MSE": "MAD",   # Dirham marocain
    "EGX": "EGP",   # Livre égyptienne
    "TSE": "TND",   # Dinar tunisien
}

# Pays par marché
MARKET_COUNTRIES = {
    "BRVM": "Côte d'Ivoire",
    "NGX": "Nigeria",
    "GSE": "Ghana",
    "JSE": "South Africa",
    "MSE": "Morocco",
    "EGX": "Egypt",
    "TSE": "Tunisia",
}

# Périodes supportées
SUPPORTED_PERIODS = ["daily", "weekly", "monthly"]

# Types de titres
TICKER_TYPES = {
    "SHARE": "Action",
    "INDEX": "Indice",
    "BOND": "Obligation",
    "ETF": "Fonds indiciels",
}

# Colonnes OHLCV standard
OHLCV_COLUMNS = ["Date", "Ticker", "Open", "High", "Low", "Close", "Volume"]

# Délai par défaut pour les données (en jours)
DEFAULT_LOOKBACK_DAYS = 89

# Nombre maximum de requêtes simultanées
MAX_CONCURRENT_REQUESTS = 5

# Timeouts (en secondes)
REQUEST_TIMEOUT = 30
SCRAPER_TIMEOUT = 60

# Format de date standard
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
