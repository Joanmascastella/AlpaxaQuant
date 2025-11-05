from alpaxa_quant.config import return_EODHD_base_api_endpoint, return_EODHD_test_api_key
from dotenv import load_dotenv
import pytest
import os

load_dotenv(".env")

def test_dotenv_variables():
    assert return_EODHD_base_api_endpoint() == os.getenv("TEST_EODHD_BASE_ENDPOINT")
    assert return_EODHD_test_api_key()      == os.getenv("TEST_EODHD_API_KEY")

if __name__ == "__main__":
    pytest.main()
