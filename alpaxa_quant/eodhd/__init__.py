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
    get_technicals,
    fetch_news_sentiment,
    )

__all__ = [
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
    'fetch_news_sentiment'
]

__version__ = "1.0"

def describe():
    """Print a description of the package and its features."""
    description = (
        "AlpaxaQuant Library\n"
        "Version: {}\n"
        "Provides all you need to code your own quant model"
    ).format(__version__())
    print(description)