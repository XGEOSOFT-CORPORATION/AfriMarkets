"""
Tests pour les adaptateurs BRVM
"""
import pytest
from afrimarkets import get_tickers, get_data
import pandas as pd


class TestBRVMMarket:
    """Tests pour le marché BRVM"""
    
    def test_get_brvm_tickers(self):
        """Vérifie qu'on peut récupérer les tickers BRVM"""
        market = get_tickers("BRVM")
        assert market is not None
        assert market.market_short_name == "BRVM"
        assert len(market.list_shares) > 0
        assert len(market.list_indexes) > 0
    
    def test_get_brvm_data_single_ticker(self):
        """Vérifie qu'on peut récupérer les données"""
        df = get_data("BRVM", ticker="SNTS")
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert "Date" in df.columns
        assert "Ticker" in df.columns
    
    def test_get_brvm_data_all_shares(self):
        """Vérifie qu'on peut récupérer toutes les actions"""
        df = get_data("BRVM", ticker="ALL SHARES")
        assert not df.empty
        assert df["Ticker"].nunique() > 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
