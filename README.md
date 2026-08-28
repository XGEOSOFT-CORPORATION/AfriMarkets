<div align="center">

# <img src="assets/logo.png" alt="AfriMarkets" width="120">

# AfriMarkets

### African Financial Markets Data for Python

[![Python](https://img.shields.io/badge/Python-%3E%3D3.12-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)]()
[![Market](https://img.shields.io/badge/Market-BRVM-0548A2.svg)]()

**Simple. Open source. Built for African financial markets.**

[Français](#français) · [English](#english) · [Yorùbá](#yorùbá)

</div>

---

## 🌍 About AfriMarkets

**AfriMarkets** is an open-source Python package designed to provide a simple and unified interface for accessing and working with African financial markets.

The project aims to make African financial-market data more accessible to:

* 👨‍💻 Developers
* 📊 Data scientists
* 🎓 Researchers
* 💼 Investors
* 🏦 Financial institutions
* 🚀 Fintechs

> **Current status:** Alpha — `v0.1.0`
> **Current market:** BRVM
> **Python:** `>=3.12`

The market registry and initial **BRVM** support are currently available.

Ticker and historical-price connectors are still under active development.

---

## 📈 Vision

AfriMarkets aims to become a unified Python ecosystem for African financial markets.

```text
                    AfriMarkets
                         │
        ┌────────────────┼────────────────┐
        │                │                │
      Markets          Assets           Data
        │                │                │
   ┌────┼────┐      ┌────┼────┐      ┌────┼────┐
   │    │    │      │    │    │      │    │    │
 BRVM  NSE  JSE   Share Bond Index  Prices Tickers ...
```

The long-term objective is to support multiple African markets through a common and consistent API.

---

# 🇫🇷 Français

## Installation

Python **3.12 ou une version plus récente** est nécessaire.

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git

cd AfriMarkets-python

python -m venv .venv

source .venv/bin/activate

# Windows :
# .venv\Scripts\activate

python -m pip install -e .
```

---

## 🚀 Utilisation

### Accéder à la BRVM

```python
from afrimarkets import BRVM

market = BRVM()

data = market.get_data(
    ["BOAB"],
    start="2020-01-01",
    end="2026-01-31",
    structure="column",
)

print(data)
```

---

## 🔎 Récupérer les tickers

Lorsque la connexion Internet est disponible, `BRVM()` récupère automatiquement les tickers du marché lors de son initialisation.

Pour récupérer ou actualiser les tickers :

```python
tickers = market.get_tickers()

print(tickers)
print(market.tickers)
```

Une connexion Internet stable est nécessaire pour récupérer les données en ligne.

---

## 🏦 Marchés disponibles

AfriMarkets possède une registry permettant de découvrir les marchés disponibles.

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())
# ['BRVM']

market = get_market("BRVM")

print(market.code)
# BRVM
```

Cette architecture permet d'ajouter progressivement de nouveaux marchés sans modifier l'interface utilisateur.

---

## 📊 Créer un actif

Un actif peut être créé directement :

```python
from afrimarkets.assets import Share

share = Share(
    symbol="BOAB",
    name="Entreprise exemple"
)

print(share.info())
```

---

## 🗺️ Marchés prévus

| Marché    | Pays / Région  | Statut     |
| --------- | -------------- | ---------- |
| 🇨🇮 BRVM | UEMOA          | 🟢 Initial |
| 🇳🇬 NGX  | Nigeria        | 🔵 Planned |
| 🇿🇦 JSE  | Afrique du Sud | 🔵 Planned |
| 🇰🇪 NSE  | Kenya          | 🔵 Planned |
| 🇪🇬 EGX  | Égypte         | 🔵 Planned |
| 🇲🇦 CSE  | Maroc          | 🔵 Planned |

> Cette liste représente la direction du projet et ne signifie pas que les connecteurs correspondants sont déjà disponibles.

---

## 🧱 Architecture

AfriMarkets est conçu autour de plusieurs composants :

```text
afrimarkets/
│
├── assets/
│   ├── share.py
│   ├── bond.py
│   └── index.py
│
├── markets/
│   ├── registry.py
│   ├── brvm.py
│   └── ...
│
├── connectors/
│   ├── tickers/
│   └── prices/
│
├── utils/
│
└── __init__.py
```

L'objectif est de séparer :

**Market → Asset → Connector → Data**

afin de faciliter l'extension du package.

---

## 🛣️ Roadmap

### `v0.1.x`

* [x] Market registry
* [x] BRVM initial support
* [x] Asset objects
* [x] Automatic ticker loading
* [x] Historical data interface
* [ ] More robust BRVM connector
* [ ] Extended tests

### `v0.2.x`

* [ ] Additional African markets
* [ ] Improved historical-price connectors
* [ ] Better error handling
* [ ] Data validation
* [ ] Caching
* [ ] Documentation website

### Future

* [ ] Fundamental financial data
* [ ] Market indices
* [ ] Bonds
* [ ] ETFs
* [ ] Portfolio analysis
* [ ] Financial indicators
* [ ] Quantitative research tools

---

## ⚠️ Disclaimer

AfriMarkets is a software and data-access project.

It **does not provide investment advice** and does not guarantee the accuracy, completeness or availability of market data.

Users are responsible for validating data before using it for financial, research or investment purposes.

---

## 🤝 Contributing

Contributions are welcome!

You can contribute by:

* adding a new African market;
* improving a connector;
* adding tests;
* improving documentation;
* reporting bugs;
* proposing new features;
* developing analysis tools.

Every contribution helps make African financial-market data more accessible.

---

# 🇬🇧 English

## Installation

Python **3.12 or later** is required.

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git

cd AfriMarkets-python

python -m venv .venv

source .venv/bin/activate

# Windows:
# .venv\Scripts\activate

python -m pip install -e .
```

---

## Usage

### Access BRVM

```python
from afrimarkets import BRVM

market = BRVM()

data = market.get_data(
    ["BOAB"],
    start="2020-01-01",
    end="2026-01-31",
    structure="column",
)

print(data)
```

### Retrieve tickers

```python
tickers = market.get_tickers()

print(tickers)
print(market.tickers)
```

### Available markets

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())
# ['BRVM']

market = get_market("BRVM")

print(market.code)
# BRVM
```

### Create an asset

```python
from afrimarkets.assets import Share

share = Share(
    symbol="BOAB",
    name="Example company"
)

print(share.info())
```

---

## Contributing

Contributions are welcome from developers, researchers, data scientists and financial professionals interested in African financial markets.

We welcome:

* new market implementations;
* data connectors;
* tests;
* documentation;
* analysis tools;
* bug fixes;
* new features.

---

# 🇳🇬 Yorùbá

## Nípa AfriMarkets

AfriMarkets jẹ́ package Python open source tí ó ń pèsè ọ̀nà rọrùn àti ìṣọ̀kan fún lílo data àwọn ọjà ìṣúná Áfíríkà.

Ó ń fẹ́ kí data ọjà ìṣúná Áfíríkà rọrùn fún:

* 👨‍💻 Developers
* 📊 Data scientists
* 🎓 Researchers
* 💼 Investors
* 🏦 Financial institutions
* 🚀 Fintechs

**Ipò iṣẹ́:** Alpha — `v0.1.0`

**Ọjà tó wà báyìí:** BRVM

**Python:** `>=3.12`

---

## Fifi sori ẹrọ

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git

cd AfriMarkets-python

python -m venv .venv

source .venv/bin/activate

python -m pip install -e .
```

---

## Lílò

```python
from afrimarkets import BRVM

market = BRVM()

data = market.get_data(
    ["BOAB"],
    start="2020-01-01",
    end="2026-01-31",
    structure="column",
)

print(data)
```

Láti gba àwọn ticker:

```python
tickers = market.get_tickers()

print(market.tickers)
```

Láti wo àwọn ọjà tó wà:

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())

market = get_market("BRVM")

print(market.code)
```

---

# 👥 Authors

| Name                            | Role                 | Contact                                                                 |
| ------------------------------- | -------------------- | ----------------------------------------------------------------------- |
| **Olabiyi Aurel Géoffroy Odjo** | Creator & Maintainer | [odjoaurel@gmail.com](mailto:odjoaurel@gmail.com)                       |
| **Koffi Frederic Sessie**       | Author               | [koffisessie@gmail.com](mailto:koffisessie@gmail.com)                   |
| **Abdoul Oudouss Diakité**      | Author               | [abdouloudoussdiakite@gmail.com](mailto:abdouloudoussdiakite@gmail.com) |
| **Steven P. Sanderson II, MPH** | Author               | [spsanderson@gmail.com](mailto:spsanderson@gmail.com)                   |

---

# 📄 License

AfriMarkets is distributed under the **MIT License**.

See [`LICENSE`](LICENSE) for more information.

---

# 🔗 Links

**Repository:**
https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python

**Issues:**
https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python/issues

---

<div align="center">

### 🌍 Built for African Financial Markets

**AfriMarkets**

*Making African market data more accessible.*

</div>
