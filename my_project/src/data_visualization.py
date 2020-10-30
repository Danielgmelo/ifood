import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns


def qty_and_percentage(df, column_name, rotation=45):
    
    data = (df[column_name]
        .groupby(df[column_name], sort=False)
        .count()
        .sort_values(ascending=False)
       )
    percentage = (data / data.sum()).sort_values(ascending=False).multiply(100).round(0)

    fig,(ax, ax1) = plt.subplots(1,2, figsize=(8,2.5)) 
    fig.subplots_adjust(wspace=0.5)
    
    data.plot.bar(ax=ax)
    ax.set_title(f'{column_name} - Qty of customer')
    ax.tick_params(axis='x', labelrotation=rotation)

    percentage.plot.bar(ax=ax1)
    ax1.set_title(f'{column_name} - Percentage of total')
    ax1.tick_params(axis='x', labelrotation=rotation)