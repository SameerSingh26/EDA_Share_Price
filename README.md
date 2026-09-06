# EDA_Share_Price
Well do EDA for one of the share price

# 📊 TCS Stock Market — Exploratory Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on historical **Tata Consultancy Services (TCS)** stock market data.

The data is collected from **Yahoo Finance** using the Python `yfinance` library. The project uses Python and Pandas to clean, analyze, and visualize historical TCS stock-price data.

The analysis focuses on:

* Stock price movements
* Daily returns
* Weekday return patterns
* Trading volume
* Moving averages
* Volatility
* Correlation
* Outliers
* Data visualizations
* Historical insights

A specific analysis question explored in the project is:

> **Does TCS historically show different average returns on different weekdays, particularly on Monday?**

The analysis is based on historical data and is intended for educational purposes. It does **not** predict future stock performance or provide investment advice.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Collect historical TCS stock-market data
* Clean and prepare the dataset
* Understand the structure of the data
* Calculate descriptive statistics
* Identify missing values and duplicate records
* Analyze TCS stock prices
* Calculate daily percentage returns
* Analyze weekday return patterns
* Analyze trading volume
* Calculate moving averages
* Analyze stock volatility
* Perform correlation analysis
* Detect outliers
* Create meaningful visualizations
* Generate insights from the historical data

---

## 🔄 Project Workflow

```text
TCS Stock Data (Yahoo Finance)
            ↓
      Data Collection
            ↓
       Data Cleaning
            ↓
   Understanding Dataset
            ↓
  Descriptive Statistics
            ↓
 Missing Values & Duplicates
            ↓
       Price Analysis
            ↓
       Daily Returns
            ↓
     Weekday Analysis
            ↓
      Volume Analysis
            ↓
      Moving Averages
            ↓
    Volatility Analysis
            ↓
    Correlation Analysis
            ↓
      Outlier Analysis
            ↓
      Visualizations
            ↓
      EDA Conclusions
```

---

## 📁 Project Structure

```text
EDA_Share_Price/
│
├── data/
│   └── TCS_stock.csv
│
├── src/
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── app.py
├── requirements.txt
└── README.md
```

### File Description

| File/Folder          | Purpose                          |
| -------------------- | -------------------------------- |
| `data/`              | Stores the TCS stock dataset     |
| `data_collection.py` | Downloads historical stock data  |
| `data_cleaning.py`   | Cleans and validates the dataset |
| `analysis.py`        | Performs calculations and EDA    |
| `visualization.py`   | Creates charts and plots         |
| `app.py`             | Main entry point of the project  |
| `requirements.txt`   | Contains Python dependencies     |
| `README.md`          | Project documentation            |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **yfinance**
* **VS Code**
* **Git & GitHub**

---

# 1️⃣ Data Collection

Historical TCS stock data is collected using the `yfinance` Python library.

The Yahoo Finance ticker for TCS on the National Stock Exchange of India is:

```text
TCS.NS
```

### Example

```python
import yfinance as yf

def data_collection(ticker):

    df = yf.download(
        ticker,
        start="2021-01-01",
        end="2026-01-01"
    )

    return df
```

The project uses:

```python
df = data_collection("TCS.NS")
```

The dataset contains stock-market information such as:

```text
Date
Open
High
Low
Close
Volume
```

---

# 2️⃣ Data Cleaning

The collected dataset is checked and prepared before performing analysis.

### Cleaning tasks

* Check column names
* Check data types
* Check missing values
* Check duplicate records
* Remove missing records where required
* Remove duplicate records
* Verify dataset shape
* Prepare the data for analysis

Example:

```python
print(df.dtypes)

print(df.isnull().sum())

print(df.duplicated().sum())
```

The current dataset contains:

```text
Rows: 1240
Columns: 5
```

before additional analysis columns are added.

---

# 3️⃣ Understanding the Dataset

Before performing EDA, the dataset structure is inspected.

### First five rows

```python
df.head()
```

### Last five rows

```python
df.tail()
```

### Number of rows and columns

```python
df.shape
```

### Column names

```python
df.columns
```

### Data types

```python
df.dtypes
```

These checks help understand the structure and quality of the dataset before analysis.

---

# 4️⃣ Descriptive Statistics

Descriptive statistics are used to understand the numerical characteristics of TCS stock data.

```python
df.describe()
```

The analysis includes:

* Mean
* Standard deviation
* Minimum
* Maximum
* 25th percentile
* Median
* 75th percentile

These statistics provide a basic summary of the historical stock prices and trading volume.

---

# 5️⃣ Missing Values & Duplicates

The dataset is checked for missing and duplicate records.

### Missing values

```python
df.isnull().sum()
```

### Duplicate rows

```python
df.duplicated().sum()
```

For the current dataset:

* Missing values: **0**
* Duplicate rows: **0**

The first `NaN` that appears after calculating daily returns is expected because the first trading day does not have a previous trading day for comparison.

---

# 6️⃣ Price Analysis

Price analysis focuses on:

* Open price
* High price
* Low price
* Closing price

The **closing price** is particularly useful for studying the historical movement of TCS stock.

Example:

```python
plt.plot(df["Close"])

plt.title("TCS Closing Price")

plt.xlabel("Date")

plt.ylabel("Price")

plt.show()
```

This visualization helps identify long-term price trends and major price movements.

---

# 7️⃣ Daily Returns

Daily return measures the percentage change in TCS's closing price from one trading day to the next.

The project calculates daily returns using:

```python
df["Daily_return"] = df["Close"].pct_change() * 100
```

For example, if the previous closing price was ₹1,000 and the current closing price was ₹1,020:

```text
Daily Return = 2%
```

Daily returns help analyze:

