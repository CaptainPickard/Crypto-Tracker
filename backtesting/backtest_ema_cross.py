import backtrader as bt
import datetime
import math


class EMAStrategy(bt.Strategy):
    params = (("fast", 69), ("slow", 420), ('order_percentage', 0.95), ('ticker', 'ETH'))

    def __init__(self):
        self.fast_moving_average = bt.indicators.EMA(
            self.data.close, 
            period=self.params.fast, 
            plotname="Moving Average"
            )

        self.slow_moving_average = bt.indicators.EMA(
            self.data.close, 
            period=self.params.slow, 
            plotname="Moving Average"
            )

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, 
            self.slow_moving_average
            )


    def next(self):
        # BUY LOGIC
        if self.crossover > 0 and not self.position:
            amount_to_invest = (self.params.order_percentage * self.broker.cash)
            self.size = math.floor(amount_to_invest / self.data.close)

            print("Long {} of {}".format(self.size, self.params.ticker))
            self.buy(size=self.size)

        if self.position.size > 0 and self.crossover < 0:
            print("Close {} of {}".format(self.size, self.params.ticker))
            self.close()

        #SHORT LOGIC
        # if self.crossover < 0 and self.position==0:
        #     amount_to_invest = (self.params.order_percentage * self.broker.cash)
        #     self.size = math.floor(amount_to_invest / self.data.close)

        #     print("Short {} of {}".format(self.size, self.params.ticker))
        #     self.sell(size=self.size)

        # if self.crossover > 0:
        #     print("Close {} of {}".format(self.size, self.params.ticker))
        #     self.close()


cerebro = bt.Cerebro()
cerebro.broker.setcash(5000)

data = bt.feeds.GenericCSVData(
    dataname='crypto-tracker\data\ETHUSDT\eth_1min_data_3day.csv' ,
    dtformat=lambda x: datetime.datetime.utcfromtimestamp(int(x) / 1000),
    compression=60,
    timeframe=bt.TimeFrame.Minutes
    )

cerebro.adddata(data)

cerebro.addstrategy(EMAStrategy)

cerebro.run()
cerebro.plot()