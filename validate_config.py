#!/usr/bin/env python
"""
Configuration validation script
Valide que toute la structure du projet est correctement configurée.
"""

import os
import sys
from pathlib import Path


def check_structure():
    """Vérifie la structure du projet"""
    print("Vérification de la structure du projet...")
    
    required_dirs = [
        "afrimarkets/core",
        "afrimarkets/markets/brvm",
        "afrimarkets/markets/nge",
        "afrimarkets/markets/gse",
        "afrimarkets/markets/jse",
        "afrimarkets/markets/mse",
        "afrimarkets/markets/egx",
        "afrimarkets/markets/tse",
        "afrimarkets/markets/templates",
        "afrimarkets/data",
        "afrimarkets/indicators",
        "afrimarkets/portfolio",
        "afrimarkets/ml",
        "afrimarkets/dashboard",
        "afrimarkets/utils",
        "tests",
        "docs",
        "examples",
    ]
    
    for dir_path in required_dirs:
        full_path = Path(dir_path)
        if full_path.exists() and full_path.is_dir():
            print(f"  ✓ {dir_path}")
        else:
            print(f"  ✗ {dir_path} - MISSING")
            return False
    
    return True


def check_files():
    """Vérifie les fichiers importants"""
    print("\nVérification des fichiers...")
    
    required_files = [
        "afrimarkets/__init__.py",
        "afrimarkets/core/__init__.py",
        "afrimarkets/core/market.py",
        "afrimarkets/core/registry.py",
        "afrimarkets/core/dispatcher.py",
        "afrimarkets/markets/base.py",
        "afrimarkets/markets/__init__.py",
        "afrimarkets/markets/brvm/adapter.py",
        "afrimarkets/utils/validators.py",
        "afrimarkets/utils/formatters.py",
        "afrimarkets/utils/constants.py",
        "tests/test_market_registry.py",
        "examples/quickstart.py",
        "CONTRIBUTING.md",
        "DEVELOPMENT.md",
    ]
    
    for file_path in required_files:
        full_path = Path(file_path)
        if full_path.exists() and full_path.is_file():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} - MISSING")
            return False
    
    return True


def check_imports():
    """Vérifie que les imports fonctionnent"""
    print("\nVérification des imports...")
    
    try:
        import afrimarkets
        print("  ✓ afrimarkets")
    except ImportError as e:
        print(f"  ✗ afrimarkets - {e}")
        return False
    
    try:
        from afrimarkets import get_tickers, get_data
        print("  ✓ get_tickers, get_data")
    except ImportError as e:
        print(f"  ✗ get_tickers, get_data - {e}")
        return False
    
    try:
        from afrimarkets.core import Market, MarketRegistry
        print("  ✓ Market, MarketRegistry")
    except ImportError as e:
        print(f"  ✗ Market, MarketRegistry - {e}")
        return False
    
    return True


def check_registry():
    """Vérifie l'enregistrement des marchés"""
    print("\nVérification du registre...")
    
    try:
        from afrimarkets.core.registry import MarketRegistry
        
        markets = MarketRegistry.list_markets()
        expected_markets = ["BRVM", "NGX", "GSE", "JSE", "MSE", "EGX", "TSE"]
        
        for market in expected_markets:
            if market in markets:
                print(f"  ✓ {market}")
            else:
                print(f"  ✗ {market} - NOT REGISTERED")
                return False
        
        return True
    except Exception as e:
        print(f"  ✗ Erreur lors de la vérification du registre: {e}")
        return False


def main():
    """Exécute toutes les vérifications"""
    print("=" * 60)
    print("VALIDATION DE LA CONFIGURATION AFRIMARKETS")
    print("=" * 60)
    
    results = []
    
    results.append(("Structure", check_structure()))
    results.append(("Fichiers", check_files()))
    results.append(("Imports", check_imports()))
    results.append(("Registry", check_registry()))
    
    print("\n" + "=" * 60)
    print("RÉSUMÉ")
    print("=" * 60)
    
    for check_name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{check_name}: {status}")
    
    all_passed = all(success for _, success in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ CONFIGURATION CORRECTE!")
        print("=" * 60)
        return 0
    else:
        print("✗ CONFIGURATION INCOMPLÈTE")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
