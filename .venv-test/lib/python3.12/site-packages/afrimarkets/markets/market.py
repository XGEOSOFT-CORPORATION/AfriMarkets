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
    indexes : list = None
    shares: list = None
    bonds: list = None
    tickers: list = None

    index_table: list = None
    share_table: list = None
    bond_table: list = None
    ticker_table: list = None

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
            f"{self.__class__.__name__}(\n"
            f"  Code='{self.code}',\n"
            f"  Name='{self.name}',\n"
            f"  Country='{self.country}',\n"
            f"  Currency='{self.currency}',\n"
            f"  Description='{self.description}',\n"
            f"\n"
            f"  * Index (N={len(self.indexes) if self.indexes else 0}):\n"
            f"    {self.indexes if self.indexes else []}\n"
            f"\n"
            f"  * Shares (N={len(self.shares) if self.shares else 0}):\n"
            f"    {self.shares if self.shares else []}\n"
            f"\n"
            f"  * Bonds (N={len(self.bonds) if self.bonds else 0}):\n"
            f"    {self.bonds if self.bonds else []}\n"
            f"{'-' * 40}"
        )