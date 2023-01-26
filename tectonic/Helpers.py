def NOI(revenue, expenses):
    """Net Operating Income"""
    return revenue - expenses

def cap_rate(revenue, expenses, property_value):
    """
    Capitalization Rate
    
    The cap rate formula compares an investment property’s net operating income with its market value
    """
    return NOI(revenue, expenses) / property_value

def price_to_rent_ratio(property_value, gross_rent):
    """
    Price to Rent Ratio
    
    This figure shows you how much rent you’ll be receiving, versus the price at which your property was purchased.
    """
    return property_value / gross_rent

def cash_on_return(revenue, expenses, property_value):
    """Cash on Return"""
    return NOI(revenue, expenses) / property_value

def GRM(property_value, gross_rent):
    """
    Gross Rent Multiplier
    GRM is a screening metric used by investors to compare rental property opportunities in a given market. Range 4-7 is considered a good value.
    """
    return property_value / gross_rent