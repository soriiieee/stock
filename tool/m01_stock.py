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

# from getErrorValues import me,rmse,mae,r2 #(x,y)
# from getPlot import drawPlot,autoLabel #(x=False,y,path),(rects, ax)
# from convSokuhouData import conv2allwithTime,conv2CutCols #(df),(df, ave=minutes,hour)
# from convAmedasData import conv2allwithTime,conv2CutCols #(df),(df, ave=minutes,hour)
# from checkFileExistSize import checkFile #(input_path)
# from plotMonthData import plotDayfor1Month #(df,_col,title=False)
#---------------------------------------------------

#import message

# from m01_stock import mk_mvave, mk_profit, mk_log_profit


# main context
class StockAnalysis:
  def __init__(self):
    print("analysis class")
  
  #kiso keisan
  def calc(self,df,_lags, colname="Close"):
    for lag in _lags:
      col = f"mv{lag}"
      df[col] = self.mk_mvave(df[colname],lag=lag)
      col2 = f"prf{lag}"
      df[col2] = self.mk_profit(df[colname],lag=lag)
    df["log_pro"] = self.mk_log_profit(df[colname])
    return df

  #subroutine--------------------------------
  def mk_mvave(self,se,lag=25):
    se = np.round(se.rolling(lag).mean().values,1)
    return se

  def mk_profit(self,se,lag=25):
    se = np.round(se.pct_change(lag),1)
    return se

  def mk_log_profit(self,se):
    se = np.log(se).diff().fillna(0)
    return se

  def plot_1com(self,df,ticker,colname="Close"):
    f,ax = plt.subplots(3,1,figsize=(22,15))

    p_col=[colname]
    col0 = p_col + [ col for col in df.columns if "mv" in col]
    col1 = [ col for col in df.columns if "prf" in col]
    col2 = [col for col in df.columns if "log" in col]
    length= df.shape[0]
    for col in col0:
      ax[0].plot(df[col].values, label=col)
    #     ax[0].legend()
        
    for col in col1:
      ax[1].plot(df[col].values, label=col)
      ax[1].set_ylim(-1,1)
      ax[1].legend()
        
    for col in col2:
      ax[2].plot(df[col].values, label=col)
      ax[2].legend()

    for i in range(3):
      ax[i].set_title(ticker, pad=-15)
      ax[i].set_xticks(np.arange(0,length,30))
      ax[i].set_xticklabels(df["Date"].values[0:length:30],rotation=45)
    
    return plt


