# main.py
import asyncio
import streamlit as st
from monitor.binance_stream import listen_to_binance

st.set_page_config(page_title="Live BTC/USDT Monitor", layout="wide")
st.title("📊 Live Transaction Monitor")

# Dropdown for symbol selection
symbol = st.selectbox("Select Symbol", ["btcusdt", "ethusdt", "bnbusdt"], index=0)

# Run Binance listener for selected symbol
try:
    asyncio.run(listen_to_binance(symbol))
except Exception as e:
    st.error(f"Error: {e}")
