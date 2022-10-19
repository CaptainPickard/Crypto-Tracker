from flask import Flask, render_template, request, flash, redirect, jsonify
from markupsafe import escape
# from sympy import symbols
from binance.enums import *
import config, csv
from binance.client import Client
import uuid
import ssl


uuid.uuid4().hex

app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
client = Client(config.API_KEY, config.API_SECRET, tld='us')

@app.route("/")
def index():
    title = 'Crypto Tracker'
    account = client.get_account()
    balance = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balance=balance, symbols=symbols)

@app.route("/buy", methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_order(symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            quantity=request.form['quantity'],
            )
    except Exception as e:
        flash(e.message, "Error Minimum Ammount Not Valid")

    return redirect('/')

# This rout is not currently being used
@app.route("/sell")
def sell():
    return 'sell'

# This rout is not currently being used
@app.route("/settings")
def settings():
    return 'settings'

# this is the main route which turns the json historical data into plotable data in charts.js
@app.route("/history")
def history():
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "30 day ago UTC")

    processed_klines = []

    for data in klines:
        candlestick = { 
            "time": data[0] / 1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
            }

        processed_klines.append(candlestick)

    return jsonify(processed_klines)


ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    app.run(debug=True)