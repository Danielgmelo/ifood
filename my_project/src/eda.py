import pandas as pd


def OnePurchaseEveryNMonths(row):
    """
    Calculates the number of months for each purchase.
    
    Parameters:
    row: Average purchase per customer over the past two years.
    
    """
    
    return round(12 / ((row / 24) * 12), 2)