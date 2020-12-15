
from api5paisa import Api5Paisa
from time import sleep
import pandas as pd

api = Api5Paisa()
api.login("8055426572", "Kapil@123","22111994")

scrcode=['15083',]

def getdata(Etyp,scrip):
    return api.post('/Trade/Chart/FetchQuoteData',{"Exch": "N","ExchType": Etyp,"LastRequestTime": "1TODAY","ScripCode": scrip})

def ma(period,pricedata):
    return pricedata["Close"].rolling(window=period).mean()

def ma_last(period,pricedata):
    temp=pricedata["Close"].rolling(window=period).mean()
    return temp.iloc[-1]

def vwap(pricedf):
    pricedf['vwap']=(((pricedf['Close']+pricedf['Low']+pricedf['High'])/3)*pricedf['Volume']).cumsum())/pricedf['Volume'].cumsum()
    return pricedf['vwap'].iloc[-1]

def vwap_signal(dfc-2,dfv-2,dfc-1,dfv-1):
    if 
    
    
    
