from alpaxa_quant.config import return_EODHD_base_api_endpoint, return_EODHD_test_api_key
from alpaxa_quant.eodhd import get_historical_ticker_price
import pandas as pd
import pytest

def test_make_safe_request():
    e = return_EODHD_base_api_endpoint()
    k = return_EODHD_test_api_key()

    df = get_historical_ticker_price(
        base_endpoint=e, 
        api_token=k, 
        ticker='TSLA', 
        fmt='json', 
        period='d',
        order='a',
        from_date='2017-05-01',
        to_date='2017-05-25',
        timeout=10,
        verbose=True)
    
    assert df is not None, "Expected non-empty DataFrame"
    assert isinstance(df, pd.DataFrame), "Response should be a pandas DataFrame"
    assert not df.empty, "Expected data in DataFrame"

    # Validate key columns exist
    for col in ["date", "open", "high", "low", "close", "adjusted_close", "volume"]:
        assert col in df.columns, f"Missing column: {col}"

    # Check if the date returned follows the date range
    assert "2017-05-01" in df["date"].values, "Expected start date missing"
    assert "2017-05-25" in df["date"].values, "Expected end date missing"

if __name__ == "__main__":
    pytest.main([__file__])