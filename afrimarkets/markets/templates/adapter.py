"""
TEMPLATE - Template pour créer un nouvel adaptateur de marché.
Copier ce fichier et remplacer NEW_MARKET par le code du marché.

Checklist pour ajouter un nouveau marché:
- [ ] Copier ce fichier vers afrimarkets/markets/NEW_MARKET/adapter.py
- [ ] Remplacer NewMarketAdapter par le nom de la classe appropriée
- [ ] Implémenter get_tickers()
- [ ] Implémenter get_data()
- [ ] Créer les fichiers legacy/ si nécessaire
- [ ] Ajouter les tests dans tests/markets/test_new_market.py
- [ ] Enregistrer dans afrimarkets/markets/__init__.py
"""
from datetime import datetime
from typing import Optional
import pandas as pd
from afrimarkets.markets.base import MarketAdapter


class NewMarketAdapter(MarketAdapter):
    """
    Adaptateur pour le marché NEW_MARKET.
    
    TODO:
    - [ ] Implémenter get_tickers()
    - [ ] Implémenter get_data()
    - [ ] Créer les fichiers legacy/
    - [ ] Ajouter des tests
    - [ ] Documenter les sources de données
    """
    
    def __init__(self, config: dict):
        """
        Initialise l'adaptateur.
        
        Args:
            config: Configuration du marché (voir MARKET_CONFIGS)
        """
        super().__init__(config)
        # TODO: Initialiser les sources de données
    
    def get_tickers(self) -> object:
        """
        Récupère tous les tickers du marché.
        
        Returns:
            Market object avec :
            - list_indexes: List de symboles d'indices
            - list_shares: List de symboles d'actions
            - list_bonds: List de symboles d'obligations (si applicable)
            - indexes: DataFrame avec détails des indices
            - shares: DataFrame avec détails des actions
            - bonds: DataFrame avec détails des obligations (si applicable)
            
        Raises:
            NotImplementedError: Si non implémentée
            
        Notes:
            Les DataFrames doivent au minimum contenir:
            - Colonne "Ticker": Symbole du titre
            - Colonne "Name": Nom complet du titre
        """
        raise NotImplementedError("get_tickers() not implemented for this market")
    
    def get_data(
        self,
        ticker: str,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        period: str = "daily"
    ) -> pd.DataFrame:
        """
        Récupère les données OHLCV pour un ou plusieurs tickers.
        
        Args:
            ticker: 
                - Ticker unique (ex: "SNTS")
                - "ALL": tous les instruments
                - "ALL SHARES": toutes les actions
                - "ALL INDEXES": tous les indices
            from_date: Date de début (default: 89 jours avant aujourd'hui)
            to_date: Date de fin (default: aujourd'hui)
            period: Fréquence ("daily", "weekly", "monthly")
        
        Returns:
            DataFrame avec colonnes:
            - Date: Date de la cotation
            - Ticker: Symbole du titre
            - Open: Prix d'ouverture
            - High: Prix le plus haut
            - Low: Prix le plus bas
            - Close: Prix de fermeture
            - Volume: Volume échangé (si disponible)
        
        Raises:
            NotImplementedError: Si non implémentée
            ValueError: Si le ticker n'existe pas
        """
        raise NotImplementedError("get_data() not implemented for this market")
