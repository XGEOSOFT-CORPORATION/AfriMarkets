"""
Development environment setup and configuration
"""

# ============================================================================
# Installation et Configuration de l'environnement de développement
# ============================================================================

SETUP_INSTRUCTIONS = """
# SETUP DÉVELOPPEMENT AFRIMARKETS

## 1. Cloner le repository
```bash
git clone https://github.com/Koffi-Fredysessie/AfriMarkets-python.git
cd AfriMarkets-python
```

## 2. Créer un environnement virtuel
```bash
# Avec venv
python -m venv venv

# Activer l'environnement
# Windows
venv\\Scripts\\activate
# macOS/Linux
source venv/bin/activate
```

## 3. Installer les dépendances
```bash
# Dépendances de base
pip install -r requirements.txt

# Dépendances de développement
pip install -r requirements-dev.txt

# Installation en mode développement
pip install -e .
```

## 4. Vérifier l'installation
```bash
python -c "import afrimarkets; print(afrimarkets.__version__)"
```

## 5. Exécuter les tests
```bash
pytest tests/ -v

# Avec coverage
pytest tests/ --cov=afrimarkets --cov-report=html
```

## 6. Formater le code
```bash
# Black formatter
black afrimarkets/ tests/

# isort pour les imports
isort afrimarkets/ tests/

# Linting
flake8 afrimarkets/ tests/

# Type checking
mypy afrimarkets/
```

---

## Structure d'un développeur

```
Mon environnement de développement:

project/
├── venv/                    # Environnement virtuel
├── afrimarkets/             # Source code
├── tests/                   # Tests
├── docs/                    # Documentation
└── examples/                # Exemples

# Workflow typique
1. Activer venv: source venv/bin/activate
2. Créer une branche: git checkout -b feature/my-feature
3. Développer le code
4. Tester: pytest
5. Formatter: black && isort
6. Commit et push
7. Créer une PR
```

---

## Variables d'environnement (optionnel)

```bash
# Pour les tests avec vraies données (si applicable)
export AFRIMARKETS_API_KEY="votre_clé"
export AFRIMARKETS_TEST_MODE=true
```

---

## Dépannage

### Python version
```bash
# Vérifier la version (doit être >= 3.9)
python --version

# Utiliser une version spécifique
pyenv versions
pyenv install 3.11.0
pyenv local 3.11.0
```

### Importer le package localement
```bash
# Depuis le répertoire du projet
cd /chemin/vers/AfriMarkets
pip install -e .

# Vérifier l'installation
python -c "from afrimarkets import get_tickers; print(get_tickers('BRVM'))"
```

### Régénérer les fichiers compilés
```bash
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

---

## Utiles pour le développement

### Run quickstart
```bash
python examples/quickstart.py
```

### Déboguer un test
```bash
pytest tests/test_brvm.py::TestBRVMMarket::test_get_brvm_tickers -v -s
```

### Générer un rapport de couverture
```bash
pytest --cov=afrimarkets --cov-report=html
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

### Lister les markets disponibles
```bash
python -c "from afrimarkets.core.registry import MarketRegistry; print(MarketRegistry.list_markets())"
```

---

## Ressources utiles

- [Python 3.9+ docs](https://docs.python.org/3/)
- [Pandas documentation](https://pandas.pydata.org/)
- [pytest documentation](https://docs.pytest.org/)
- [Black code formatter](https://black.readthedocs.io/)
- [Pylance documentation](https://github.com/microsoft/pylance-release)

---

Besoin d'aide? Consultez CONTRIBUTING.md ou ouvrez une issue!
"""

if __name__ == "__main__":
    print(SETUP_INSTRUCTIONS)
