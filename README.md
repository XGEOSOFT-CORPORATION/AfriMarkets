# AfriMarkets
AfriMarkets is a Python package dedicated to African financial market data analysis and visualization. The project aims to provide an easy-to-use and extensible toolkit for retrieving, cleaning, analyzing, and visualizing market data from African stock exchanges and regional financial markets.

<div align="center">

<img src="https://raw.githubusercontent.com/Koffi-Fredysessie/AfriMarkets-python/main/docs/assets/logo.png" width="160px" alt="AfriMarkets logo"/>

# AfriMarkets — Python

### Access · Analyze · Understand African Capital Markets

[![Python ≥ 3.9](https://img.shields.io/badge/Python-%3E%3D%203.9-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)]()
[![Lifecycle: experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)]()
[![GitHub issues](https://img.shields.io/github/issues/Koffi-Fredysessie/AfriMarkets-python)](https://github.com/Koffi-Fredysessie/AfriMarkets-python/issues)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**AfriMarkets** is a Python package that provides unified, programmatic access
to historical and real-time financial data from African stock exchanges.
It covers the full analytical workflow — from data discovery and retrieval,
through technical analysis, portfolio optimization, and machine learning
forecasting, to interactive dashboards.

[Installation](#-installation) · [Quick Start](#-quick-start) · [Markets](#-supported-markets) · [Modules](#-modules) · [Dashboard](#-interactive-dashboard) · [Contributing](#-contributing)

</div>

---

## 🌍 Why AfriMarkets?

African financial markets represent one of the last frontiers in global finance,
yet remain largely underserved by existing Python financial libraries.
`yfinance`, `pandas-datareader`, and similar tools provide little to no
coverage of African exchanges.

**AfriMarkets** fills that gap:

- **Unified API** across 10 African stock exchanges and multiple data sources
- **Full analytical stack** — data, indicators, portfolio, ML, and dashboards
- **Production-ready** — typed, tested, documented, and CI/CD-integrated
- **Familiar interface** — designed to feel natural alongside `pandas`, `numpy`,
  and `plotly`

---

## ✨ Features

| | Module | Capabilities |
|---|---|---|
| 📊 | **Data** | Ticker discovery, OHLCV retrieval, cleaning, validation, transformation |
| 📈 | **Plotting** | Candlestick charts, volume overlays, technical indicator overlays |
| 📐 | **Indicators** | Trend, momentum, volatility, and moving average indicators |
| 💼 | **Portfolio** | Return/risk metrics, allocation strategies, optimization, performance |
| 🤖 | **ML** | Price forecasting, preprocessing, model wrappers, sentiment analysis |
| 🖥️ | **Dashboard** | Interactive Dash application — no extra coding required |
| 🛠️ | **Utils** | Date helpers, formatters, constants, custom exceptions |

---

## 📦 Installation

### From PyPI *(coming soon)*

```bash
pip install afrimarkets
```

### From GitHub *(current)*

```bash
pip install git+https://github.com/Koffi-Fredysessie/AfriMarkets-python.git
```

### Development install

```bash
git clone https://github.com/Koffi-Fredysessie/AfriMarkets-python.git
cd AfriMarkets-python
pip install -e ".[dev]"
```

> **Requirements:** Python ≥ 3.9, see [`requirements.txt`](requirements.txt)
> for the full dependency list.

---

## 🔑 Supported Markets

| Flag | Code | Exchange | Region |
|---|---|---|---|
| 🌍 | `BRVM` | Bourse Régionale des Valeurs Mobilières | UEMOA (8 countries) |
| 🇬🇭 | `GSE` | Ghana Stock Exchange | Ghana |
| 🇳🇬 | `NGX` | Nigerian Exchange Group | Nigeria |
| 🇿🇦 | `JSE` | Johannesburg Stock Exchange | South Africa |
| 🇲🇦 | `MSE` | Casablanca Stock Exchange | Morocco |
| 🇪🇬 | `EGX` | Egyptian Exchange | Egypt |
| 🇹🇳 | `TSE` | Tunis Stock Exchange | Tunisia |
| 🇰🇪 | `NSE` | Nairobi Securities Exchange | Kenya |
| 🇧🇼 | `BSE` | Botswana Stock Exchange | Botswana |
| 🇲🇺 | `SEM` | Stock Exchange of Mauritius | Mauritius |

---

## 📌 Quick Start

### 1 · Discover available tickers

```python
from afrimarkets.data import get_tickers

# Single market
brvm = get_tickers("BRVM")
print(brvm.shares)        # pandas DataFrame
print(brvm.indexes)       # pandas DataFrame
print(brvm.list_shares)   # list of ticker codes

# All supported markets
all_markets = get_tickers("ALL")
print(all_markets.keys()) # dict_keys(['BRVM', 'GSE', 'NGX', ...])
```

---

### 2 · Download historical OHLCV data

```python
from afrimarkets.data import get_data

# Single ticker — last 90 days (default)
df = get_data("BRVM", ticker="BICC")

# Multiple tickers — custom date range
df = get_data(
    market_code = "BRVM",
    ticker      = ["BICC", "BOAB", "SNTS"],
    from_date   = "2023-01-01",
    to_date     = "2024-12-31"
)

# All shares — wide format
df_wide = get_data("NGX", ticker="ALL SHARES", output_format="wide")

# Both formats at once
result = get_data("JSE", ticker="ALL", output_format="all")
result["long"]   # long format DataFrame
result["wide"]   # wide format DataFrame
```

**Special `ticker` keywords:**

| Keyword | Returns |
|---|---|
| `"ALL"` | All instruments (shares + indexes) |
| `"ALL SHARES"` | Equities only |
| `"ALL INDEXES"` | Indexes only |

**Output DataFrame columns:**

| Column | Type | Description |
|---|---|---|
| `date` | `datetime` | Trading date |
| `ticker` | `str` | Ticker symbol |
| `open` | `float` | Opening price |
| `high` | `float` | Intraday high |
| `low` | `float` | Intraday low |
| `close` | `float` | Closing price |
| `volume` | `float` | Trading volume |

---

### 3 · Plot interactive charts

```python
from afrimarkets.plotting import candlestick

# Single ticker — candlestick + volume
fig = candlestick.plot("BRVM", ticker="BICC", from_date="2023-01-01")
fig.show()

# Multiple tickers simultaneously — grouped line chart
fig = candlestick.plot(
    market    = "BRVM",
    ticker    = ["BICC", "BOAB", "SNTS"],
    from_date = "2023-01-01"
)
fig.show()

# From an existing DataFrame
fig = candlestick.from_df(df, up_color="green", down_color="red")
fig.show()
```

---

### 4 · Compute technical indicators

```python
from afrimarkets.indicators import trend, momentum, volatility, moving_average

# Moving averages
df["sma_20"]        = moving_average.sma(df["close"], window=20)
df["ema_50"]        = moving_average.ema(df["close"], window=50)
df["wma_14"]        = moving_average.wma(df["close"], window=14)

# Trend
df["adx"]           = trend.adx(df)
df["macd"]          = trend.macd(df["close"])
df["parabolic_sar"] = trend.parabolic_sar(df)

# Momentum
df["rsi"]           = momentum.rsi(df["close"], period=14)
df["stoch"]         = momentum.stochastic(df)
df["cci"]           = momentum.cci(df)

# Volatility
df["bb_upper"], df["bb_lower"] = volatility.bollinger_bands(df["close"])
df["atr"]           = volatility.atr(df)
df["keltner"]       = volatility.keltner_channel(df)
```

---

### 5 · Portfolio analysis

```python
from afrimarkets.portfolio import performance, risk, optimization, allocation

# Fetch multi-ticker data
df = get_data(
    "BRVM",
    ticker    = ["BICC", "BOAB", "SNTS", "SGBCI"],
    from_date = "2023-01-01"
)

# Performance metrics
perf = performance.compute(df)
print(perf)

# Portfolio optimisation
weights = optimization.max_sharpe(df)    # maximum Sharpe ratio
weights = optimization.min_variance(df)  # minimum variance
weights = optimization.risk_parity(df)   # risk parity

# Capital allocation
portfolio = allocation.build(df, weights=weights, capital=1_000_000)
print(portfolio)
```

**Performance metrics computed:**

| Metric | Formula |
|---|---|
| Total Return (%) | `(P_end / P_start − 1) × 100` |
| Annualised Return (%) | `(P_end / P_start)^(252/n) − 1` |
| Annualised Volatility (%) | `σ(log returns) × √252 × 100` |
| Sharpe Ratio | `μ(log returns) / σ(log returns) × √252` |
| Sortino Ratio | `μ(log returns) / σ(downside) × √252` |
| Calmar Ratio | `Annualised Return / \|Max Drawdown\|` |
| Max Drawdown (%) | `min((P − cummax(P)) / cummax(P))` |
| VaR 95% | `5th percentile of daily returns` |
| CVaR 95% | `Mean of returns below VaR` |

> Sharpe and Sortino ratios assume a risk-free rate of **zero**.

---

### 6 · Machine learning & forecasting

```python
from afrimarkets.ml import forecasting, preprocessing, models, sentiment

# Feature engineering
X, y = preprocessing.prepare_features(df, target="close", lags=10)
X_train, X_test, y_train, y_test = preprocessing.split(X, y, test_size=0.2)

# Model wrappers
model = models.LSTMForecaster(units=64, dropout=0.2)
model.fit(X_train, y_train, epochs=50)
preds = model.predict(X_test)

model = models.XGBoostForecaster(n_estimators=200)
model.fit(X_train, y_train)
preds = model.predict(X_test)

# End-to-end forecasting pipeline
forecast = forecasting.run(
    df      = df,
    ticker  = "BICC",
    horizon = 30,       # days ahead
    model   = "lstm",   # "lstm" | "xgboost" | "prophet" | "arima"
    plot    = True
)

# News sentiment scoring
score = sentiment.analyze(ticker="BICC", market="BRVM")
```

---

### 7 · Launch the interactive dashboard

```python
from afrimarkets.dashboard import app

# Default — all markets, port 8050
app.run(debug=False)

# Custom port and market subset
app.run(
    port              = 8051,
    supported_markets = ["BRVM", "NGX", "JSE"]
)
```

**Dashboard tabs:**

| Tab | Content |
|---|---|
| 🕯️ **Chart** | Interactive candlestick or multi-ticker line chart |
| 📋 **OHLCV Data** | Filterable, sortable data table with CSV export |
| 🏆 **Performance** | Full KPI table per ticker |
| 📐 **Indicators** | Technical indicator overlays on price chart |
| 💼 **Portfolio** | Weight optimisation and allocation visualisation |
| 🤖 **Forecast** | ML price forecast with confidence intervals |
| 🧪 **Stats** | Normality and stationarity test results |

---

## 📁 Project Structure

```
AfriMarkets/
│
├── afrimarkets/
│   ├── __init__.py
│   │
│   ├── data/                    # Data retrieval and processing
│   │   ├── api.py               # HTTP session management, request handling
│   │   ├── loaders.py           # get_tickers(), get_data() — public API
│   │   ├── cleaning.py          # Missing values, outliers, type coercion
│   │   ├── transformers.py      # Long ↔ wide pivoting, resampling
│   │   └── validators.py        # Input validation, market code checks
│   │
│   ├── plotting/                # Interactive charts (Plotly)
│   │   ├── candlestick.py       # OHLC candlestick + multi-ticker line
│   │   ├── volume.py            # Volume bar overlays
│   │   ├── indicators.py        # Technical indicator overlays
│   │   └── dashboard.py         # Chart composition helpers
│   │
│   ├── indicators/              # Technical analysis
│   │   ├── trend.py             # ADX, MACD, Parabolic SAR, Ichimoku
│   │   ├── momentum.py          # RSI, Stochastic, CCI, Williams %R
│   │   ├── volatility.py        # Bollinger Bands, ATR, Keltner Channel
│   │   └── moving_average.py    # SMA, EMA, WMA, DEMA, TEMA
│   │
│   ├── portfolio/               # Portfolio management
│   │   ├── performance.py       # Return, Sharpe, Sortino, Calmar, drawdown
│   │   ├── risk.py              # VaR, CVaR, Beta, correlation matrix
│   │   ├── optimization.py      # Max Sharpe, Min Variance, Risk Parity
│   │   └── allocation.py        # Capital allocation, rebalancing
│   │
│   ├── ml/                      # Machine learning & forecasting
│   │   ├── preprocessing.py     # Feature engineering, lag creation, scaling
│   │   ├── models.py            # LSTM, XGBoost, Prophet, ARIMA wrappers
│   │   ├── forecasting.py       # End-to-end forecasting pipeline
│   │   └── sentiment.py         # News sentiment scoring
│   │
│   ├── dashboard/               # Interactive Dash application
│   │   ├── app.py               # Entry point — app.run()
│   │   ├── layouts.py           # Page and tab layout definitions
│   │   └── callbacks.py         # Dash reactive callbacks
│   │
│   ├── utils/                   # Shared utilities
│   │   ├── dates.py             # Date parsing, trading calendar helpers
│   │   ├── formatting.py        # Number formatting, table styling
│   │   ├── constants.py         # Market registry, default values
│   │   └── exceptions.py        # Custom exception classes
│   │
│   └── datasets/                # Bundled sample datasets
│
├── tests/
│   ├── test_data.py
│   ├── test_plotting.py
│   ├── test_indicators.py
│   └── test_portfolio.py
│
├── examples/
│   ├── basic_usage.py
│   ├── portfolio_example.py
│   └── dashboard_example.py
│
├── docs/
│
├── .github/
│   └── workflows/
│       └── python-package.yml
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── setup.py
```

---

## ⚙️ Dependencies

### Core

| Category | Packages |
|---|---|
| Data wrangling | `pandas`, `numpy` |
| HTTP & scraping | `requests`, `httpx`, `beautifulsoup4`, `lxml` |
| Visualization | `plotly`, `dash`, `dash-bootstrap-components` |
| Statistics | `scipy`, `statsmodels` |
| Portfolio | `cvxpy`, `PyPortfolioOpt` |
| ML / Forecasting | `scikit-learn`, `xgboost`, `prophet` |
| Deep learning | `tensorflow` / `torch` *(optional)* |
| Utils | `python-dateutil`, `pytz`, `tqdm` |

### Development

```bash
pip install afrimarkets[dev]
# installs: pytest, black, flake8, mypy, sphinx, pre-commit
```

---

## 🧠 Use Cases

- 📐 **Academic research** — market efficiency, volatility clustering, cointegration
- 💼 **Portfolio management** — cross-market diversification, risk budgeting
- 🔬 **Quantitative finance** — factor models, event studies, pairs trading
- 🤖 **ML research** — price prediction, regime detection, alternative data
- 🗺️ **Data journalism** — African market trend visualisation
- 🎓 **Teaching** — real market data for finance and data science courses

---

## 🗺️ Roadmap

- [x] Project structure and architecture design
- [ ] `data` module — ticker discovery and OHLCV retrieval
- [ ] `plotting` module — candlestick and multi-ticker charts
- [ ] `indicators` module — full technical indicator library
- [ ] `portfolio` module — performance and risk metrics
- [ ] `dashboard` module — interactive Dash application
- [ ] `ml` module — forecasting pipeline
- [ ] PyPI publication
- [ ] Full Sphinx / MkDocs documentation
- [ ] REST API wrapper *(future)*

---

## 🤝 Contributing

Contributions are welcome at every level — bug fixes, new markets,
new indicators, documentation, or ML models.

```bash
# 1. Fork and clone
git clone https://github.com/Koffi-Fredysessie/AfriMarkets-python.git
cd AfriMarkets-python

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# 3. Install in dev mode
pip install -e ".[dev]"

# 4. Create a feature branch
git checkout -b feature/add-xyz-market

# 5. Run tests
pytest tests/ -v

# 6. Format and lint
black afrimarkets/
flake8 afrimarkets/

# 7. Push and open a Pull Request
git push origin feature/add-xyz-market
```

> Please open an **issue** first to discuss major changes.

**Adding a new market requires only two steps:**

1. Add an entry to `utils/constants.py` — market registry
2. Add the fetch logic to `data/loaders.py`

---

## 🐛 Bug Reports & Feature Requests

Found a bug or want a new feature?  
👉 [Open an issue](https://github.com/Koffi-Fredysessie/AfriMarkets-python/issues)

Please include:

- Python version → `python --version`
- AfriMarkets version → `import afrimarkets; print(afrimarkets.__version__)`
- Full traceback
- Minimal reproducible example

---

## 🔗 Related

| Project | Language | Link |
|---|---|---|
| AfriMarkets | R | [github.com/Koffi-Fredysessie/AfriMarkets](https://github.com/Koffi-Fredysessie/AfriMarkets) |
| AfriMarkets | Python | *this repository* |

---

## 👥 Authors

| Name | Role | Contact |
|---|---|---|
| **Olabiyi Aurel Géoffroy Odjo** | Creator & maintainer | odjoaurel@gmail.com |
| **Koffi Frederic Sessie** | Author | koffisessie@gmail.com |
| **Abdoul Oudouss Diakité** | Author | abdouloudoussdiakite@gmail.com |
| **Steven P. Sanderson II, MPH** | Author | spsanderson@gmail.com |

---

## 📄 License

This project is licensed under the **MIT License** — see the
[LICENSE](LICENSE) file for full details.

---

<div align="center">

Made with ❤️ for African financial markets

⭐ **Star the repository** if AfriMarkets is useful to you — it helps others discover it.

🌍 *Empowering African financial data, one commit at a time.*

</div>

