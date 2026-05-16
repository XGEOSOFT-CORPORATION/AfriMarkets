"""
Markets module - All market adapters and registry
"""
from afrimarkets.core.registry import MarketRegistry, MARKET_CONFIGS

# Import all market adapters
from afrimarkets.markets.brvm.adapter import BRVMAdapter
from afrimarkets.markets.nge.adapter import NGXAdapter
from afrimarkets.markets.gse.adapter import GSEAdapter
from afrimarkets.markets.jse.adapter import JSEAdapter
from afrimarkets.markets.mse.adapter import MSEAdapter
from afrimarkets.markets.egx.adapter import EGXAdapter
from afrimarkets.markets.tse.adapter import TSEAdapter

__all__ = [
    "BRVMAdapter",
    "NGXAdapter",
    "GSEAdapter",
    "JSEAdapter",
    "MSEAdapter",
    "EGXAdapter",
    "TSEAdapter",
]


def register_all_markets():
    """
    Enregistre tous les marchés supportés.
    Appelé automatiquement à l'import du module.
    """
    adapters = {
        "BRVM": BRVMAdapter,
        "NGX": NGXAdapter,
        "GSE": GSEAdapter,
        "JSE": JSEAdapter,
        "MSE": MSEAdapter,
        "EGX": EGXAdapter,
        "TSE": TSEAdapter,
    }
    
    for market_code, adapter_class in adapters.items():
        config = MARKET_CONFIGS.get(market_code, {})
        try:
            MarketRegistry.register(market_code, adapter_class, config)
        except ValueError as e:
            # Market already registered (peut arriver lors des tests)
            pass


# Auto-register on import
register_all_markets()
