from dataclasses import dataclass, field
from typing import Any


@dataclass
class Ticker:
    """Base class for a financial instrument."""

    symbol: str
    name: str
    data: Any = field(default_factory=dict)

    def info(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(symbol={self.symbol}, name={self.name})"
        )

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return self.info()