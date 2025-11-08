from insider_trades import get_insider_trades

__all__ = [
    # insider_trades
    'get_insider_trades',
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