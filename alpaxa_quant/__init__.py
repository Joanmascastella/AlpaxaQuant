from .insider_trades import insider_trades
from .eodhd import eodhd
from .finra import finra
from .utils import utils
from .fred import fred

__all__ = [
    'utils',
    'eodhd',
    'insider_trades',
    'finra',
    'fred',
]

# Package version
__version__ = "1.0"


def describe():
    """
    Print a detailed description of the AlpaxaQuant package and its modules.
    """

    description = f"""
AlpaxaQuant Library
Version: {__version__}

Overview:
    AlpaxaQuant is an end-to-end quantitative finance library designed for
    developers and researchers building custom trading, data analytics,
    and econometric models. It provides high-level access to financial,
    fundamental, insider, and macroeconomic data — all through clean,
    modular APIs.

Modules:
    • utils:
        Contains general helper functions and abstractions for making safe,
        authenticated API requests, handling timeouts, retries, and data
        formatting. It is the backbone of all data retrieval functions in
        the package.

    • eodhd:
        Integrates directly with the EODHD API to fetch a complete range of
        financial and market data for any ticker symbol — including prices,
        earnings, balance sheets, technicals, analyst ratings, sentiment,
        and much more.

    • insider_trades:
        Retrieves insider transaction data for all U.S.-listed companies.
        Offers extensive filtering capabilities (by date, transaction type,
        position, minimum value, etc.) to support alpha generation and
        compliance analysis.

    • finra:
        Provides access to FINRA’s extensive repository of U.S. market
        structure and fundamental data — including short interest,
        block trades, corporate/agency debt markets, OTC summaries,
        and trade volume analytics.

    • fred:
        Fetches all economic, macroeconomic, and commodity indicators
        available via the Federal Reserve (FRED) API, including inflation,
        yields, GDP, employment, and global commodity indexes.

"""

    print(description.strip())
