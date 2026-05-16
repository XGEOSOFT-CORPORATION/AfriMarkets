"""
Market class definition - représente la structure de base d'un marché
"""
from dataclasses import dataclass, field
from typing import Optional
import pandas as pd


@dataclass
class Market:
    """
    Représente la structure de base d'un marché africain.
    
    Attributes:
        market_short_name: Code court du marché (ex: "BRVM", "NGX")
        market_full_name: Nom complet du marché
        official_url: URL officielle du marché
        market_url: URL de marché
        market_data_url: URL pour accéder aux données
        country: Pays où se trouve le marché
        currency: Devise utilisée (XOF, NGN, ZAR, etc.)
        list_indexes: Liste des indices du marché
        list_shares: Liste des actions du marché
        list_bonds: Liste des obligations du marché
        indexes: DataFrame avec informations détaillées sur les indices
        shares: DataFrame avec informations détaillées sur les actions
        bonds: DataFrame avec informations détaillées sur les obligations
    """
    # Métadonnées
    market_short_name: str           # "BRVM", "NGX", etc.
    market_full_name: str            # "Bourse Régionale des Valeurs Mobilières"
    official_url: str                # URL officielle
    market_url: str                  # URL de marché
    market_data_url: str             # URL pour les données
    country: str                     # Pays
    currency: str                    # Devise (XOF, NGN, etc.)
    
    # Listes de tickers
    list_indexes: list = field(default_factory=list)           # ["BRVM10", "BRVM Composite", ...]
    list_shares: list = field(default_factory=list)            # ["SNTS", "SGBCI", ...]
    list_bonds: list = field(default_factory=list)             # Obligations si applicable
    
    # DataFrames contenant les détails
    indexes: Optional[pd.DataFrame] = None                      # DataFrame avec infos des indices
    shares: Optional[pd.DataFrame] = None                       # DataFrame avec infos des actions
    bonds: Optional[pd.DataFrame] = None                        # DataFrame avec infos des obligations
    
    @property
    def all_tickers(self) -> list:
        """Retourne tous les tickers (indices + actions + obligations)"""
        return self.list_indexes + self.list_shares + self.list_bonds
    
    @property
    def all_tickers_list(self) -> list:
        """Alias pour compatibilité R - retourne List = all_tickers"""
        return self.all_tickers
    
    @property
    def List(self) -> list:
        """Alias direct pour compatibilité R"""
        return self.all_tickers
    
    @property
    def ListIndexes(self) -> list:
        """Alias direct pour compatibilité R"""
        return self.list_indexes
    
    @property
    def ListShares(self) -> list:
        """Alias direct pour compatibilité R"""
        return self.list_shares
    
    @property
    def ListBonds(self) -> list:
        """Alias direct pour compatibilité R"""
        return self.list_bonds
    
    @property
    def Indexes(self) -> Optional[pd.DataFrame]:
        """Alias direct pour compatibilité R"""
        return self.indexes
    
    @property
    def Shares(self) -> Optional[pd.DataFrame]:
        """Alias direct pour compatibilité R"""
        return self.shares
    
    @property
    def Bonds(self) -> Optional[pd.DataFrame]:
        """Alias direct pour compatibilité R"""
        return self.bonds
    
    def __repr__(self) -> str:
        return (
            f"Market('{self.market_short_name}' - {self.market_full_name}) "
            f"[{len(self.list_shares)} shares, {len(self.list_indexes)} indexes]"
        )
    
    def __str__(self) -> str:
        return (
            f"\n{'='*60}\n"
            f"Market: {self.market_full_name} ({self.market_short_name})\n"
            f"Country: {self.country} | Currency: {self.currency}\n"
            f"URL: {self.official_url}\n"
            f"Shares: {len(self.list_shares)} | Indexes: {len(self.list_indexes)} | Bonds: {len(self.list_bonds)}\n"
            f"{'='*60}\n"
        )
