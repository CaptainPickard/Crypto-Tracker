import backtrader as bt
from backtrader.indicators import SumN, TrueLow, TrueRange
import talib
import datetime
import math
import numpy as np



class Momentum(bt.Indicator):
    lines = ('Mom',)
    params = (
        ('period', 20),
    )

    plotinfo = dict(subplot=False)

    def _plotlabel(self):
        plabels = [self.p.period]
        return plabels

    def __init__(self):
        highest = bt.ind.Highest(self.data.high, period=self.p.period)
        lowest = bt.ind.Lowest(self.data.low, period=self.p.period)
        midline = (highest + lowest) / 2
        m_avg = bt.ind.MovingAverageSimple(self.data.close, period=self.p.period)
        self.delta = self.data.close - ((midline + m_avg) / 2)
        # fit_y = np.array(range(0, self.p.period))
        # self.lines.Mom = delta(window=self.p.period).apply(lambda x: np.polyfit(fit_y, x, 1)[0] * (self.p.period - 1) + np.polyfit(fit_y, x, 1)[1], raw=True)
        # # Probably need to rewrite the lines for fit_y and self.lines.Mom



class EMAStrategy(bt.Strategy):

    params = (
        ("twohundred", 200), 
        ('period', 20),
        ('order_percentage', 0.95)
        )

    plotinfo = dict(subplot=False)

    def _plotlabel(self):
        plabels = [self.p.period]
        return plabels

    def __init__(self):
        self.moving_average = bt.ind.EMA(
            self.data.close, 
            period=self.params.twohundred, 
            plotname="Moving Average"
            )
        
        highest = bt.ind.Highest(self.data.high, period=self.p.period)
        lowest = bt.ind.Lowest(self.data.low, period=self.p.period)
        midline = (highest + lowest) / 2
        m_avg = bt.ind.MovingAverageSimple(self.data.close, period=self.p.period)
        self.delta = self.data.close - ((midline + m_avg) / 2)


    def next(self):
        # BUY LOGIC
        pass


cerebro = bt.Cerebro()
cerebro.broker.setcash(5000)

data = bt.feeds.GenericCSVData(
    dataname='data\ETHUSDT\eth_1hour_data_90day.csv' ,
    dtformat=lambda x: datetime.datetime.utcfromtimestamp(int(x) / 1000),
    compression=60,
    timeframe=bt.TimeFrame.Minutes
    )

cerebro.adddata(data)

cerebro.addstrategy(EMAStrategy)

cerebro.run()
cerebro.plot()