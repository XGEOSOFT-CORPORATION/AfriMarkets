#!/usr/bin/env python3
"""
Script pour générer un guide PDF complet sur:
- Comment configurer un nouveau marché
- Comment ajouter des fonctions (get_tickers, get_data)
- Étapes pratiques avec exemples
"""

from fpdf import FPDF
from datetime import datetime

# Créer PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Utiliser les polices par défaut de FPDF

# Titre principal
pdf.set_font("DejaVu-Bold", "B", 24)
pdf.cell(0, 15, "AfriMarkets - Guide d'Extension", ln=True, align="C")
pdf.set_font("DejaVu", "", 11)
pdf.cell(0, 8, f"Comment ajouter un nouveau marché et configurer les fonctions", ln=True, align="C")
pdf.cell(0, 8, f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", ln=True, align="C")

pdf.ln(10)

# Section 1: Vue d'ensemble
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "1. Vue d'ensemble de l'architecture", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """L'architecture d'AfriMarkets utilise plusieurs patterns de conception:

• Registry Pattern: Enregistrement centralisé des marchés
• Factory Pattern: Création dynamique des adaptateurs
• Strategy Pattern: Implémentations spécifiques par marché
• Template Method: Interface commune via MarketAdapter

Tous les marchés héritent de la classe abstraite MarketAdapter et implémentent deux méthodes principales:
  - get_tickers(): Retourne les listes de tickers
  - get_data(): Retourne les données OHLCV
"""

pdf.multi_cell(0, 4, text)
pdf.ln(5)

# Section 2: Structure d'un marché
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "2. Structure d'un marché", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Chaque marché a une structure de répertoires:

afrimarkets/markets/CODE/
├── __init__.py              # Imports et exports
├── adapter.py               # Classe CODEAdapter
└── legacy/
    ├── __init__.py
    ├── scraper.py           # Web scraper custom
    ├── api_client.py        # Client API
    └── helpers.py           # Fonctions utilitaires

Exemple pour BRVM:
afrimarkets/markets/brvm/
├── __init__.py
├── adapter.py               # BRVMAdapter
└── legacy/
    ├── scraper.py
    └── helpers.py
"""

pdf.multi_cell(0, 4, text)
pdf.ln(5)

# Section 3: Étape 1 - Créer l'adaptateur
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "3. ÉTAPE 1 - Créer la classe adaptateur", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Exemple: Créer un adaptateur pour un marché fictif "XYZ"

1. Créer les fichiers:
   afrimarkets/markets/xyz/adapter.py

2. Implémenter la classe XYZAdapter:
"""

pdf.multi_cell(0, 4, text)

# Code snippet
pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """from afrimarkets.markets.base import MarketAdapter
from afrimarkets.core.market import Market
import pandas as pd
from datetime import datetime

class XYZAdapter(MarketAdapter):
    \"\"\"Adaptateur pour le marché XYZ\"\"\"
    
    def get_tickers(self) -> Market:
        \"\"\"Récupère les tickers du marché XYZ\"\"\"
        market = self._create_market()
        
        # Récupérer depuis scraper ou API
        market.list_shares = ["TICK1", "TICK2", "TICK3"]
        market.list_indexes = ["XYZ Index", "XYZ 10"]
        
        # Créer DataFrames pour les partages
        market.shares = pd.DataFrame({
            "Ticker": market.list_shares,
            "Name": ["Company 1", "Company 2", "Company 3"]
        })
        
        return market
    
    def get_data(self, ticker, from_date, to_date, period):
        \"\"\"Récupère données OHLCV pour un ticker\"\"\"
        from_date, to_date = self.normalize_dates(from_date, to_date)
        
        # Générer données ou récupérer via scraper
        dates = pd.date_range(from_date, to_date, freq='D')
        
        data = pd.DataFrame({
            'Date': dates,
            'Ticker': ticker,
            'Open': 100.0,
            'High': 105.0,
            'Low': 95.0,
            'Close': 102.0,
            'Volume': 1000000
        })
        
        return data
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

pdf.ln(5)

# Section 4: Étape 2 - Configurer la registry
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "4. ÉTAPE 2 - Configurer dans la Registry", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """1. Ouvrir: afrimarkets/core/registry.py

2. Ajouter configuration dans MARKET_CONFIGS:
"""

pdf.multi_cell(0, 4, text)

pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """MARKET_CONFIGS = {
    ...
    "XYZ": {
        "market_short_name": "XYZ",
        "market_full_name": "XYZ Stock Exchange",
        "official_url": "https://xyz.example.com",
        "market_url": "https://xyz.example.com/markets",
        "market_data_url": "https://api.xyz.example.com",
        "country": "Country XYZ",
        "currency": "XYZ",
    }
}
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

pdf.ln(5)

# Section 5: Étape 3 - Enregistrer
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "5. ÉTAPE 3 - Enregistrer le marché", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """1. Ouvrir: afrimarkets/markets/__init__.py

2. Importer et enregistrer:
"""

pdf.multi_cell(0, 4, text)

pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """from afrimarkets.markets.xyz.adapter import XYZAdapter
from afrimarkets.core.registry import MarketRegistry, MARKET_CONFIGS

def register_all_markets():
    \"\"\"Enregistrer tous les marchés\"\"\"
    
    MarketRegistry.register("BRVM", BRVMAdapter, MARKET_CONFIGS["BRVM"])
    # ... autres marchés ...
    MarketRegistry.register("XYZ", XYZAdapter, MARKET_CONFIGS["XYZ"])

# Auto-registration on import
register_all_markets()
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

pdf.ln(5)

# Section 6: Étape 4 - Implémenter le scraper
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "6. ÉTAPE 4 - Implémenter le scraper (Optionnel)", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Créer: afrimarkets/markets/xyz/legacy/scraper.py

Ce fichier contient la logique métier pour récupérer les données:
  • Web scraping (BeautifulSoup, Selenium)
  • API calls (requests, httpx)
  • Parse de données
  • Nettoyage et normalisation

Exemple simple:
"""

pdf.multi_cell(0, 4, text)

pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """import requests
import pandas as pd
from datetime import datetime

def fetch_tickers():
    \"\"\"Récupère tickers depuis API\"\"\"
    response = requests.get(
        "https://api.xyz.example.com/tickers"
    )
    return response.json()

def fetch_ohlcv(ticker, from_date, to_date):
    \"\"\"Récupère données OHLCV\"\"\"
    params = {
        'ticker': ticker,
        'from': from_date,
        'to': to_date
    }
    response = requests.get(
        "https://api.xyz.example.com/data",
        params=params
    )
    
    data = response.json()
    df = pd.DataFrame(data)
    
    # Normaliser colonnes
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    
    return df
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

pdf.ln(5)

# Section 7: Étape 5 - Utiliser le scraper dans l'adaptateur
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "7. ÉTAPE 5 - Intégrer le scraper", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Modifier: afrimarkets/markets/xyz/adapter.py

Importer et utiliser le scraper:
"""

pdf.multi_cell(0, 4, text)

pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """from afrimarkets.markets.base import MarketAdapter
from afrimarkets.markets.xyz.legacy.scraper import (
    fetch_tickers, fetch_ohlcv
)

class XYZAdapter(MarketAdapter):
    
    def get_tickers(self) -> Market:
        market = self._create_market()
        
        # Récupérer via scraper
        tickers_data = fetch_tickers()
        market.list_shares = tickers_data['shares']
        market.list_indexes = tickers_data['indexes']
        
        return market
    
    def get_data(self, ticker, from_date, to_date, period):
        from_date, to_date = self.normalize_dates(from_date, to_date)
        
        # Récupérer via scraper
        df = fetch_ohlcv(ticker, from_date, to_date)
        
        return df
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

# Page 2
pdf.add_page()

# Section 8: Tester
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "8. ÉTAPE 6 - Tester le nouveau marché", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Créer: tests/test_xyz.py

Tester que le marché fonctionne correctement:
"""

pdf.multi_cell(0, 4, text)

pdf.set_font("DejaVu-Mono", "", 9)
pdf.set_fill_color(240, 240, 240)

code = """import pytest
from afrimarkets import get_tickers, get_data
from afrimarkets.core.registry import MarketRegistry

class TestXYZMarket:
    
    def test_xyz_registered(self):
        \"\"\"Vérifier que XYZ est enregistré\"\"\"
        assert MarketRegistry.is_registered("XYZ")
    
    def test_get_xyz_tickers(self):
        \"\"\"Tester get_tickers pour XYZ\"\"\"
        market = get_tickers("XYZ")
        assert market is not None
        assert len(market.list_shares) > 0
        assert len(market.list_indexes) > 0
    
    def test_get_xyz_data(self):
        \"\"\"Tester get_data pour XYZ\"\"\"
        df = get_data("XYZ", ticker="TICK1")
        assert not df.empty
        assert "Date" in df.columns
        assert "Close" in df.columns
        assert "Volume" in df.columns

# Exécuter les tests
# pytest tests/test_xyz.py -v
"""

for line in code.split('\n'):
    if line.strip():
        pdf.cell(0, 3, line, ln=True, fill=True)

pdf.ln(5)

# Section 9: Checklist
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "9. Checklist d'implémentation", ln=True)
pdf.set_font("DejaVu", "", 10)

