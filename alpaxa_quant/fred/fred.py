from alpaxa_quant.config import return_FRED_base_api_endpoint, return_FRED_test_api_key
from alpaxa_quant.utils import request_util
import pandas as pd 

# ----------------
# Labour Market
# ----------------
def get_young_unemployment_rate(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "LNS14000024",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_total_unemployed(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "U6RATE",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df



# ----------------

# ----------------
# FEDERAL
# ----------------
def get_all_federal_employees(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "CES9091000001",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_federal_expenditures_interest_payements(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "A091RC1Q027SBEA",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "q",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_federal_liabilities_capital(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "WRBWFRBL",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "w",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_federal_liabilities_capital_weekly_average(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "WRESBAL",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "w",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_quarterly_federal_debt(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "GFDEGDQ188S",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "q",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_annual_federal_funds_effective(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "RIFSPFFNA",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "y",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_weekly_federal_funds_effective(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "FF",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "w",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_daily_federal_funds_effective(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "DFF",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_monthly_federal_funds_effective(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
# Construct params
    params = {
        "series_id":       "FEDFUNDS",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df
# ----------------

# ----------------
# MONETARY
# ----------------
def get_m2_velocity(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "M2V",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "q",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_monetary_base(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BOGMBASE",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_daily_nominal_broad_US_dollar(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "DTWEXBGS",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_monthly_nominal_broad_US_dollar(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "TWEXBGSMTH",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_annual_US_vs_EURO_rate(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "AEXUSEU",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "y",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_monthly_US_vs_EURO_rate(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "EXUSEU",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "m",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_daily_US_vs_EURO_rate(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "DEXUSEU",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df
# ----------------

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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_daily_ICE_BofA_corp(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAMLC0A0CM",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df

def get_daily_ICE_BofA_BBB_corp(api_key: str, base_url: str, start_date: str, end_date: str, verbose: bool = False) -> pd.DataFrame:
    # Construct params
    params = {
        "series_id":       "BAMLC0A4CBBB",
        "api_key":         api_key,
        "file_type":       "json",
        "observation_start": start_date,
        "observation_end":   end_date,
        "frequency":       "d",
    }
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
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
    df = request_util(params=params, base_url=base_url, verbose=verbose)
    return df
# -------------------

if __name__ == "__main__":
    K= return_FRED_test_api_key()
    u= return_FRED_base_api_endpoint()
    get_young_unemployment_rate(K, u,"2020-01-01","2021-01-01", verbose=True)