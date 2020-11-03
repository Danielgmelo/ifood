import pandas as pd
import numpy as np


def optimal_probability(df:pd.DataFrame):
    """
    Returns what would be the revenue, cost and success rate for each probability (limit_prob) value between 0 and 100.
    
    Parameters:
    df: Dataframe containig the coluns of model
    """

    columns = list(['limit_prob','result_pred', 'response', 'revenue_previst', 'cost_previst', 'profit_previst', 'tx_sucess'])
    data = []

    for i in np.arange(0,100):

        df['result_p'] = df['prob_true'].apply(lambda x: True if x >= i/100 else False)

        result_p = df.query("result_p == 1")[['result_p','Response']].sum()[0]
        response = df.query("result_p == 1")[['result_p','Response']].sum()[1]
        
        revenue =  response * 11
        cost = result_p * 3
        profit = revenue - cost
        tx_sucess = round(response / result_p, 1) if result_p > 0 else 0

        values = [i, result_p, response, revenue, cost, profit, tx_sucess]
        zipped = zip(columns, values)
        a_dictionary = dict(zipped)
        data.append(a_dictionary)

    df.drop('result_p', axis=1, inplace=True)
    results = pd.DataFrame(data).sort_values('profit_previst', ascending=False)
    
    return results[['limit_prob','result_pred', 'response', 'revenue_previst', 'cost_previst', 'profit_previst', 'tx_sucess']]


def purchase_every_N_days(df, column):
    """
    Return the number of days for each purchase.
    
    Parameters:
    df:The dataframe containing the data.
    column: The that will be used.
    
    """

    return (df['DaysOfRegistration']/ df[column]).replace([np.inf, -np.inf], 0)