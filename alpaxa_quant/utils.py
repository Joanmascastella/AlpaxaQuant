from typing import Dict, Any
import pandas as pd
import requests

def make_safe_request(endpoint: str, timeout: int, params: Dict[str,Any] ,verbose: bool) -> pd.DataFrame:
    """
        Performs a HTTP GET request to a given endpoint and returns the
        response content as a pandas DataFrame.

        Args:
            endpoint (str): The full URL to send the GET request to.
            timeout (int): The maximum number of seconds to wait for a response.
            params (dict): The dictionary containing all the necessery date to make a request.
            debug (bool): If True, prints debug information during the request
                (e.g., URL, status code, and DataFrame preview).

        Returns:
            pd.DataFrame | None: A pandas DataFrame containing the JSON response
            data if the request succeeds and can be parsed. Returns None if the
            request fails, times out, or the response is not valid JSON.

        Raises:
            requests.exceptions.RequestException: For network-related errors.
            ValueError: If JSON decoding fails or the response cannot be converted
            into a DataFrame.

        Example:
            >>> df = make_safe_request("https://api.example.com/data", timeout=10, debug=True)
            >>> if df is not None:
            ...     print(df.head())
        """
    try:
        if verbose:
            print(f"Making request to {endpoint} with timeout {timeout}")

        # Check what http method will be used to make the request
        response = requests.get(endpoint, params=params, timeout=timeout)
        response.raise_for_status()
        
        if verbose:
            print(f"Made request. Got status {response.status_code}")

        # Parse JSON
        data = response.json()
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        if verbose:
            print(f"Data retrieved {df.head(5)}")

        return df 

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        return None
