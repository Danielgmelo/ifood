import pandas as pd

def look_quality_of_the_column_data(dataframe, name_column):
    """
    Show some informations about the column, how dtype, null data and duplicated data.
    
    Parameters:
    dataframe: dataframe containing the column to be analyzed.
    name_column: column to be analyzed.
    """
    
    df = dataframe
    
    column_name = name_column
    print(f'Column name: {column_name}')

    dtype = df.dtypes[name_column]
    print(f"Data type: {dtype}")

    data_null = df[name_column].isnull().sum()
    print(f"Null data: {data_null}")

    duplicate_data = True if df[name_column].nunique() < df[name_column].count() else False
    print(f"Duplicate data: {duplicate_data}")

    print("Values:")
    print(*df[name_column].sort_values().unique(), sep=', ') 