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
df = data_collection()
print(df.head())