from ..african_market import AfricanMarket


class BRVM(AfricanMarket):
    """
    Bourse Régionale des Valeurs Mobilières.
    """

    code = "BRVM"

    def __init__(self):
        super().__init__(
            name="Bourse Régionale des Valeurs Mobilières",
            code=self.code,
            country="WAEMU",
            currency="XOF",
            description=(
                "Regional stock exchange serving "
                "the West African Economic and Monetary Union."
            ),
        )

    def get_tickers(self, *args, **kwargs):
        """
        Return BRVM listed securities.

        This method contains BRVM-specific logic.
        """

        # TODO:
        # API / scraping / local database / etc.

        raise NotImplementedError(
            "BRVM.get_tickers() is not implemented yet."
        )

    def get_data(
        self,
        tickers=None,
        start=None,
        end=None,
        freq="1d",
        format="dataframe",
    ):
        """
        Return historical BRVM data.

        This method contains BRVM-specific logic.
        """

        # TODO:
        # BRVM-specific data provider

        raise NotImplementedError(
            "BRVM.get_data() is not implemented yet."
        )