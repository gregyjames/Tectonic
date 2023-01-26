import numpy as np
import math

from tectonic.Helpers import *

def discounted_NOI(revenue, expenses, required_rate_of_return, growth_rate):
    """Discounted Net Operating Income"""
    return NOI(revenue, expenses) / (required_rate_of_return - growth_rate)

def band_of_investing(i, n_periods, financed_percent, required_rate_of_return, NOI):
    SFF = i / (math.pow(1 + i, n_periods) - 1)
    lender_rate = i + SFF
    weighted_average_rate = ((financed_percent * lender_rate)+((1-financed_percent)*required_rate_of_return))
    return NOI / weighted_average_rate

def price_per_squarefoot(price, area):
    '''Price per Square Foot'''
    return price / area