* Positive price movements
* Negative price movements
* Average daily performance
* Large price changes
* Return volatility

The first return is removed because there is no previous trading day:

```python
df = df.dropna(subset=["Daily_return"])
```

---

# 8️⃣ Weekday Analysis

One of the project-specific analyses is to investigate whether TCS has historically shown different return patterns across weekdays.

A weekday column is created using:

```python
df["Day"] = df.index.day_name()
```

The average return for each weekday is calculated using:

```python
def weekday_analysis(df):

    result = df.groupby("Day")["Daily_return"].mean()

    return result
```

This allows us to compare:

```text
Monday
Tuesday
Wednesday
Thursday
Friday
```

The purpose is to answer:

> **Which weekday historically had the highest average daily return for TCS?**

This analysis describes historical behavior only. It should not be interpreted as a guaranteed trading strategy.

---

# 9️⃣ Volume Analysis

Trading volume represents the number of shares traded during a particular period.

Example:

```python
plt.plot(df["Volume"])

plt.title("TCS Trading Volume")

plt.xlabel("Date")

plt.ylabel("Volume")

plt.show()
```

Volume analysis can help identify periods of unusually high or low trading activity.

High-volume periods can then be investigated alongside significant price movements.

---

# 🔟 Moving Averages

Moving averages help identify the general trend of the stock price by smoothing short-term fluctuations.

### 20-Day Moving Average

```python
df["MA_20"] = df["Close"].rolling(window=20).mean()
```

### 50-Day Moving Average

```python
df["MA_50"] = df["Close"].rolling(window=50).mean()
```

### 200-Day Moving Average

```python
df["MA_200"] = df["Close"].rolling(window=200).mean()
```

These moving averages can be compared with the closing price to understand short-term and long-term trends.

---

# 1️⃣1️⃣ Volatility Analysis

Volatility measures how much stock returns fluctuate over time.

The project can calculate rolling volatility using:

```python
df["Volatility"] = (
    df["Daily_return"]
    .rolling(window=20)
    .std()
)
```

Higher volatility indicates larger fluctuations in daily returns.

Lower volatility indicates relatively smaller fluctuations.

---

# 1️⃣2️⃣ Correlation Analysis

Correlation helps understand the relationship between numerical variables.

Example:

```python
correlation = df.corr(numeric_only=True)

print(correlation)
```

Variables that can be analyzed include:

```text
Open
High
Low
Close
Volume
Daily_return
```

A correlation heatmap can be created using Seaborn:

```python
sns.heatmap(correlation, annot=True)

plt.title("TCS Stock Correlation")

plt.show()
```

Correlation measures association between variables; it does not by itself prove causation.

---

# 1️⃣3️⃣ Outlier Analysis

Outlier analysis identifies unusual observations in the dataset.

Daily returns are particularly useful for detecting unusually large price movements.

Example:

```python
sns.boxplot(x=df["Daily_return"])

plt.title("TCS Daily Return Outliers")

plt.show()
```

Outliers may represent periods where TCS experienced unusually large positive or negative returns.

These observations can be investigated further using their corresponding dates and trading volumes.

---

# 1️⃣4️⃣ Data Visualizations

The project will use visualizations to make the EDA findings easier to understand.

### Planned visualizations

* 📈 TCS Closing Price
* 📊 Trading Volume
* 📉 Daily Returns
* 📈 Moving Averages
* ⚡ Rolling Volatility
* 🔥 Correlation Heatmap
* 📦 Daily Return Outliers
* 📊 Return Distribution
* 📊 Average Return by Weekday

The visualizations will be implemented in:

```text
src/visualization.py
```

---

# 1️⃣5️⃣ EDA Conclusions

After completing the analysis, the project will summarize the important findings from the historical TCS stock data.

The conclusions will be based on actual results generated from the dataset.

The analysis may identify:

* Overall price trend
* Average daily return
* Best and worst historical return periods
* Weekday return patterns
* Trading-volume patterns
* High-volatility periods
* Relationships between stock variables
* Unusual return observations
* Short-term and long-term trends

A specific conclusion will also address the weekday analysis:

> **Does Monday historically have a higher or lower average return compared with the other trading days?**

The project will not assume the answer in advance.

---

# 🚀 How to Run the Project

## Step 1: Clone the repository

```bash
git clone <your-github-repository-url>
```

## Step 2: Navigate to the project

```bash
cd EDA_Share_Price
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the project

```bash
python app.py
```

---

# 📦 Requirements

Create a `requirements.txt` file containing:

```text
pandas
numpy
matplotlib
seaborn
yfinance
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📈 Future Improvements

Possible improvements include:

* Add RSI and MACD technical indicators
* Compare TCS with NIFTY 50
* Compare TCS with other IT companies
* Build an interactive Streamlit dashboard
* Automate daily data collection
* Add more statistical analysis
* Build a stock-price prediction model
* Deploy the analysis as a web application

---

# ⚠️ Disclaimer

This project is created for **educational and analytical purposes**.

The analysis is based on historical stock-market data. Historical performance does not guarantee future performance.

This project should not be considered financial or investment advice.

---

## 👨‍💻 Author

**Sameer**

### Skills Used

```text
Python | Pandas | NumPy | Matplotlib | Seaborn | SQL
```

---

## ⭐ Project Goal

The goal of this project is to demonstrate practical data-analysis skills through a complete EDA workflow:

```text
Python
   ↓
Data Collection
   ↓
Data Cleaning
   ↓
Data Understanding
   ↓
Exploratory Data Analysis
   ↓
Statistical Analysis
   ↓
Data Visualization
   ↓
Insights
```

The project demonstrates how historical stock-market data can be transformed into meaningful analytical insights using Python.
