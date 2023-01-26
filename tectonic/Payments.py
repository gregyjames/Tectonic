import math

def Mortgage(years, principal, annual_rate):
    """Monthly payment for a mortgage"""
    monthly_rate = annual_rate / 12
    n_periods = years * 12
    return principal * ((monthly_rate * math.pow(1+monthly_rate, n_periods)) / (math.pow(1+monthly_rate, n_periods) - 1))
