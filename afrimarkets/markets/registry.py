from typing import Type, Dict


class MarketRegistry:
    """
    Registry containing all available financial markets.
    """

    _markets: Dict[str, Type] = {}

    @classmethod
    def register(cls, market_class: Type) -> None:
        """
        Register a market class.
        """

        code = market_class.code

        if not code:
            raise ValueError(
                f"Market {market_class.__name__} "
                "must define a code."
            )

        code = code.upper()

        if code in cls._markets:
            existing = cls._markets[code]

            if existing is not market_class:
                raise ValueError(
                    f"Market code '{code}' is already registered "
                    f"by {existing.__name__}."
                )

        cls._markets[code] = market_class

    @classmethod
    def get(cls, code: str):
        """
        Return a market instance from its code.
        """

        code = code.strip().upper()

        if code not in cls._markets:
            raise KeyError(
                f"Unknown market: '{code}'. "
                f"Available markets: {cls.codes()}"
            )

        market_class = cls._markets[code]

        return market_class()

    @classmethod
    def get_class(cls, code: str):
        """
        Return the market class itself.
        """

        code = code.strip().upper()

        if code not in cls._markets:
            raise KeyError(
                f"Unknown market: '{code}'."
            )

        return cls._markets[code]

    @classmethod
    def codes(cls) -> list[str]:
        """
        Return all registered market codes.
        """

        return sorted(cls._markets.keys())

    @classmethod
    def markets(cls) -> dict:
        """
        Return all registered markets.
        """

        return cls._markets.copy()

    @classmethod
    def clear(cls) -> None:
        """
        Clear the registry.

        Mainly useful for testing.
        """

        cls._markets.clear()


def get_market(code: str):
    """
    Shortcut for MarketRegistry.get().
    """

    return MarketRegistry.get(code)


def get_market_class(code: str):
    """
    Shortcut for MarketRegistry.get_class().
    """

    return MarketRegistry.get_class(code)


def available_markets() -> list[str]:
    """
    Return all available market codes.
    """

    return MarketRegistry.codes()