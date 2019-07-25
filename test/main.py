import time
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import sys
import mpl_finance as mpf
import datetime as datetime
import tushare as ts

##style.use('ggplot')
start = datetime.datetime(2019,1,1)
df_2330 = web.DataReader('2330.TW','yahoo',start=start)
##time.sleep(1)
##print(df.tail())
##df = web.DataReader('2331.TW','yahoo',start,end)
##time.sleep(1)
##print(df.tail())
##df = web.DataReader('2332.TW','yahoo',start,end)
##time.sleep(1)
##print(df.tail())
df_2330.index = df_2330.index.format(formatter=lambda x: x.strftime('%Y-%m-%d')) 

fig = plt.figure(figsize=(24, 8))

ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(range(0, len(df_2330.index), 30))
ax.set_xticklabels(df_2330.index[::30])
mpf.candlestick2_ochl(ax, df_2330['Open'], df_2330['Close'], df_2330['High'],df_2330['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75) 
plt.show()                                      