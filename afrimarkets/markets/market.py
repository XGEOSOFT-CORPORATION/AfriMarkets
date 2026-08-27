from abc import ABC, abstractmethod
from dataclasses import dataclass

from .registry import MarketRegistry


@dataclass
class Market(ABC):
    """
    Base class for all financial markets.
    """

    name: str
    code: str
    country: str
    currency: str
    description: str = ""

    def __init_subclass__(cls, **kwargs):
        """
        Automatically register every concrete market subclass.
        """

        super().__init_subclass__(**kwargs)

        # Do not register abstract intermediate classes.
        if not getattr(cls, "__abstractmethods__", None):
            MarketRegistry.register(cls)

    def __post_init__(self):
        """
        Validate and normalize market information.
        """

        for field_name in (
            "name",
            "code",
            "country",
            "currency",
        ):
            value = getattr(self, field_name)

            if not isinstance(value, str):
                raise TypeError(
                    f"{field_name} must be a string."
                )

            if not value.strip():
                raise ValueError(
                    f"{field_name} must not be empty."
                )

        self.code = self.code.strip().upper()
        self.currency = self.currency.strip().upper()

    # =========================================================
    # TICKERS
    # =========================================================

    @abstractmethod
    def get_tickers(self, *args, **kwargs):
        """
        Return the tickers available on the market.
        """
        raise NotImplementedError

    # =========================================================
    # HISTORICAL DATA
    # =========================================================

    @abstractmethod
    def get_data(
        self,
        tickers=None,
        start=None,
        end=None,
        freq="1d",
        format="dataframe",
    ):
        """
        Return historical data for the requested tickers.
        """
        raise NotImplementedError

    # =========================================================
    # REPRESENTATION
    # =========================================================

    def __str__(self):
        return f"{self.name} ({self.code})"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"code='{self.code}', "
            f"name='{self.name}')"
        )