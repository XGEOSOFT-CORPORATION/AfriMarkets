import datetime
from http import cookies

from ..african_market import AfricanMarket
from ...local_tools.common import period2interval, datefr2dateiso, datalist2structure

import requests
from bs4 import BeautifulSoup
import pandas as pd


class BRVM(AfricanMarket):
    """
    Bourse Régionale des Valeurs Mobilières.
    """

    code = "BRVM"

    def __init__(self):
        super().__init__(
            name="Bourse Régionale des Valeurs Mobilières",
            code=self.code,
            country="Ivory Coast",
            currency="XOF",
            description=(
                "Regional stock exchange serving "
                "the West African Economic and Monetary Union."
            ),
        )

        # Launch the process of retrieving tickers and categorizing them
        self.get_tickers()


    def get_tickers(self, *args, **kwargs):
        """
        Return BRVM listed securities.
        No parameters are required for this method.
        """
        # tick_data = assets
        tick_data = self.__get_tickers__()

        self.indexes = [asset["Symbol"] for asset in tick_data if asset["Type"] == "Index"]
        self.shares = [asset["Symbol"] for asset in tick_data if asset["Type"] == "Share"]
        self.bonds = [asset["Symbol"] for asset in tick_data if asset["Type"] == "Bond"]
        self.tickers = [asset["Symbol"] for asset in tick_data]

        self.index_table = [asset for asset in tick_data if asset["Type"] == "Index"]
        self.share_table = [asset for asset in tick_data if asset["Type"] == "Share"]
        self.bond_table = [asset for asset in tick_data if asset["Type"] == "Bond"]
        self.ticker_table = tick_data

        return self



    def get_data(
        self,
        tickers: list,
        start: str,
        end: str,
        freq: list = ["daily", "weekly", "monthly", "quarterly", "yearly"],
        structure: str="column",
        format: str="dataframe",
    ):
        """
        Return historical BRVM data.

        Parameters:
            tickers (list): List of tickers to retrieve data for.
            start (str): Start date in 'YYYY-MM-DD' format.
            end (str): End date in 'YYYY-MM-DD' format.
            freq (list): Frequency of data. Options: "daily", "weekly", "monthly", "quarterly", "yearly".
            structure (str): Structure of the returned data. Options: "row" or "column".
            format (str): Format of the returned data. Options: "dataframe" or "list".
        Returns:
            pd.DataFrame or list: Historical data in the specified format and structure.
        """

        dfreq = {
            "daily": "0",
            "weekly": "7",
            "monthly": "30",
            "quarterly": "91",
            "yearly": "365"
        }

        data_list = self.__get_data__(tickers, start=start, end=end, freq=dfreq[freq[0]])

        if structure in ["row", "column"]:
            data_list = datalist2structure(data_list, structure=structure, date_field="Date")
        else:
            raise ValueError(
                f"Invalid structure '{structure}'. Must be 'row' or 'column'."
            )

        if format == "dataframe":
            return pd.DataFrame(data_list)
        elif format == "list":
            return data_list
        else:
            raise ValueError(
                f"Invalid format '{format[0]}'. Must be 'dataframe' or 'list'."
            )
        

    def __get_tickers__(self):

        """
        Return BRVM listed securities.
        This method contains BRVM-specific logic.
        """

        url = "https://www.sikafinance.com"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url,headers=headers,timeout=30)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")
            select = soup.find("select", id="dpShares")

            assets = []
            for option in select.find_all("option"):

                code = option.get("value")
                if code:
                    assets.append({
                        "Type"  : "Share" if "." in code else "Index",
                        "Symbol": code.split(".")[0],
                        "Ticker": code,
                        "Country": code.split(".")[1] if "." in code else "",
                        "Name": option.get_text(" ", strip=True)
                    })

            # assets_sorted = sorted(assets, key=lambda x: x["Symbol"].upper())
            assets.sort(key=lambda x: x["Symbol"].upper())
            # df = pd.DataFrame(assets)
        return assets


    def __get_data__(self, symbols: list, start = '2026-01-01', end = '2026-08-31', freq = '0'):
        """
        Return historical BRVM data.
        This method contains BRVM-specific logic.
        """

        # symbols = ["BOaB","bicc","abjc"]

        data_list = []
        
        for symb in symbols:
            # symb = symbols[0]

            symb = symb.upper()

            if symb in [asset["Symbol"] for asset in self.ticker_table]:
                tick = next(row["Ticker"] for row in self.ticker_table if row["Symbol"] == symb)
            else:
                print(f"Ticker '{symb}' not found in BRVM tickers.")
                continue

            # process

            if tick:
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.9,en-US;q=0.8,en;q=0.7',
                    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Origin': 'https://www.sikafinance.com',
                    'Connection': 'keep-alive',
                    'Referer': f'https://www.sikafinance.com/marches/historiques/{tick}',
                    # 'Cookie': 'editionSika=BJ; _ga_721Z734TN6=GS2.1.s1787866580$o2$g1$t1787866828$j49$l0$h0; _ga=GA1.1.82534532.1787833023; __gads=ID=e758c2a4c83f0446:T=1787833026:RT=1787866591:S=ALNI_MaoBqxii34PJEDuFohKW0YZBbz6uA; __gpi=UID=000015287a912142:T=1787833026:RT=1787866591:S=ALNI_MYwOqHrDlh_jeao2dI-JTah0S0B6A; __eoi=ID=b4f43210e9663567:T=1787833026:RT=1787866591:S=AA-AfjacxeMiDyaoA4M-WeNFjOvD',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Priority': 'u=0',
                }

                intervals = period2interval(start_date=start, end_date=end, by=85)

                data_interval = []
                for interval in intervals:

                    d1, d2 = interval
                    json_data = {
                        'ticker': tick,
                        'datedeb': d1,
                        'datefin': d2,
                        'xperiod': freq,
                    }

                    response = requests.post('https://www.sikafinance.com/api/general/GetHistos', headers=headers, json=json_data)

                    if response.status_code != 200:
                        # print(f"Failed to retrieve data for {symb} from {d1} to {d2}. Status code: {response.status_code}")
                        continue

                    data = response.json()
                    if "lst" in data.keys():
                        data_interval.extend([{"Symbol": symb, **row} for row in data["lst"]])

                if len(data_interval) > 0:
                    data_interval = datefr2dateiso(data_interval, date_field="Date")
                    print(f"Data for {symb} retrieved successfully from {min([row['Date'] for row in data_interval])} to {max([row['Date'] for row in data_interval])}.")
                    data_list.extend(data_interval)
                else:
                    print(f"No data found for {symb} in the specified date range.")
                    continue

                data_list = list({tuple(row.items()): row for row in data_list}.values())  # Remove duplicates
                data_list = sorted(data_list, key=lambda x: (x["Symbol"], x["Date"]))

        return data_list
                
