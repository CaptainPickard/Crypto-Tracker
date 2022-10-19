import config, csv
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)

# Use this to pull csv data to test with backtest.py

# Get all current prices for all coins in binance
# prices = client.get_all_tickers()
# for price in prices:
#     print(price)


# Get all 15 minute data and write that to a csv
klines = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1HOUR, "90 day ago UTC")

csvfile = open('eth_1hour_data_90day.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

for tick in klines:
    candlestick_writer.writerow(tick)

print(len(klines))


# Get historical data for one asset "1 day ago UTC"
# https://python-binance.readthedocs.io/en/latest/market_data.html#id7
# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
# for candle in klines:
#     print(candle)





