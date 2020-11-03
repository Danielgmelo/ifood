import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns


def qty_and_percentage(df, column_name, rotation=45):
    """
    Shows two graphs containing the absolute value and the percentage of the total value.
    
    Parameters:
    df: Dataframe containing the data.
    column_name: Column containing the data to be plotted.
    rotation: The rotation of x_label.
    
    """
    
    data = (df[column_name]
        .groupby(df[column_name], sort=False)
        .count()
        .sort_values(ascending=False)
       )
    percentage = (data / data.sum()).sort_values(ascending=False).multiply(100).round(0)

    fig,(ax, ax1) = plt.subplots(1,2, figsize=(8,2.5)) 
    fig.subplots_adjust(wspace=0.5)
    
    data.plot.bar(ax=ax)
    ax.set_title(f'{column_name} - Qty of customers')
    ax.tick_params(axis='x', labelrotation=rotation)
    ax.set_ylabel('Qty')

    percentage.plot.bar(ax=ax1)
    ax1.set_title(f'{column_name} - Percentage of total')
    ax1.tick_params(axis='x', labelrotation=rotation)
    ax1.set_ylabel('%')
    