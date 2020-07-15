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

def mk_merit(price,lag):
  _se=[]
  p_diff= price.diff(lag).values.tolist()
  p0 = price.values.tolist()

  for p in zip(p0, ):
    price.diff()

  return se


if __name__ == "__main__":
  #

  os.makedirs("../dat/0715/png" , exist_ok=True)
  _ticker=["TSM","SAP","QCOM","DCM","CTSH","EMC"]
  _lag=[7,30,90]
  
  # df = pd.read_csv("../dat/0715/{}")
  for ticker in _ticker:
    df = pd.read_csv(f"../dat/0715/{ticker}.csv")
    p = df["Close"]
    p["logp"] = np.log(p["Close"])

    for lag in _lag:
      col ="mv_" +str(lag)
      p[col] = p["Close"].rolling(lag).mean()

    p["diff"] = price["Close"].diff().fillna(0)

    print(df.head())
    sys.exit()

    
