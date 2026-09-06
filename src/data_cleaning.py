import pandas as pd

def data_cleaning(df):
    print(df.head(20))
    print(df.columns)
    print(df.dtypes)
    print(df.isnull().sum())
    print(df.duplicated().sum())
    df = df.dropna()
    df = df.drop_duplicates()
    print(df.isnull().sum())
    print(df.duplicated().sum())
    print(df.shape)
    df.columns = df.columns.get_level_values(0)
    return df
