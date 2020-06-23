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
api_key = open("../env/api.key").read()
# print(api_key)
# sys.exit()
quandl.ApiConfig.api_key = str(api_key)

# data = quandl.get('WIKI/PRICES',ticker = ['AAPL', 'MSFT', 'WMT'],
#   qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
#   date = { 'gte': '2015-12-31', 'lte': '2016-12-31' },
#   paginate=True)

start_date = "2001-01-01"
end_date = "2019-12-31"


appl = quandl.get("WIKI/AAPL.4",start_date=start_date, end_date=end_date)
appl.to_csv("../dat/appl.csv")

print(appl.shape)
print(appl.head())
print(appl.columns)




