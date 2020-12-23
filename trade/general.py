def check_position(pos):
    """
    :param pos= list of position closed or open.
    """
    if not pos:
          return "no active position"
    try:
       for i in pos:  
           if i['NET_QTY']==0:
               return i["SECURITY_ID"]
           else:
              return "no active position"