checklist = """☐ 1. Créer répertoire afrimarkets/markets/XYZ/
☐ 2. Créer adapter.py avec classe XYZAdapter
☐ 3. Implémenter get_tickers()
☐ 4. Implémenter get_data()
☐ 5. Créer répertoire legacy/
☐ 6. Créer scraper.py ou api_client.py
☐ 7. Ajouter configuration dans MARKET_CONFIGS
☐ 8. Enregistrer dans register_all_markets()
☐ 9. Créer tests/test_xyz.py
☐ 10. Tester: pytest tests/test_xyz.py
☐ 11. Tester l'intégration complète
☐ 12. Documenter les sources de données
"""

for line in checklist.split('\n'):
    if line.strip():
        pdf.cell(0, 4, line, ln=True)

pdf.ln(5)

# Section 10: Commandes utiles
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "10. Commandes utiles", ln=True)
pdf.set_font("DejaVu", "", 10)

commands = """# Vérifier que le marché est enregistré
python -c "from afrimarkets.core.registry import MarketRegistry; \\
           print(MarketRegistry.list_markets())"

# Tester rapidement
python -c "from afrimarkets import get_tickers; \\
           market = get_tickers('XYZ'); \\
           print(market.list_shares)"

# Exécuter tous les tests
pytest tests/ -v

# Exécuter les tests d'un marché spécifique
pytest tests/test_xyz.py -v

# Valider toute la configuration
python validate_config.py

# Voir les détails de configuration
python CONFIG_SUMMARY.py
"""

