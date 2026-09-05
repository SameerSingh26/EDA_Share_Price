# EDA_Share_Price
Well do EDA for one of the share price

# 📊 TCS Stock Market — Exploratory Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on historical **Tata Consultancy Services (TCS)** stock market data.

The data is collected from **Yahoo Finance** using the Python `yfinance` library. The project analyzes stock prices, daily returns, trading volume, moving averages, volatility, correlations, and outliers to understand the historical behavior of TCS stock.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Collect historical TCS stock market data
* Clean and prepare the dataset
* Understand the structure of the data
* Calculate descriptive statistics
* Identify missing values and duplicate records
* Analyze TCS stock prices
* Calculate daily returns
* Analyze trading volume
* Calculate moving averages
* Analyze stock volatility
* Perform correlation analysis
* Detect outliers
* Create meaningful visualizations
* Summarize important findings from the EDA

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
TCS_Stock_EDA/
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
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **yfinance**
* **Jupyter/VS Code**
* **Git & GitHub**

---

# 1️⃣ Data Collection

Historical TCS stock data is downloaded using the `yfinance` Python library.

The Yahoo Finance ticker for TCS on the National Stock Exchange of India is:

```python
TCS.NS
```

### Example

```python
import yfinance as yf

def data_collection():

    df = yf.download(
        "TCS.NS",
        start="2020-01-01",
        end="2026-01-01"
    )

    df.to_csv("data/TCS_stock.csv")

    return df
```

The downloaded dataset contains information such as:

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

The next step is to prepare the dataset for analysis.

### Tasks performed

* Check data types
* Convert Date column to datetime
* Check missing values
* Remove duplicate records
* Handle unnecessary columns
* Sort data by date

Example:

```python
df.info()
df.isnull().sum()
df.duplicated().sum()
```

---

# 3️⃣ Understanding the Dataset

Before performing analysis, we inspect the dataset.

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

### Dataset information

```python
df.info()
```

---

# 4️⃣ Descriptive Statistics

Descriptive statistics help us understand the numerical characteristics of the stock data.

```python
df.describe()
```

We analyze:

* Mean
* Standard deviation
* Minimum value
* Maximum value
* 25th percentile
* Median
* 75th percentile

---

# 5️⃣ Missing Values & Duplicates

We check whether the dataset contains missing or duplicate records.

### Missing values

```python
df.isnull().sum()
```

### Duplicate rows

```python
df.duplicated().sum()
```

If required, missing values and duplicate records are handled during the cleaning stage.

---

# 6️⃣ Price Analysis

The price analysis focuses on:

* Open price
* High price
* Low price
* Closing price

The **closing price** is especially important for understanding the historical movement of the stock.

Example visualization:

```python
plt.plot(df["Close"])
plt.title("TCS Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
```

---

# 7️⃣ Daily Returns

Daily return measures the percentage change in the stock price from one trading day to the next.

```python
df["Daily_Return"] = df["Close"].pct_change()
```

Daily returns help us understand:

* Positive price movements
* Negative price movements
* Daily performance
* Large price changes

---

# 8️⃣ Volume Analysis

Trading volume represents the number of shares traded during a particular period.

```python
plt.plot(df["Volume"])
plt.title("TCS Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
```

Volume analysis can help identify periods of unusually high or low trading activity.

---

# 9️⃣ Moving Averages

Moving averages help identify the general trend of the stock price.

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

These can be visualized together with the closing price.

---

# 🔟 Volatility Analysis

Volatility measures how much the stock price or returns fluctuate over time.

We can calculate rolling volatility using daily returns.

```python
df["Volatility"] = df["Daily_Return"].rolling(window=20).std()
```

Higher volatility indicates larger fluctuations in returns.

Lower volatility indicates relatively smaller fluctuations.

---

# 1️⃣1️⃣ Correlation Analysis

Correlation helps understand the relationship between numerical variables.

For example:

```python
correlation = df.corr(numeric_only=True)

print(correlation)
```

We can analyze relationships between:

```text
Open
High
Low
Close
Volume
Daily_Return
```

A correlation heatmap can be created using Seaborn.

```python
sns.heatmap(correlation, annot=True)
plt.title("TCS Stock Correlation")
plt.show()
```

> Correlation shows association between variables; it does not by itself prove causation.

---

# 1️⃣2️⃣ Outlier Analysis

Outlier analysis identifies unusual observations in the dataset.

For example, we can use a boxplot for daily returns:

```python
sns.boxplot(x=df["Daily_Return"])
plt.title("TCS Daily Return Outliers")
plt.show()
```

Outliers may represent periods of unusually large positive or negative price movements.

---

# 1️⃣3️⃣ Data Visualizations

The project uses visualizations to make the analysis easier to understand.

### Planned visualizations

* 📈 TCS Closing Price
* 📊 Trading Volume
* 📉 Daily Returns
* 📈 Moving Averages
* ⚡ Volatility
* 🔥 Correlation Heatmap
* 📦 Outlier Boxplots
* 📊 Return Distribution

---

# 1️⃣4️⃣ EDA Conclusions

After completing the analysis, we summarize the important observations from the TCS historical stock data.

The conclusions may include:

* Overall price trend
* Periods of significant price movement
* Average daily return
* Volatility behavior
* Trading-volume patterns
* Relationship between stock-price variables
* Presence of unusual return observations
* Behavior of short-term and long-term moving averages

> The conclusions will be based on the actual results generated from the dataset rather than assumptions.

---

# 🚀 How to Run the Project

## Step 1: Clone the repository

```bash
git clone <your-github-repository-url>
```

## Step 2: Navigate to the project

```bash
cd TCS_Stock_EDA
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the project

```bash
python main.py
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

Install them using:

```bash
pip install -r requirements.txt
```

---

# 📈 Future Improvements

Possible improvements for this project include:

* Add technical indicators such as RSI and MACD
* Add interactive dashboards
* Compare TCS with NIFTY 50
* Compare TCS with other IT companies
* Build a stock-price prediction model
* Create a Streamlit dashboard
* Automate daily data collection
* Deploy the analysis as a web application

---

# ⚠️ Disclaimer

This project is created for **educational and analytical purposes**.

Historical stock-market performance does not guarantee future performance. This project should not be considered financial or investment advice.

---

## 👨‍💻 Author

**Sameer**

### Skills Used

```text
Python | Pandas | NumPy | Matplotlib | Seaborn | SQL
```

---

## ⭐ Project Goal

The goal of this project is to demonstrate practical skills in:

**Python → Data Collection → Data Cleaning → EDA → Data Visualization → Insights**
