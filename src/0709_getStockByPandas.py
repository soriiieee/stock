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
#   paginate=True)

# print(datetime.now().strftime("%Y-%m-%d"))
# sys.exit()
symbols = get_nasdaq_symbols()
datum = web.DataReader("GOOGL","yahoo","2019/11/1")
print(datum.tail())
sys.exit()
def getStockData(sub, ticker):
  start_date = "2010-01-01"
  end_date = datetime.now().strftime("%Y-%m-%d")
  df = quandl.get(f"{sub}/{ticker}",start_date=start_date,end_date=end_date)
  return df

if __name__ == "__main__":
  SUB="WIKI"
  TICKER="AAPL.4"
  DAT="/home/griduser/work/sori-py2/stock/dat"

  DAT_DIR=f"{DAT}/{SUB}"
  os.makedirs(DAT_DIR, exist_ok=True)

  df = getStockData(SUB, TICKER)

  df.to_csv(f"{DAT_DIR}/{TICKER}.csv")
  print(df.shape)
  print(df.tail())
  sys.exit()

