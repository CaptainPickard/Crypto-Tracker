// this is the main chart info file, colors and indicators need to be constructed here
var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1700,
    height: 500,
	layout: {
		backgroundColor: '#131722',
		textColor: '#d1d4dc',
	},
	grid: {
		vertLines: {
			color: 'rgba(42, 46, 57, 0)',
		},
		horzLines: {
			color: 'rgba(42, 46, 57, 0.6)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
    topColor: 'rgba(38,198,218, 0.56)',
    upColor: 'rgba(38,198,218, 0.56)',
    downColor: 'rgba(255,82,82, 0.8)',
    borderDownColor: 'rgba(255,82,82, 0.8)',
    borderUpColor: 'rgba(0, 150, 136, 0.8)',
    wickDownColor: 'rgba(255,82,82, 0.8)',
    wickUpColor: 'rgba(0, 150, 136, 0.8)',
    lineWidth:2,
});



// fetch('http://127.0.0.1:5000/history')
// 	.then((r) => r.json())
// 	.then((response) => {
// 		console.log(response);
// 		candleSeries.setData(response);
// })


const { log, error } = console;

const getData = async () => {
  const resp = await fetch('http://127.0.0.1:5000/history');
  const data = await resp.json();
  return data;
};

// const renderChart = async () => {
// 	const chartProperties = {
// 	  timeScale: {
// 		timeVisible: true,
// 		secondsVisible: true,
// 	  },
// 	  pane: 0,
// 	};


// const domElement = document.getElementById('chart');
// const chart = LightweightCharts.createChart(domElement, chartProperties);
// const candleseries = chart.addCandlestickSeries();
// const klinedata = await getData();
// candleseries.setData(klinedata);

// const sma_series = chart.addLineSeries({ color: 'red', lineWidth: 1 });
// const sma_data = klinedata
// 	.filter((d) => d.sma)
// 	.map((d) => ({ time: d.time, value: d.sma }));
// sma_series.setData(sma_data);






// console.log('------->1<--------');
// const colors = ['green', 'red', 'blue', 'black', 'purple'];
// let i = 0;
// _.map(klinedata[0].emas, (value, emaNumber) => {
// 	const ema_series = chart.addLineSeries({ color: colors[i], lineWidth: 1 });
// 	const ema_data = klinedata
// 		.filter((d) => d.emas[emaNumber])
// 		.map((d) => ({ time: d.time, value: d.emas[emaNumber] }));
// 	ema_series.setData(ema_data);
// 	i++;
// })


var btcSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_15m");

btcSocket.onmessage = function (event) {
	var message = JSON.parse(event.data);

var candlestick = message.k;
	console.log(message.k)
	
	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}


// candleseries.setMarkers(
// 	klinedata
//     .filter((d) => d.long || d.short)
//     .map((d) =>
//     d.long
//         ? {
//             time: d.time,
//             position: 'belowBar',
//             color: 'green',
//             shape: 'arrowUp',
//             text: 'LONG',
//         }
//         : {
//             time: d.time,
//             position: 'aboveBar',
//             color: 'red',
//             shape: 'arrowDown',
//             text: 'SHORT',
//         }
//     )
// );

// };
// renderChart();