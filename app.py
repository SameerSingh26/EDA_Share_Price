# Data Collection
#       ↓
# Data Cleaning
#       ↓
# Understanding Dataset
#       ↓
# Descriptive Statistics
#       ↓
# Missing Values / Duplicates
#       ↓
# Price Analysis
#       ↓
# Daily Returns
#       ↓
# Volume Analysis
#       ↓
# Moving Averages
#       ↓
# Volatility Analysis
#       ↓
# Correlation Analysis
#       ↓
# Outlier Analysis
#       ↓
# Visualizations
#       ↓
# EDA Conclusions

from src.data_collection import data_collection
from src.data_cleaning import data_cleaning
from src.analysis import calculate_daily_return,weekday_analysis
df = data_collection("TCS.NS")
df = data_cleaning(df)
df = calculate_daily_return(df)
result = weekday_analysis(df)
print(df[["Daily_return","Day"]].head())
print(df.head())

print(df.columns)
print("WEEKDAY AVERAGE RETURNS")
print(result)