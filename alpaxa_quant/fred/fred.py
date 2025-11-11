from alpaxa_quant.config import return_FRED_base_api_endpoint, return_FRED_test_api_key
from alpaxa_quant.utils import make_safe_request
import pandas as pd 


# ----------------
# YIELDS
# ----------------

def get_ICE_BofA_H_Y_option_adjusted_spread(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAMLH0A0HYM2",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_ICE_BofA_H_Y_effective_yield(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAMLH0A0HYM2EY",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_ICE_BofA_CCC_L_H_Y_option_adjusted_spread(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAMLH0A3HYC",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_monthly_moodys_seasoned_BAA_corp_yield(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAA",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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

def get_daily_moodys_seasoned_BAA_corp_yield(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "DBAA",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_weekly_moodys_seasoned_BAA_corp_yield(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "WBAA",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "w",
    }
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



# ----------------

# ----------------
# TREASURY YIELDS
# ----------------

# Get US30Y Treasury Yields 
def get_thirty_yield_us(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "DGS30",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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
    

# Get US20Y Treasury Yields 
def get_twenty_yield_us(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "DGS20",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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
    

# Get US10Y Treasury Yields 
def get_ten_yield_us(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "DGS10",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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
    

# Get US05Y Treasury Yields 
def get_five_yield_us(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "DGS5",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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
    

# Get US02Y Treasury Yields 
def get_two_yield_us(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "DGS2",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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
    

def get_daily_ten_year_treasury_constant_maturity(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "T10Y2Y",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_monthly_ten_year_treasury_constant_maturity(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "T10Y2Y",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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

def get_daily_market_yield_US_treasury_ten_year_constant(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "DGS10",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
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

def get_weekly_market_yield_US_treasury_ten_year_constant(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "WGS10YR",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "w",
    }
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

def get_monthly_market_yield_US_treasury_ten_year_constant(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    params = {
        "series_id":       "GS10",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
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


# -------------------

if __name__ == "__main__":
    K= return_FRED_test_api_key()
    u= return_FRED_base_api_endpoint()
    get_monthly_moodys_seasoned_BAA_corp_yield(K, u,"2020-01-01","2021-01-01", verbose=True)