"""
README - Guide pour ajouter un nouveau marché

## Étapes rapides

1. **Créer la structure du dossier**
   ```bash
   mkdir -p afrimarkets/markets/NEW_MARKET/legacy
   ```

2. **Copier l'adaptateur template**
   ```bash
   cp afrimarkets/markets/templates/adapter.py afrimarkets/markets/NEW_MARKET/adapter.py
   ```

3. **Renommer la classe**
   - Remplacer `NewMarketAdapter` par `NEWMARKETAdapter`
   - Remplacer les références à `new_market` par votre marché

4. **Implémenter les méthodes abstraites**
   - `get_tickers()`: Récupérer les listes d'indices, actions, obligations
   - `get_data()`: Récupérer les données OHLCV

5. **Créer les fichiers legacy/**
   - `legacy/scraper.py`: Code de scraping spécifique au marché
   - `legacy/parser.py`: Parseurs de données
   - `legacy/__init__.py`: Exports

6. **Enregistrer le marché**
   ```python
   # Dans afrimarkets/markets/__init__.py
   from afrimarkets.markets.new_market.adapter import NEWMARKETAdapter
   MarketRegistry.register("NEWMARKET", NEWMARKETAdapter, MARKET_CONFIGS["NEWMARKET"])
   ```

7. **Ajouter la configuration**
   ```python
   # Dans afrimarkets/core/registry.py (MARKET_CONFIGS)
   "NEWMARKET": {
       "market_short_name": "NEWMARKET",
       "market_full_name": "New Market Name",
       "country": "Country",
       "currency": "CUR",
       "official_url": "https://...",
       "market_url": "https://...",
       "market_data_url": "https://...",
   }
   ```

8. **Créer les tests**
   ```bash
   touch tests/markets/test_newmarket.py
   ```
   ```python
   from afrimarkets import get_tickers, get_data
   
   def test_get_tickers_newmarket():
       market = get_tickers("NEWMARKET")
       assert market is not None
       assert len(market.list_shares) > 0
   
   def test_get_data_newmarket():
       df = get_data("NEWMARKET", ticker="TICKER")
       assert not df.empty
       assert "Date" in df.columns
   ```

9. **Tester localement**
   ```bash
   pytest tests/markets/test_newmarket.py -v
   ```

## Structure recommended pour le dossier legacy/

```
legacy/
├── __init__.py
├── scraper.py          # Web scraper ou API client
├── parser.py           # Parseur de données
├── constants.py        # Constantes spécifiques au marché
└── utils.py            # Utilitaires
```

## Exemple d'implémentation

```python
# afrimarkets/markets/brvm/adapter.py
from datetime import datetime
import pandas as pd
from afrimarkets.markets.base import MarketAdapter
from .legacy import BRVMScraper

class BRVMAdapter(MarketAdapter):
    def __init__(self, config: dict):
        super().__init__(config)
        self.scraper = BRVMScraper()
    
    def get_tickers(self) -> object:
        indexes = self.scraper.fetch_indexes()
        shares = self.scraper.fetch_shares()
        
        self.market.indexes = indexes
        self.market.shares = shares
        self.market.list_indexes = indexes["Ticker"].tolist()
        self.market.list_shares = shares["Ticker"].tolist()
        
        return self.market
    
    def get_data(self, ticker: str, **kwargs) -> pd.DataFrame:
        from_date, to_date = self.normalize_dates(kwargs.get("from_date"), kwargs.get("to_date"))
        return self.scraper.fetch_data(ticker, from_date, to_date)
```

## Ressources

- [Template d'adaptateur](./adapter.py)
- [Base class MarketAdapter](../base.py)
- [Classe Market](../../core/market.py)
- [Registry et Dispatcher](../../core/)

## Support

Pour des questions ou des problèmes:
1. Consultez les exemples d'adaptateurs existants (BRVM, NGX, etc.)
2. Ouvrez une issue sur GitHub
3. Consultez la documentation complète
"""
