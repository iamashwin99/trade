def stop-loss(ltp,sl,bs="B"):
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
