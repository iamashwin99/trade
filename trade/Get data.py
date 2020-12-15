#Author:-Rahul Ghuge

from time import sleep
import pandas as pd




def ma(period,pricedata):
    return pricedata["Close"].rolling(window=period).mean()

def ma_last(period,pricedata):
    temp=pricedata["Close"].rolling(window=period).mean()
    return temp.iloc[-1]

def vwap(pricedf):
    pricedf['vwap']=(((pricedf['Close']+pricedf['Low']+pricedf['High'])/3)*pricedf['Volume']).cumsum())/pricedf['Volume'].cumsum()
    return pricedf['vwap'].iloc[-1]


    
    
