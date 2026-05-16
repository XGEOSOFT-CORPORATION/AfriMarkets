"""
Registry system - Permet de paramétrer et gérer tous les marchés
"""
from typing import Dict, Type, Optional


class MarketRegistry:
    """
    Registre centralisé de tous les marchés supportés.
    Permet l'enregistrement dynamique de nouveaux marchés.
    Pattern: Registry pattern + Factory pattern
    """
    
    _markets: Dict[str, Type] = {}
    _market_configs: Dict[str, dict] = {}
    
    @classmethod
    def register(
        cls,
        market_code: str,
        adapter_class: Type,
        config: dict
    ) -> None:
        """
        Enregistre un nouveau marché.
        
        Args:
            market_code: Code court du marché ("BRVM", "NGX", etc.)
            adapter_class: Classe de l'adaptateur (hérite de MarketAdapter)
            config: Configuration du marché
            
        Raises:
            ValueError: Si le marché est déjà enregistré
            
        Examples:
            >>> from afrimarkets.markets.brvm.adapter import BRVMAdapter
            >>> from afrimarkets.core.registry import MarketRegistry, MARKET_CONFIGS
            >>> MarketRegistry.register("BRVM", BRVMAdapter, MARKET_CONFIGS["BRVM"])
        """
        market_code = market_code.upper()
        
        if market_code in cls._markets:
            raise ValueError(f"Market '{market_code}' already registered")
        
        cls._markets[market_code] = adapter_class
        cls._market_configs[market_code] = config
        print(f"✓ Market '{market_code}' registered")
    
    @classmethod
    def get_adapter(cls, market_code: str) -> 'MarketAdapter':
        """
        Récupère l'adaptateur d'un marché.
        
        Args:
            market_code: Code du marché
            
        Returns:
            Instance d'un adaptateur de marché
            
        Raises:
            ValueError: Si le marché n'existe pas
        """
        market_code = market_code.upper()
        adapter_class = cls._markets.get(market_code)
        
        if adapter_class is None:
            raise ValueError(
                f"Market '{market_code}' not found in registry. "
                f"Available: {', '.join(sorted(cls._markets.keys()))}"
            )
        
        config = cls._market_configs.get(market_code, {})
        return adapter_class(config)
    
    @classmethod
    def get_config(cls, market_code: str) -> dict:
        """Récupère la configuration d'un marché"""
        market_code = market_code.upper()
        return cls._market_configs.get(market_code, {})
    
    @classmethod
    def list_markets(cls) -> list:
        """Liste tous les marchés enregistrés"""
        return sorted(list(cls._markets.keys()))
    
    @classmethod
    def is_registered(cls, market_code: str) -> bool:
        """Vérifie si un marché est enregistré"""
        return market_code.upper() in cls._markets
    
    @classmethod
    def unregister(cls, market_code: str) -> None:
        """Désenregistre un marché (utile pour les tests)"""
        market_code = market_code.upper()
        if market_code in cls._markets:
            del cls._markets[market_code]
            del cls._market_configs[market_code]
    
    @classmethod
    def clear_all(cls) -> None:
        """Vide le registre (utile pour les tests)"""
        cls._markets.clear()
        cls._market_configs.clear()


# Configuration globale des marchés
MARKET_CONFIGS = {
    "BRVM": {
        "market_short_name": "BRVM",
        "market_full_name": "Bourse Régionale des Valeurs Mobilières",
        "country": "Côte d'Ivoire",
        "currency": "XOF",
        "official_url": "https://www.brvm.org",
        "market_url": "https://www.brvm.org",
        "market_data_url": "https://www.brvm.org/marches/cours",
    },
    "NGX": {
        "market_short_name": "NGX",
        "market_full_name": "Nigerian Exchange",
        "country": "Nigeria",
        "currency": "NGN",
        "official_url": "https://www.ngxgroup.com",
        "market_url": "https://www.ngxgroup.com",
        "market_data_url": "https://www.investing.com",
        "investing_market_id": "20",
    },
    "GSE": {
        "market_short_name": "GSE",
        "market_full_name": "Ghana Stock Exchange",
        "country": "Ghana",
        "currency": "GHS",
        "official_url": "https://www.gse.com.gh",
        "market_url": "https://www.gse.com.gh",
        "market_data_url": "https://www.gse.com.gh/market-data",
        "investing_market_id": "3",
    },
    "JSE": {
        "market_short_name": "JSE",
        "market_full_name": "Johannesburg Stock Exchange",
        "country": "South Africa",
        "currency": "ZAR",
        "official_url": "https://www.jse.co.za",
        "market_url": "https://www.jse.co.za",
        "market_data_url": "https://www.investing.com",
        "investing_market_id": "110",
    },
    "MSE": {
        "market_short_name": "MSE",
        "market_full_name": "Casablanca Stock Exchange",
        "country": "Morocco",
        "currency": "MAD",
        "official_url": "https://www.bvmt.ma",
        "market_url": "https://www.bvmt.ma",
        "market_data_url": "https://www.investing.com",
        "investing_market_id": "105",
    },
    "EGX": {
        "market_short_name": "EGX",
        "market_full_name": "Egyptian Exchange",
        "country": "Egypt",
        "currency": "EGP",
        "official_url": "https://www.egx.com.eg",
        "market_url": "https://www.egx.com.eg",
        "market_data_url": "https://www.investing.com",
        "investing_market_id": "59",
    },
    "TSE": {
        "market_short_name": "TSE",
        "market_full_name": "Tunis Stock Exchange",
        "country": "Tunisia",
        "currency": "TND",
        "official_url": "https://www.bvmt.tn",
        "market_url": "https://www.bvmt.tn",
        "market_data_url": "https://www.investing.com",
        "investing_market_id": "202",
    },
}
