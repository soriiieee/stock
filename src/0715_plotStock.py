# -*- coding: utf-8 -*-
# when   : 2020.0x.xx
# who : [sori-machi]
# what : [ ]
#---------------------------------------------------------------------------
# basic-module
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter('ignore')
#---------------------------------------------------
# sori -module
sys.path.append('/home/griduser/tool')
from getErrorValues import me,rmse,mae,r2 #(x,y)
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# initial
#
from datetime import datetime
# import quandl
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from tqdm import tqdm

# data = quandl.get('WIKI/PRICES',ticker = ['AAPL', 'MSFT', 'WMT'],
#   qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
#   date = { 'gte': '2015-12-31', 'lte': '2016-12-31' },
#   paginate=True
def getStockData(ticker, media="yahoo", start_date="201701010000"):
  yy=start_date[0:4]
  mm=start_date[4:6]
  dd=start_date[6:8]

  start_fmt=f"{yy}/{mm}/{dd}"
  
  data = web.DataReader(ticker,media,start_fmt)
  print(ticker,data.shape)
  print(data.head(2))
  print(data.tail(2))
  return data
  # sys.exit()

if __name__ == "__main__":
  #
      # symbols = get_nasdaq_symbols()
      # use_cols = ['Nasdaq Traded', 'Security Name', 'Listing Exchange', 'Market Category','ETF', 'Round Lot Size', 'Test Issue', 'Financial Status', 'CQS Symbol','NASDAQ Symbol', 'NextShares']
      # symbols = symbols.reset_index()
      # symbols.to_csv("../dat/tickers.csv")
      # # print(datetime.now().strftime("%Y-%m-%d"))
      # sys.exit()

  os.makedirs("../dat/0715" , exist_ok=True)
  _ticker=["AAPL","MSFT","NVDA","INTC","TSM","SAP","QCOM","DCM","CTSH","EMC"]
  media="yahoo"
  start_date="201701010000"
  for ticker in _ticker:
    df = getStockData(ticker, media=media, start_date=start_date)
    df = df.reset_index()
    df.to_csv(f"../dat/0715/{ticker}.csv", index=False)
    # print()
    # print(df.shape)
    # sys.exit()
    
