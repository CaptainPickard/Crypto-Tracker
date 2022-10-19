import numpy
import talib
from numpy import genfromtxt

# This is a test file for testing the ta-lib python library for technical analysis

my_data = genfromtxt('data\ETHUSDT\eth_1day_data_3years.csv', delimiter=',')
close_data = my_data[:,4]
rsi_close_data = talib.RSI(close_data, timeperiod=14)
print(rsi_close_data)


# Ta-Lib docs
# https://mrjbq7.github.io/ta-lib/funcs.html

################################################################
#  Number generator for testing
# close = numpy.random.random(1000)
# print(close)

# All important Exponential Moving Averages
# five_ema = talib.EMA(close, timeperiod=5)
# thirteen_ema = talib.EMA(close, timeperiod=13)
# fifty_ema = talib.EMA(close, timeperiod=50)
# twohundred_ema = talib.EMA(close, timeperiod=200)
# eighthundred_ema = talib.EMA(close, timeperiod=800)
# print(five_ema, thirteen_ema, fifty_ema, twohundred_ema, eighthundred_ema)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Relative Strength Inxed
# rsi = talib.RSI(close, timeperiod=14)
# print(close)
################################################################
