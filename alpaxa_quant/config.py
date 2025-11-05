from dotenv import load_dotenv
import os

load_dotenv(".env")

def return_EODHD_test_api_key() -> str:
    return os.getenv("TEST_EODHD_API_KEY")

def return_EODHD_base_api_endpoint() -> str:
    return os.getenv("TEST_EODHD_BASE_ENDPOINT")