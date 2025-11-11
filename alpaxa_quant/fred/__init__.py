from .fred import (
    get_monthly_market_yield_US_treasury_ten_year_constant,
    get_weekly_market_yield_US_treasury_ten_year_constant,
    get_daily_market_yield_US_treasury_ten_year_constant,
    get_monthly_ten_year_treasury_constant_maturity,
    get_ICE_BofA_CCC_L_H_Y_option_adjusted_spread,
    get_daily_ten_year_treasury_constant_maturity,
    get_monthly_moodys_seasoned_BAA_corp_yield,
    get_weekly_moodys_seasoned_BAA_corp_yield,
    get_daily_moodys_seasoned_BAA_corp_yield,
    get_ICE_BofA_H_Y_option_adjusted_spread,
    get_monthly_nominal_broad_US_dollar,
    get_daily_nominal_broad_US_dollar,
    get_ICE_BofA_H_Y_effective_yield,
    get_monthly_US_vs_EURO_rate,
    get_daily_ICE_BofA_BBB_corp,
    get_annual_US_vs_EURO_rate,
    get_daily_US_vs_EURO_rate,
    get_daily_ICE_BofA_corp,
    get_thirty_yield_us,
    get_twenty_yield_us,
    get_five_yield_us,   
    get_monetary_base,
    get_ten_yield_us,
    get_two_yield_us,
    get_all_federal_employees,
    get_annual_federal_funds_effective,
    get_daily_federal_funds_effective,
    get_federal_expenditures_interest_payements,
    get_federal_liabilities_capital,
    get_federal_liabilities_capital_weekly_average,
    get_m2_velocity,
    get_monthly_federal_funds_effective,
    get_quarterly_federal_debt,
    get_weekly_federal_funds_effective,



)

__all__ = [
    'get_daily_ten_year_treasury_constant_maturity',
    'get_five_yield_us',
    'get_ten_yield_us',
    'get_thirty_yield_us',
    'get_twenty_yield_us',
    'get_two_yield_us'
   
]

def __version__():
    """Return the version of the Alpaxa Quant Package."""
    return "0.0.1"

def describe():
    """Print a description of the package and its features."""
    description = (
        "AlpaxaQuant Library\n"
        "Version: {}\n"
        "Provides all you need to code your own quant model"
    ).format(__version__())
    print(description)