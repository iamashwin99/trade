#Author:-Rahul Ghuge

def ma(period,pricedata):
    """
    Arg=
    period=moving average period
    pricedata= intraday data of today in dataframe
    """
    return pricedata["Close"].rolling(window=period).mean()

def ma_last(period,pricedata):
    """
    Arg=
    period=moving average period
    pricedata= intraday data of today in dataframe
    """
    temp=pricedata["Close"].rolling(window=period).mean()
    return temp.iloc[-1]

def vwap(pricedf):
    """
    Arg:-
    pricedata= intraday data of today in dataframe
    """
    pricedf["temp"]=((pricedf['Close']+pricedf['Low']+pricedf['High'])/3)*pricedf['Volume']
    pricedf['vwap']=pricedf["temp"].cumsum()/pricedf['Volume'].cumsum()
    pricedf.drop('temp', inplace=True, axis=1)
    return pricedf

def vwap_last(pricedf):
    """
    Arg:-
    pricedata= intraday data of today in dataframe
    """
    pricedf["temp"]=((pricedf['Close']+pricedf['Low']+pricedf['High'])/3)*pricedf['Volume']
    pricedf['vwap']=pricedf["temp"].cumsum()/pricedf['Volume'].cumsum()
    pricedf.drop('temp', inplace=True, axis=1)
    return pricedf['vwap'].iloc[-1]
