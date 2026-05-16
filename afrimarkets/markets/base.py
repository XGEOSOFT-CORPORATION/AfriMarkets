"""
Base adapter class - Pattern Template Method pour tous les marchés
"""
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime, timedelta
import pandas as pd
from afrimarkets.core.market import Market


class MarketAdapter(ABC):
    """
    Classe abstraite pour tous les adaptateurs de marché.
    Définit l'interface que tous les adaptateurs doivent implémenter.
    
    Pattern: Template Method + Strategy Pattern
    
    Chaque adaptateur doit implémenter:
    - get_tickers(): Récupère les indices, actions et obligations
    - get_data(): Récupère les données OHLCV historiques
    
    Examples:
        >>> from afrimarkets.markets.brvm.adapter import BRVMAdapter
        >>> from afrimarkets.core.registry import MARKET_CONFIGS
        >>> 
        >>> adapter = BRVMAdapter(MARKET_CONFIGS["BRVM"])
        >>> market = adapter.get_tickers()
        >>> data = adapter.get_data("SNTS", from_date="2023-01-01")
    """
    
    def __init__(self, config: dict):
        """
        Initialise l'adaptateur avec sa configuration.
        
        Args:
            config: Dictionnaire de configuration du marché
        """
        self.config = config
        self.market = self._create_market()
    
    def _create_market(self) -> Market:
        """
        Crée l'objet Market à partir de la configuration.
        Appelé automatiquement dans __init__.
        
        Returns:
            Market object avec les métadonnées
        """
        return Market(
            market_short_name=self.config.get("market_short_name", ""),
            market_full_name=self.config.get("market_full_name", ""),
            official_url=self.config.get("official_url", ""),
            market_url=self.config.get("market_url", ""),
            market_data_url=self.config.get("market_data_url", ""),
            country=self.config.get("country", ""),
            currency=self.config.get("currency", ""),
        )
    
    # ========== Méthodes abstraites (à implémenter par chaque marché) ==========
    
    @abstractmethod
    def get_tickers(self) -> Market:
        """
        Récupère tous les tickers (indices, actions, obligations).
        Retourne un objet Market rempli avec les listes et DataFrames.
        
        Returns:
            Market object avec :
            - list_indexes: List de symboles d'indices
            - list_shares: List de symboles d'actions
            - list_bonds: List de symboles d'obligations (si applicable)
            - indexes: DataFrame avec détails des indices
            - shares: DataFrame avec détails des actions
            - bonds: DataFrame avec détails des obligations
            
        Raises:
            NotImplementedError: Si non implémentée dans la sous-classe
            
        Notes:
            Les DataFrames doivent au minimum contenir:
            - Colonne "Ticker": Symbole du titre
            - Colonne "Name": Nom complet du titre (optionnel)
        """
        pass
    
    @abstractmethod
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
            NotImplementedError: Si non implémentée dans la sous-classe
            ValueError: Si le ticker n'existe pas
            
        Examples:
            >>> adapter.get_data("SNTS", from_date="2023-01-01", to_date="2023-12-31")
            >>> adapter.get_data("ALL SHARES")  # Tous les tickers
        """
        pass
    
    # ========== Méthodes utilitaires ==========
    
    def validate_ticker(self, ticker: str) -> bool:
        """
        Valide qu'un ticker existe dans ce marché.
        
        Args:
            ticker: Symbole à valider
            
        Returns:
            True si le ticker existe, False sinon
        """
        return ticker.upper() in [t.upper() for t in self.market.all_tickers]
    
    def normalize_dates(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None
    ) -> tuple:
        """
        Normalise les dates.
        
        Args:
            from_date: Date de début (None -> 89 jours avant to_date)
            to_date: Date de fin (None -> aujourd'hui)
            
        Returns:
            Tuple (from_date, to_date) au format datetime.date
        """
        # Convertir en date si datetime
        if isinstance(to_date, datetime):
            to_date = to_date.date()
        if isinstance(from_date, datetime):
            from_date = from_date.date()
        
        # Appliquer les défauts
        if to_date is None:
            to_date = datetime.now().date()
        if from_date is None:
            from_date = to_date - timedelta(days=89)
        
        return from_date, to_date
    
    def __repr__(self) -> str:
        """Représentation textuelle de l'adaptateur"""
        return f"<{self.__class__.__name__} for {self.market.market_short_name}>"
