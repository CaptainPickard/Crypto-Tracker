import backtrader as bt
import datetime



# Strategy class
# Simple RSI buy when oversold < 30 and sell when overbought > 70
class RSTStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        # Buy Logic
        if self.rsi < 20 and not self.position:
            self.buy(size=1)
        if self.rsi > 81 and self.position:
            self.close()

        # Sell Logic
        if self.rsi > 81 and not self.position:
            self.sell(size=1)
        if self.rsi < 20 and self.position:
            self.close()


cerebro = bt.Cerebro()
cerebro.broker.setcash(5000)

data = bt.feeds.GenericCSVData(
    dataname='crypto-tracker\data\ETHUSDT\eth_1hour_data_90day.csv' ,
    dtformat=lambda x: datetime.datetime.utcfromtimestamp(int(x) / 1000),
    compression=1,
    timeframe=bt.TimeFrame.Minutes
    )

cerebro.adddata(data)

cerebro.addstrategy(RSTStrategy)
cerebro.run()
cerebro.plot()