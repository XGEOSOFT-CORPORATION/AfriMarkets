# AfriMarkets

**Documentation:** [Français](#français) | [English](#english) | [Yorùbá](#yorùbá)

AfriMarkets est un package Python open source qui fournit une interface simple
pour les marchés financiers africains. Le projet est actuellement en **alpha
(0.1.0)** et inclut la registry des marchés ainsi que le support initial de la
BRVM.

Les connecteurs pour récupérer les tickers et les historiques de prix sont
encore en développement.

Le projet veut rendre les marchés africains plus accessibles aux développeurs,
chercheurs, fintechs et investisseurs. Il peut faciliter la création d'outils
de suivi, d'analyse et de recherche adaptés aux réalités régionales.

## Français

### Installation

Python 3.12 ou une version plus récente est nécessaire.

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git
cd AfriMarkets-python
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
python -m pip install -e .
```

### Utilisation

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

Lorsque la connexion Internet est stable, `BRVM()` récupère automatiquement les
tickers du marché à l'initialisation. Pour les récupérer ou les actualiser à
nouveau dans l'instance locale :

```python
tickers = market.get_tickers()
print(market.tickers)
```

On peut aussi consulter les marchés disponibles :

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())       # ['BRVM']
market = get_market("BRVM")
print(market.code)               # BRVM
```

Pour créer un actif :

```python
from afrimarkets.assets import Share

share = Share(symbol="BOAB", name="Entreprise exemple")
print(share.info())
```

`get_tickers()` actualise les tickers chargés localement par l'instance. Une
connexion stable est nécessaire pour récupérer les données en ligne.
AfriMarkets ne fournit pas de conseil en investissement et ne garantit pas
l'exactitude des données.

Les contributions sont les bienvenues pour ajouter des marchés, améliorer les
connecteurs, renforcer les tests et développer les outils d'analyse. Chaque
contribution aide à étendre la puissance et l'utilité du package en Afrique.

## English

AfriMarkets is an open-source Python package providing a simple interface for
African financial markets. It is currently **alpha (0.1.0)** and includes a
market registry and initial BRVM support.

Ticker and historical-price connectors are still under development.

### Installation

Python 3.12 or later is required.

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git
cd AfriMarkets-python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e .
```

### Usage

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

With a stable Internet connection, `BRVM()` automatically retrieves the
market tickers during initialization. To retrieve and refresh them again in
the local instance:

```python
tickers = market.get_tickers()
print(market.tickers)
```

Available markets can also be listed:

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())       # ['BRVM']
market = get_market("BRVM")
print(market.code)               # BRVM
```

An asset can be created directly:

```python
from afrimarkets.assets import Share

share = Share(symbol="BOAB", name="Example company")
print(share.info())
```

`get_tickers()` refreshes the tickers loaded locally by the instance. A stable
connection is required to retrieve online data. AfriMarkets does not provide
investment advice or guarantee data accuracy.

Contributors are welcome to add markets, improve connectors, strengthen tests
and develop analysis tools. Every contribution helps expand the package's
power and usefulness across Africa.

## Yorùbá

AfriMarkets jẹ́ package Python open source tí ó ń pèsè ọ̀nà rọrùn fún lílo data
ọjà ìṣúná Áfíríkà. Ó wà ní ipò **alpha (0.1.0)**, ó sì ní market registry àti
ìbẹ̀rẹ̀ support fún BRVM.

Àwọn connector fún tickers àti data ìtàn kò tíì parí.

### Fifi sori ẹrọ

Python 3.12 tàbí tuntun ju bẹ́ẹ̀ lọ ni a nílò.

```bash
git clone https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python.git
cd AfriMarkets-python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e .
```

### Lílò

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

Nígbà tí ìbáṣepọ̀ Internet bá dúró ṣinṣin, `BRVM()` máa ń gba àwọn ticker ọjà
wọlé láìsí ìgbésẹ̀ míì nígbà ìbẹ̀rẹ̀. A lè tún gba wọn, kí a sì tún wọn ṣe nínú
instance local, pẹ̀lú:

```python
tickers = market.get_tickers()
print(market.tickers)
```

A tún lè wo àwọn ọjà tó wà:

```python
from afrimarkets.markets import available_markets, get_market

print(available_markets())       # ['BRVM']
market = get_market("BRVM")
print(market.code)               # BRVM
```

Láti dá asset sílẹ̀:

```python
from afrimarkets.assets import Share

share = Share(symbol="BOAB", name="Àpẹẹrẹ ilé-iṣẹ́")
print(share.info())
```

`get_tickers()` máa ń tún àwọn ticker tí instance náà kó sílẹ̀ ṣe. Internet tó
duro ṣinṣin ṣe pàtàkì fún gbigba data online. AfriMarkets kì í ṣe ìmọ̀ràn fún
investment, kò sì ṣe ìdánilójú pé data máa péye.

Àwọn contributor káàbọ̀ láti fi ọjà tuntun, connector, tests àti irinṣẹ́
ìtúpalẹ̀ kún un. Gbogbo contribution máa ń ran package náà lọ́wọ́ láti lágbára
sí i àti láti wúlò fún Áfíríkà.

## Licence et liens | License and links | Licence àti àwọn ìtọ́kasí



## 👥 Authors

| Name | Role | Contact |
|---|---|---|
| **Olabiyi Aurel Géoffroy Odjo** | Creator & maintainer | odjoaurel@gmail.com |
| **Koffi Frederic Sessie** | Author | koffisessie@gmail.com |
| **Abdoul Oudouss Diakité** | Author | abdouloudoussdiakite@gmail.com |
| **Steven P. Sanderson II, MPH** | Author | spsanderson@gmail.com |

---

AfriMarkets est distribué sous licence MIT. Consultez le fichier `LICENSE`.

- Dépôt / Repository: https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python
- Issues: https://github.com/XGEOSOFT-CORPORATION/AfriMarkets-python/issues

