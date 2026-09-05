import pandas as pd
import yfinance as yf 

def data_collection():
   df = yf.download(
      "TCS.NS",
      start ="2021-09-05",
      end = "2026-09-05"
   )
   return df