for line in commands.split('\n'):
    if line.strip():
        pdf.multi_cell(0, 3, line)

pdf.ln(5)

# Section 11: Ressources
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "11. Fichiers de référence", ln=True)
pdf.set_font("DejaVu", "", 10)

text = """Pour bien comprendre l'architecture, consultez:

1. afrimarkets/core/market.py
   → Définition de la classe Market

2. afrimarkets/markets/base.py
   → Classe abstraite MarketAdapter (interface)

3. afrimarkets/markets/brvm/adapter.py
   → Exemple d'implémentation réelle

4. afrimarkets/core/registry.py
   → Système de registry et configuration

5. afrimarkets/__init__.py
   → API publique (get_tickers, get_data)

6. CONTRIBUTING.md
   → Guide de contribution complet

7. DEVELOPMENT.md
   → Setup environnement de développement
"""

pdf.multi_cell(0, 4, text)

pdf.ln(5)

# Section 12: FAQ
pdf.set_font("DejaVu-Bold", "B", 14)
pdf.cell(0, 10, "12. Questions Fréquemment Posées", ln=True)
pdf.set_font("DejaVu", "", 10)

faq = """Q: Comment ajouter un nouveau marché sans scraper?
R: Utilisez des données fixes ou des fichiers CSV. L'API accepte
   une Market avec des DataFrames pré-remplis.

Q: Comment tester localement?
R: Utilisez pytest: pytest tests/test_xyz.py -v

Q: Où mettre mon code d'authentification API?
R: Dans afrimarkets/markets/xyz/legacy/config.py
   Utilisez des variables d'environnement pour secrets!

Q: Comment gérer les erreurs réseau?
R: Implémentez retry logic avec exponential backoff dans scraper.py
   Utilisez try/except pour les timeouts

Q: Comment ajouter d'autres endpoints?
R: Étendez MarketAdapter avec des méthodes supplémentaires
   Ex: get_live_quotes(), get_company_info()

Q: Comment faire du caching?
R: Utilisez functools.lru_cache() ou Redis
   Voir utils/cache.py pour exemple
"""

for line in faq.split('\n'):
    if line.strip():
        pdf.multi_cell(0, 3.5, line)

# Sauvegarder
output_path = "c:\\Users\\DELL\\Desktop\\GITHUB DEV\\AfriMarkets\\GUIDE_AJOUTER_MARCHE.pdf"
pdf.output(output_path)

print(f"✓ PDF généré avec succès: {output_path}")
print(f"✓ Nombre de pages: {pdf.page}")
print(f"✓ Taille: {pdf.len_page_width}x{pdf.len_page_height}")
