import streamlit as st
import pandas as pd
import yfinance as yf

st.write(""" 
# Simple Stock Price App

Here , we are showing GOOGLE stock **closing price** and **volume**

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period ='1d',start ='2010-5-31',end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)


