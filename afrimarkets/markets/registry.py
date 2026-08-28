from typing import Dict, Type
from inspect import isabstract
from tabulate import tabulate


class MarketRegistry:
    """
    Registry containing all available financial markets.
    """

    _markets: Dict[str, Type] = {}

    @classmethod
    def register(cls, market_class):
        """
        Register a concrete market class.
        """

        if isabstract(market_class):
            return

        code = getattr(market_class, "code", None)

        if not code:
            return

        code = code.strip().upper()

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
                f"Unknown market: '{code}'. "
                f"Available markets: {cls.codes()}"
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
    def show(cls):

        rows = []

        for code, market_class in cls._markets.items():

            market = market_class()

            rows.append([
                code,
                market.name,
                market.country,
                market.currency,
                market.description
            ])

        rows.sort(key=lambda x: x[0])

        print(
            tabulate(
                rows,
                headers=[
                    "Code",
                    "Name",
                    "Country",
                    "Currency",
                    "Description"
                ],
                tablefmt="rounded_outline"
            )
        )

        return rows

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

