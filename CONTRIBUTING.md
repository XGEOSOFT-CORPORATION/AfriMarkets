"""
CONTRIBUTING - Guide pour contribuer au projet AfriMarkets

Merci de votre intérêt pour contribuer à AfriMarkets! Ce guide explique comment
ajouter de nouveaux marchés, fonctionnalités, ou améliorer le code existant.

## 🚀 Ajouter un nouveau marché

C'est l'une des contributions les plus utiles!

### Étapes rapides:

1. **Consulter le template**
   ```bash
   cat afrimarkets/markets/templates/README.md
   ```

2. **Créer la structure**
   ```bash
   mkdir -p afrimarkets/markets/XXX/legacy
   ```

3. **Implémenter l'adaptateur**
   - Copier `templates/adapter.py` vers `XXX/adapter.py`
   - Implémenter `get_tickers()` et `get_data()`
   - Créer le code legacy dans `legacy/`

4. **Enregistrer le marché**
   - Ajouter la configuration dans `core/registry.py`
   - Enregistrer dans `markets/__init__.py`

5. **Tester**
   ```bash
   pytest tests/markets/test_xxx.py -v
   ```

6. **Ouvrir une Pull Request**

### Exemple d'adaptateur (template)

Voir: `afrimarkets/markets/templates/adapter.py`

## 🔧 Structure du projet

```
afrimarkets/
├── core/                  # Classes Core (Market, Registry, Dispatcher)
├── markets/               # Adaptateurs pour chaque marché
│   ├── brvm/             # Adaptateur BRVM + legacy code
│   ├── nge/              # Adaptateur NGX
│   ├── templates/        # Template pour nouveau marché
│   └── __init__.py       # Enregistrement automatique
├── data/                 # Models et utilitaires de données
├── indicators/           # Analyse technique (TODO)
├── portfolio/            # Optimisation (TODO)
├── ml/                   # Machine learning (TODO)
├── dashboard/            # Dashboards (TODO)
├── utils/                # Utilitaires (validators, formatters, constants)
└── tests/                # Suite de tests
```

## 📝 Directives de code

### Style
- Respecter PEP 8
- Utiliser black pour formater: `black afrimarkets/`
- Utiliser mypy pour les types: `mypy afrimarkets/`

### Docstrings
- Utiliser le format NumPy/Google
- Inclure Args, Returns, Raises, Examples

### Tests
- Chaque fonction/classe doit avoir des tests
- Tester les cas d'erreur aussi
- Coverage minimum: 80%

```bash
pytest tests/ --cov=afrimarkets --cov-report=html
```

### Commits
- Messages clairs et en anglais
- Format: `type: description`
  - `feat:` Nouvelle fonctionnalité
  - `fix:` Correction de bug
  - `docs:` Documentation
  - `market:` Ajout d'un marché
  - `refactor:` Refactorisation

## 🧪 Tests

### Exécuter les tests
```bash
# Tous les tests
pytest

# Tests pour un fichier
pytest tests/markets/test_brvm.py

# Avec verbose
pytest -v

# Avec coverage
pytest --cov=afrimarkets
```

### Ajouter un test
```python
# tests/markets/test_new_market.py
from afrimarkets import get_tickers, get_data

def test_get_tickers_xxx():
    """Test récupération des tickers"""
    market = get_tickers("XXX")
    assert market is not None
    assert len(market.list_shares) > 0

def test_get_data_xxx():
    """Test récupération des données"""
    df = get_data("XXX", ticker="TICKER")
    assert not df.empty
    assert "Date" in df.columns
    assert "Close" in df.columns
```

## 📚 Documentation

### Mettre à jour la documentation
- Modifier les fichiers dans `docs/source/`
- Utiliser reStructuredText ou Markdown
- Ajouter des exemples

### Générer la documentation
```bash
cd docs
make html
# Ouvrir build/html/index.html
```

## 🤝 Process de contribution

1. **Fork** le repository
2. **Créer une branche** pour votre feature
   ```bash
   git checkout -b market/xxx
   git checkout -b feature/my-feature
   ```
3. **Commit** vos changements
   ```bash
   git commit -m "market: add XXX stock exchange"
   ```
4. **Push** vers votre fork
   ```bash
   git push origin feature/my-feature
   ```
5. **Ouvrir une Pull Request** avec description

## 🐛 Reporter des bugs

1. Vérifier que le bug n'a pas déjà été reporté
2. Ouvrir une issue avec:
   - Description du problème
   - Étapes de reproduction
   - Comportement attendu vs réel
   - Versions (Python, AfriMarkets, dépendances)
   - Logs/tracebacks

## 💡 Proposer des améliorations

1. Ouvrir une issue de discussion
2. Décrire l'amélioration
3. Expliquer les bénéfices
4. Si approuvé, implémenter

## 📮 Aide et Support

- **Issues**: Pour les bugs et feature requests
- **Discussions**: Pour les questions générales
- **Pull Requests**: Pour les contributions

## 🙏 Remerciements

Merci d'avoir contribué à AfriMarkets! Votre aide est précieuse pour rendre
les données des marchés financiers africains accessibles à tous.

---

Questions? N'hésitez pas à ouvrir une issue!
"""
