from alpaxa_quant.utils import make_safe_request
import pandas as pd

def get_historical_ticker_price(
            base_endpoint: str,
            api_token: str,
            ticker: str,
            fmt: str = 'json',
            period: str = 'd',
            order: str = 'a',
            from_date: str = None,
            to_date: str = None,
            timeout: int = 10,
            verbose: bool = True
        ) -> pd.DataFrame:
        """
        Fetch historical EODHD price data for a given ticker symbol.

        Uses make_safe_request() internally for API calls.

        Args:
            base_endpoint: Base EODHD endpoint (e.g., https://eodhd.com/api/eod)
            api_token: EODHD API key
            ticker: Stock ticker symbol (e.g., 'AAPL')
            fmt: Response format (default: 'json')
            period: Data frequency ('d' daily, 'w' weekly, 'm' monthly)
            order: Sorting order ('a' ascending, 'd' descending)
            from_date: Start date (optional)
            to_date: End date (optional)
            timeout: Max request timeout (seconds)
            verbose: Print request configuration and logs if True

        Returns:
            A pandas DataFrame with historical price data or None on failure.
        """
    
        # Construct query paramteres 
        params = {
            "api_token": api_token,
            "period": period,
            "order": order,
            "fmt": fmt,
        }

        # Add date params only if provided
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        
        # Set up endpoint 
        constructed_endpoint=f"{base_endpoint}/{ticker.upper()}.US"

        # Verbose print statement
        if verbose:
            print(f"""
                    Processing ticker: {ticker}

                    Request configuration:
                    Period: {period}
                    From: {from_date or 'Not Provided.'}
                    To: {to_date or 'Not Provided.'}

                    Return configuration:
                    Order: {order}
                    Format: {fmt}
                    URL: {constructed_endpoint}
                """)
        
        # Make request
        df = make_safe_request(endpoint=constructed_endpoint, timeout=timeout, params=params, verbose=verbose)

        # Check if df is not empty
        if df is None or df.empty:
            print(f"No data returned for {ticker}")
            return None

        return df
