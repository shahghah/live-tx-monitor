# 📊 Live Transaction Monitor (BTC/USDT and More)

A real-time cryptocurrency transaction monitor using Binance WebSocket streams. Built with Streamlit and Plotly for live charting in your browser.

## ✨ Features
- Real-time trade data from Binance (WebSocket)
- Live-updating Plotly chart
- Streamlit interface
- Select from multiple trading pairs (BTC/USDT, ETH/USDT, BNB/USDT)

---

## 📄 Requirements
```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```txt
streamlit
websockets
pandas
plotly
```

---

## 🚀 Run the App
```bash
streamlit run main.py
```

Then open the provided localhost URL in your browser.

---

## 📂 Project Structure
```
live-tx-monitor/
├── main.py
├── monitor/
│   └── binance_stream.py
├── requirements.txt
└── README.md
```

---

## 🚀 Next Ideas
- Add more symbols dynamically
- Support time interval grouping (e.g. OHLC)
- Save historical trade snapshots
- Add volume and moving average overlays

---

## 🙏 Credits
Built using:
- [Binance WebSocket API](https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)

MIT License
