from .insider_trades import insider_trades
from .eodhd import eodhd
from .finra import finra
from .utils import utils
from .fred import fred

__all__ = [
    # utils
    'utils',

    # eodhd
    'eodhd',

    # insider_trades
    'insider_trades',

    # finra
    'finra',

    # fred
    'fred'
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