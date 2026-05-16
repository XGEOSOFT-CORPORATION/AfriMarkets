"""
Tests for the market registry and dispatcher system
"""
import pytest
from afrimarkets.core.registry import MarketRegistry, MARKET_CONFIGS
from afrimarkets.core.market import Market
from afrimarkets.core.dispatcher import MarketDispatcher


class TestMarketRegistry:
    """Tests pour MarketRegistry"""
    
    def test_markets_are_registered(self):
        """Vérifie que tous les marchés sont enregistrés"""
        markets = MarketRegistry.list_markets()
        assert len(markets) >= 7
        assert "BRVM" in markets
        assert "NGX" in markets
    
    def test_get_adapter(self):
        """Vérifie qu'on peut récupérer un adaptateur"""
        adapter = MarketRegistry.get_adapter("BRVM")
        assert adapter is not None
        assert adapter.market.market_short_name == "BRVM"
    
    def test_invalid_market_raises_error(self):
        """Vérifie qu'un marché invalide lève une erreur"""
        with pytest.raises(ValueError):
            MarketRegistry.get_adapter("INVALID")
    
    def test_is_registered(self):
        """Vérifie la vérification d'enregistrement"""
        assert MarketRegistry.is_registered("BRVM")
        assert not MarketRegistry.is_registered("INVALID")


class TestMarketDispatcher:
    """Tests pour MarketDispatcher"""
    
    def test_get_tickers_single_market(self):
        """Vérifie qu'on peut récupérer les tickers d'un marché"""
        market = MarketDispatcher.get_tickers("BRVM")
        assert isinstance(market, Market)
        assert market.market_short_name == "BRVM"
    
    def test_get_tickers_all_markets(self):
        """Vérifie qu'on peut récupérer tous les marchés"""
        markets = MarketDispatcher.get_tickers("ALL")
        assert isinstance(markets, dict)
        assert len(markets) >= 7
        assert "BRVM" in markets
        assert isinstance(markets["BRVM"], Market)
    
    def test_get_data_single_ticker(self):
        """Vérifie qu'on peut récupérer les données"""
        import pandas as pd
        df = MarketDispatcher.get_data("BRVM", ticker="SNTS", period="daily")
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert "Date" in df.columns
        assert "Close" in df.columns


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
