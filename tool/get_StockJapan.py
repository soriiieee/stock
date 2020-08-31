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
from datetime import datetime, timedelta
import warnings
warnings.simplefilter('ignore')
from tqdm import tqdm
# import seaborn as sns
#---------------------------------------------------
# sori -module
sys.path.append('/home/griduser/tool')
from getErrorValues import me,rmse,mae,r2 #(x,y)
#---------------------------------------------------

from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError


def get_price(code=7201, yy=10, freq=1):
  code = code+".T"
  my_stock = share.Share(code)

  symbol_data = my_stock.get_historical(
    share.PERIOD_TYPE_YEAR,yy,
    share.FREQUENCY_TYPE_DAY,freq
  )

  df = pd.DataFrame(symbol_data.values(), index=symbol_data.keys()).T
  df.timestamp = pd.to_datetime(df.timestamp, unit='ms')
  # df.index = pd.DatetimeIndex(df.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')
  df["time"] = df.timestamp.apply(lambda x: x.strftime("%Y-%m-%d"))
  df = df.drop(["timestamp", "open", "high", "low"], axis=1)
  df = df[["time","volume","close"]]

  df["close"] = np.round(df["close"],2)
  df["volume"] = np.round(df["volume"],2)
  df["time"] = pd.to_datetime(df["time"])

  df["benefit"] = np.log(df["close"]).diff().fillna(0)*100
  df["benefit"] =np.round(df["benefit"],3)

  return df


def cut_data(df,sta="2012-09-30", end="2013-03-31"):
  df = df[df["time"]>=sta]
  df = df[df["time"]<=end].reset_index(drop=True)
  return df

def plot_price(df, _col, title):
  f,ax = plt.subplots(figsize=(22,8))
  for col in _col:
    ax.plot(np.arange(len(df)), df[col], label=col)

  ax.set_title(title, pad=-15)
  ax.legend()
  ax.plot()

  f.savefig(f"../png/{title}.png", bbox_inches="tight")
  print(f"end {title}")
  return 

def plot_ax(ax,df,code, col="close"):
  ax.plot(np.arange(len(df)), df[col], label=code)
  return ax

if __name__ == "__main__":
  _code =["5202","7272","4927","4502"]
  _df=[]
  for code in _code:
    #get _ stock 
    if os.path.exists(f"../dat/japan/{code}.csv"):
      df = pd.read_csv(f"../dat/japan/{code}.csv")
      df["time"] = pd.to_datetime(df["time"])
    else:
      df = get_price(code)
      df = cut_data(df)
      df.to_csv(f"../dat/japan/{code}.csv", index=False)

    # df["close"] = df["close"] /df["close"].iloc[0]
    print(code, np.mean(df["benefit"]))
    # sys.exit()
    # _df.append(df)

  # f,ax = plt.subplots(figsize=(22,8))
  # for i, df in enumerate(_df):
  #   code = _code[i]
  #   ax = plot_ax(ax,df,code,col="benefit")
  
  # ax.legend()
  # f.savefig(f"../png/ratio.png", bbox_inches="tight")

    
  # plot_price(df, ["close"],code)
  sys.exit


