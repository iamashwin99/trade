def stop_loss_hit(ltp,sl,bs="B"):
    """
    :param ltp=last price of current position
    :param sl=stop loss defined by system for current position
              which can be varried by system
    :param bs=is open position is long or short. 'B' for long,'S' short.
    """
    if bs=='B' and ltp<=sl:
       return "slhit"
    elif bs=='B' and ltp>sl:
       return "slnothit"
    
    if bs=='S' and ltp>=sl:
       return "slhit"
    elif bs=='S' and ltp<sl:
       return "slnothit"
def sl_modify(abs_sl,sl,ltp,bs_price):
    """
    :param sl=stop loss defined by system.
    :param ltp=ltp of open instrument.
    :param bs_price=buy or sell price of open instrument.
    :param abs_sl=sl at the time of buy.
    """
    if (ltp-sl)>abs_sl:
       sl=ltp-abs_sl
       return sl
