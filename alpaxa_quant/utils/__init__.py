from .utils import make_safe_request
from .eodhd import (
    get_analyst_ratings, 
    get_ticker_valuation, 
    get_ticker_highlights, 
    get_earnings, get_financials, 
    get_general_ticker_info, 
    get_historical_ticker_price, 
    get_holders,
    get_insider_transactions,
    get_outstanding_shares,
    get_shares_stats,
    get_split_dividends,
    get_technicals
    )
from insider_trades import get_insider_trades
from finra import (
    get_agency_debt_market_breadth,
    get_agency_debt_market_sentiment,
    get_bearer_token,
    get_blocks_summary,
    get_consolidated_short_interest,
    get_corporate_and_agency_capped_volume,
    get_corporate_debt_market_breadth,
    get_corporate_debt_market_sentiment,
    get_daily_short_volume_sale,
    get_monthly_summary,
    get_otc_block_summary,
    get_securitized_product_capped_volume,
    get_treasury_daily_aggregates,
    get_treasury_monthly_aggregates,
    get_weekly_summary
)

__all__ = [
    # utils
    'make_safe_request',

    # eodhd
    'get_analyst_ratings',
    'get_ticker_valuation',
    'get_ticker_highlights',
    'get_earnings',
    'get_financials',
    'get_general_ticker_info',
    'get_historical_ticker_price',
    'get_holders',
    'get_insider_transactions',
    'get_outstanding_shares',
    'get_shares_stats',
    'get_split_dividends',
    'get_technicals',

    # insider_trades
    'get_insider_trades',

    # finra
    'get_agency_debt_market_breadth',
    'get_agency_debt_market_sentiment',
    'get_bearer_token',
    'get_blocks_summary',
    'get_consolidated_short_interest',
    'get_corporate_and_agency_capped_volume',
    'get_corporate_debt_market_breadth',
    'get_corporate_debt_market_sentiment',
    'get_daily_short_volume_sale',
    'get_monthly_summary',
    'get_otc_block_summary',
    'get_securitized_product_capped_volume',
    'get_treasury_daily_aggregates',
    'get_treasury_monthly_aggregates',
    'get_weekly_summary',
]

def __version__():
    """Return the version of the Alpaxa Quant Package."""
    return "0.0.1"

def describe():
    """Print a description of the package and its features."""
    description = (
        "AlpaxaQuant Library\n"
        "Version: {}\n"
        "Provides all you need to code your own quant model"
    ).format(__version__())
    print(description)