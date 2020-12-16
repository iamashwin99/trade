from trade.study import *


def trade_on_vwap(dfdata):
    vwap_value=vwap_last(dfdata)
    if vwap_value>dfdata["Close"].iloc[-1] and vwap_value>dfdata["Open"].iloc[-1]:
       return "B"
    if vwap_value<dfdata["Close"].iloc[-1] and vwap_value<dfdata["Open"].iloc[-1]:
       return "S"
    else:
        print("No Signal Generated")
