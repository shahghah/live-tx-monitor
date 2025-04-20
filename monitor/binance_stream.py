# monitor/binance_stream.py
import json
import asyncio
import pandas as pd
import websockets
import plotly.graph_objs as go
from collections import deque
from datetime import datetime
import streamlit as st

TRADE_LIMIT = 100

def render_chart(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['price'],
        mode='lines+markers',
        name=symbol.upper()
    ))
    fig.update_layout(
        title=f'Live {symbol.upper()} Prices',
        xaxis_title='Time',
        yaxis_title='Price (USD)',
        autosize=True
    )
    st.plotly_chart(fig, use_container_width=True)

async def listen_to_binance(symbol: str):
    url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"
    buffer = deque(maxlen=TRADE_LIMIT)

    async with websockets.connect(url) as websocket:
        while True:
            message = await websocket.recv()
            trade = json.loads(message)
            data = {
                "price": float(trade['p']),
                "quantity": float(trade['q']),
                "timestamp": datetime.fromtimestamp(trade['T'] / 1000.0)
            }
            buffer.append(data)
            df = pd.DataFrame(buffer)
            render_chart(df, symbol)
