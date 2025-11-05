from alpaxa_quant.config import return_EODHD_base_api_endpoint, return_EODHD_test_api_key
from alpaxa_quant.utils import make_safe_request
import pytest

def test_make_safe_request():
    e = return_EODHD_base_api_endpoint()
    k = return_EODHD_test_api_key()

    # Construct test endpoint
    endpoint = f"{e}/MCD.US?api_token={e}&period=d&from=2017-01-05&to=2017-01-10&fmt=json"
    print(endpoint)

if __name__ == "__main__":
    pytest.main()