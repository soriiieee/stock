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
  # sihyou
  # https://qiita.com/innovation1005/items/5be026cf7e1d459e9562 に資料が表示されている
  # _ticker=["^DJI","^NDQ","^SPX"]

  _ticker ={
    "index":["^NDX","^NDXT","^IXCO","^OEX","^GSPC","^SOX","^N225"],
    "comp":["AAPL","MSFT","NVDA","INTC","TSM","SAP","QCOM","DCM","CTSH","EMC"],
    "etf":["VCIT"]
    }
  #NKX:nikkei-ave
  #IXIC:dow-ave
  #ES.C:sp500-ave

  # "^NDX" : nasdaq 100
  # "^NDXT" : nasdaq tech 100
  # "^IXCO" : nasdaq ccomputer
  # "^OEX" : s&p 100
  # "^GSPC" : s&p 500
  # "^SOX" : handoutai 
  # "^N225": nikkei225

  # <ETF>
  # VCIT


  # media="stooq"
  media="yahoo"
  cate="index"
  os.makedirs(f"../dat/{cate}" , exist_ok=True)
  start_date="201701010000"
  for ticker in _ticker[cate]:
    df = getStockData(ticker, media=media, start_date=start_date)
    df = df.reset_index()
    df.to_csv(f"../dat/{cate}/{ticker}.csv", index=False)
    # print()
    # print(df.shape)
    # sys.exit()
    
