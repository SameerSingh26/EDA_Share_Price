import pandas as pd
def calculate_daily_return(df):
    df["Daily_return"] = df["Close"].pct_change()* 100
    df = df.dropna(subset=["Daily_return"])
    df["Day"]= df.index.day_name()
    return(df)

def weekday_analysis(df):
    result = df.groupby("Day")["Daily_return"].mean()
    return(result)