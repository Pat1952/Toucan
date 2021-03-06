import re
from enum import Enum
from typing import NamedTuple, Optional

import pandas as pd
from typing_extensions import TypedDict


class TimeInterval(Enum):

    ONE_MIN: str = "1min"
    FIVE_MIN: str = "5min"
    FIFTEEN_MIN: str = "15min"
    THIRTY_MIN: str = "30min"
    SIXTY_MIN: str = "60min"


class OutputSize(Enum):

    COMPACT: str = "compact"
    FULL: str = "full"


class QueryParams(TypedDict, total=False):
    apikey: str
    symbol: str
    interval: Optional[str]
    function: str
    outputsize: str
    keywords: str


class AVFunctions(Enum):
    INTRADAY: str = "TIME_SERIES_INTRADAY"
    INTRADAY_EXTENDED: str = "TIME_SERIES_INTRADAY_EXTENDED"
    DAILY: str = "TIME_SERIES_DAILY"
    DAILY_ADJUSTED: str = "TIME_SERIES_DAILY_ADJUSTED"
    WEEKLY: str = "TIME_SERIES_WEEKLY"
    SYMBOl_SEARCH: str = "SYMBOL_SEARCH"
    OVERVIEW: str = "OVERVIEW"
    INCOME_STATEMENT: str = "INCOME_STATEMENT"
    BALANCE_SHEET: str = "BALANCE_SHEET"
    CASH_FLOW: str = "CASH_FLOW"
    EARNINGS: str = "EARNINGS"
    LISTING_STATUS: str = "LISTING_STATUS"


def clean_column_names(column_name: str) -> str:
    """
    clean column names returned from alpha vantage response
    """
    pattern = r"^\d+\.+\s+"
    return re.sub(pattern, "", column_name)


class ReportsResponse(NamedTuple):

    annual_reports: pd.DataFrame
    quarterly_reports: pd.DataFrame
