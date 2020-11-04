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



def remove_outlier(df, column):
    """
    Return a dataframe with outliers removed. The statistical method used is IQR.
    
    Parameter:
    df: Dataframe cotanining the column.
    column: The column containing the outliers.
    
    """
    
    q1, q3 = np.percentile(df[column], [25,75])
    iqr = q3 - q1
    lower_bound = q1 -(1.5 * iqr) 
    upper_bound = q3 +(1.5 * iqr)

    return df.query(f'{column} >= {lower_bound} and {column} <= {upper_bound}')


def classification(row, income_limit, income_min):
    """
    Create a segmentation based on income and total children. 
    This function can be used with lambda.
    
    row: The dataframe containing the data.
    income_limit: The maximum acceptable income for group A.
    income_min: The minimum acceptable income for group B
    
    """
    
    if row['TotalChildren'] == 0 and row['Income'] > income_limit:
        return 'A'
    
    if row['TotalChildren'] == 0 and (row['Income'] < income_limit and row['Income'] > income_min):
        return 'B'
    
    if row['TotalChildren'] > 0 and (row['Income'] > income_min):
        return 'C'
    
    else:
        return 'D'