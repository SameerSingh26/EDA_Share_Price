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
df = data_collection()
df = data_cleaning(df)
print(df.head())