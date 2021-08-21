"""Start running Innanzi"""

from __future__ import annotations

from datetime import datetime
from logging import INFO as INFO_LOG_LEVEL

import pandas as pd
import toml

from innanzi.util.logging import get_logger

RUN_LOG = get_logger(__name__, fmt="%(message)s")
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def get_weight(
    d_frame: pd.DataFrame,
    total_pct: float,
    country: str,
) -> float:
    """Get the weight of a country in a dataset

    :param d_frame: Dataset
    :param total_pct: Total weighted percent of all countries
    :param country: Desired country
    :return: Weight of country
    """
    weight = float(d_frame[d_frame["COUNTRY"] == country]["WEIGHT"].apply(float).sum())
    RUN_LOG.info("%s: %s", f"{country.title(): >13}", f"{weight / total_pct:.3%}")
    return weight


def main() -> None:
    """Main function"""
    with open("etf.toml", encoding="utf-8", errors="surrogateescape") as f:
        etf_data = toml.load(f)

    RUN_LOG.info("Retrieving from: %s", etf_data["NYSEARCA_AVDV"]["holdings"])
    # Read data
    etf = pd.read_csv(
        etf_data["NYSEARCA_AVDV"]["holdings"],
        error_bad_lines=False,
        names=[
            "COMPANY",
            "TICKER",
            "CUSIP",
            "ISIN",
            "SEDOL",
            "SHARES/PRINCIPAL/NOTIONAL AMOUNT",
            "CONTRACT COUNT",
            "MARKET VALUE ($)",
            "WEIGHT",
            "SECTOR",
            "COUNTRY",
        ],
        sep=",",
    )

    # Retrieve date from CSV file
    data_date = etf[  # pylint: disable=unsubscriptable-object
        etf["COMPANY"] == "As of"  # pylint: disable=unsubscriptable-object
    ]["TICKER"].iloc[0]
    data_date = datetime.strptime(data_date, "%m/%d/%Y").strftime("%Y-%m-%d %a")
    RUN_LOG.info("%s: %s", f'{"Date": >13}', data_date)

    # Calculate the total weight of all countries
    etf_sub = etf[["WEIGHT", "COUNTRY"]][  # pylint: disable=unsubscriptable-object
        7:
    ].copy()
    etf_sub["WEIGHT"] = etf_sub["WEIGHT"].map(lambda x: float(x.removesuffix("%")))
    total_pct = float(etf_sub["WEIGHT"].sum())

    # Weight of specific countries
    country_1 = "CANADA"
    country_2 = "UNITED STATES"
    country_1_weight = get_weight(etf_sub, total_pct, country_1)
    country_2_weight = get_weight(etf_sub, total_pct, country_2)

    # Weight of the rest of the world, excluding specific countries above
    remaining = total_pct - country_1_weight - country_2_weight
    RUN_LOG.info("%s: %s", f'{"Rest of World": >13}', f"{remaining / total_pct:.3%}")
