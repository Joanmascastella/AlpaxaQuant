from typing import Dict, Any
import pandas as pd
import requests

def request_util(params: Dict, base_url:str, verbose: bool) -> pd.DataFrame():
    start_date = params['observation_start']

    if verbose:
        print(f"Making request with params: \nSeries ID: {params['series_id']}\nFile Type: {params['file_type']}\nObservation Start Date: {params['observation_start']}\nObservation End Date: {params['observation_end']}\nFrequency: {params['frequency']}\n")

    data = make_safe_request(endpoint=base_url, params=params, verbose=verbose)

    if data is None or data.empty:
        print("No data returned from FRED.")
        return pd.DataFrame()

    if "observations" not in data.columns:
        print("No observations field in response.")
        return pd.DataFrame()

    observations = data.loc[0, "observations"]

    if not isinstance(observations, list) or len(observations) == 0:
        print("No observations data available.")
        return pd.DataFrame()

    df = pd.DataFrame(observations)[["date", "value"]]
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df = df[df["date"] >= pd.to_datetime(start_date)]
    df = df.set_index("date").rename(columns={"value": "close"}).sort_index()

    if verbose:
        print(df.head())
    
    return df


def _normalize_to_df(payload: Any) -> pd.DataFrame | None:
    """
    Convert common JSON shapes from EODHD into a pandas DataFrame.
    Handles:
      - list[dict]                       -> DataFrame(list)
      - dict[key -> dict]               -> DataFrame(list(dict.values()))
      - dict of scalars                 -> DataFrame([dict])
      - mixed / nested                  -> pd.json_normalize(dict)
    """
    if payload is None:
        return None

    if isinstance(payload, list):
        return pd.DataFrame(payload)

    # Dict payload
    if isinstance(payload, dict):
        vals = list(payload.values())
        if len(payload) == 0:
            return pd.DataFrame()

        if all(isinstance(v, dict) for v in vals):
            return pd.DataFrame.from_records(vals)

        if any(isinstance(v, (dict, list)) for v in vals):
            return pd.json_normalize(payload, sep=".")

        return pd.DataFrame([payload])

    return pd.DataFrame([{"value": payload}])

def make_safe_request(   
    endpoint: str,
    timeout: int = 30,
    params: [Dict[str, Any]] = None,
    json: [Dict[str, Any]] = None,
    auth: bool = False,
    jwt_key: str = "",
    verbose: bool = False) -> pd.DataFrame | None:
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

        headers = {"Accept": "application/json"}
        if auth:
            if jwt_key == "":
                raise ValueError("JWT was not provided.")
            headers["Authorization"] = f"Bearer {jwt_key}"

        if json:
            response = requests.post(endpoint, headers=headers, json=json, timeout=timeout)
            response.raise_for_status()
        else:
            response = requests.get(endpoint, headers=headers, params=params, timeout=timeout)
            response.raise_for_status()
            
        if verbose:
            print(f"Made request. Got status {response.status_code}")

        # Parse JSON
        data = response.json()
        # Convert to DataFrame
        df = _normalize_to_df(data)
        
        if verbose:
            print(f"Data retrieved {df.head(5)}")

        return df 

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        return None
