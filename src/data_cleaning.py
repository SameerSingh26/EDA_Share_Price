import pandas as pd

def data_cleaning(df):
    print(df.head(20))
    print(df.columns)
    print(df.dtypes)
    print(df.isnull().sum())
    print(df.duplicated().sum())
    print(df.dropna())
    print(df.shape)
    return df