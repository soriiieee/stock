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
import quandl

print("start analysis quandl!")

company="appl"
input_path =f"../dat/{company}.csv"
df = pd.read_csv(input_path)

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
f,ax = plt.subplots(figsize=(22,16))
for lag in [7,30, 180, 365, 365*3]:
  c_lag = str(lag)
  df[f"mv_{c_lag}day"] = df["Close"].rolling(lag).mean()

# plot
for col in df.columns:
  ax.plot(df[col], label = col)

ax.legend()
ax.set_title(company)

f.savefig(f"../png/{company}.png", bbox_inches="tight")
print(f"make END: {company}")

sys.exit()





