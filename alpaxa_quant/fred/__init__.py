from .fred import (
    get_daily_ten_year_treasury_constant_maturity,
    get_five_yield_us,
    get_ten_yield_us,
    get_thirty_yield_us,
    get_twenty_yield_us,
    get_two_yield_us
)

__all__ = [
    'get_daily_ten_year_treasury_constant_maturity',
    'get_five_yield_us',
    'get_ten_yield_us',
    'get_thirty_yield_us',
    'get_twenty_yield_us',
    'get_two_yield_us'
   
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