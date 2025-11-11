from .utils import make_safe_request, request_util, make_yf_request

__all__ = [
    # utils
    'make_safe_request',
    'request_util',
    'make_yf_request'
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