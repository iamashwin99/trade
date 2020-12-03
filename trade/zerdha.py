import time
import json
import datetime as dt
import requests
      
s=requests.session()

symbols=['IBULHSGFIN','AUROPHARMA','ADANIGREEN','CUMMINSIND','INDHOTEL','CHOLAFIN','FORTIS','COROMANDEL','M&MFIN','CADILAHC','NAUKRI','AARTIIND','SHREECEM','TORNTPHARM','ADANITRANS','BALKRISIND','GRASIM','ADANIGAS','HINDZINC',
         'PAGEIND','BATAINDIA','SRF','SUNPHARMA','BIOCON','ABCAPITAL','ASHOKLEY','JUBLFOOD','SIEMENS','ITC','BAJAJHLDNG','INFRATEL','COFORGE','EDELWEISS','ADANIENT','BHEL','APOLLOTYRE','MANAPPURAM','EMAMILTD','GLENMARK','L&TFH','OIL',
         'RAMCOCEM','NAM-INDIA','VGUARD','PETRONET','GSPL','LTTS','TATACHEM','EICHERMOT','HDFCLIFE','IPCALAB','DALBHARAT','HINDUNILVR','JSWENERGY','MGL','ZEEL','DABUR','HINDALCO','SAIL','CIPLA','TATAMOTORS','GICRE','ESCORTS','NMDC','MRF',
         'UBL','PEL','NAVINFLUOR','TECHM','SYNGENE','CROMPTON','DIVISLAB','LUPIN','MOTHERSUMI','GAIL','BAJAJFINSV','IDEA','HEROMOTOCO','TITAN','LT','EXIDEIND','PRESTIGE','APLLTD','INDIGO','TATACONSUM','MINDTREE','SANOFI','HUDCO','ENDURANCE',
         'IRCTC','OFSS','TVSMOTOR','GMRINFRA','SUNTV','BAJFINANCE','BRITANNIA','MUTHOOTFIN','PNB','M&M','ISEC','BHARTIARTL','AMBUJACEM','COLPAL','BAJAJ-AUTO','LTI','AMARAJABAT','GODREJAGRO','FRETAIL','CASTROLIND','HDFCAMC','RBLBANK','NATCOPHARM',
         'ACC','NESTLEIND','ICICIPRULI','PIDILITIND','ULTRACEMCO','GODREJPROP','HINDPETRO','RELIANCE','ALKEM','CONCOR','IDFCFIRSTB','IOC','BERGEPAINT','UNIONBANK','BEL','LALPATHLAB','WIPRO','BANDHANBNK','HCLTECH','GODREJIND','HAVELLS','AUBANK',
         'SBILIFE','BHARATFORG','MFSL','BPCL','TORNTPOWER','ABFRL','DRREDDY','POWERGRID','MARUTI','PIIND','INFY','NATIONALUM','HDFCBANK','ASIANPAINT','ADANIPORTS','DMART','ICICIGI','GODREJCP','PFC','TATASTEEL','GUJGASLTD','BANKINDIA','TCS',
         'DLF','ABBOTINDIA','FEDERALBNK','AJANTPHARM','JINDALSTEL','CESC','MARICO','HDFC','POLYCAB','NTPC','UPL','PFIZER','CUB','VOLTAS','JSWSTEEL','AXISBANK','RECLTD','ONGC','PGHH','TATAPOWER','WHIRLPOOL','VBL','MCDOWELL-N','IGL','INDUSINDBK',
         'SBIN','ICICIBANK','COALINDIA','YESBANK','SBICARD','CANBK','BANKBARODA','BOSCHLTD','KOTAKBANK','LICHSGFIN','APOLLOHOSP','SRTRANSFIN']
res=""
resp1=""
referer="https://kite.zerodha.com/static/build/chart.html?v=2.6.1"
method="get"
path=""
enctoken=""
cookie=""

def login(uid,pw,twofa):
    s.get("https://kite.zerodha.com")
    try:
        global cookie
        cookie="__cfduid="+s.cookies.get_dict()["__cfduid"]+"; kf_session="+s.cookies.get_dict()["kf_session"]
    except:
        print("error in getting cookies")
    h={"Host": "kite.zerodha.com","cache-control": "max-age=0","save-data": "on","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
      "sec-fetch-mode":"navigate","sec-fetch-user": "?1","dnt": "1","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","sec-fetch-site": "none",
      "accept-encoding": "utf-8","accept-language": "en-US,en;q=0.9,mr;q=0.8,hi;q=0.7","cookie":cookie}
    res=s.post("https://kite.zerodha.com/api/login",headers=h,data={"user_id":uid,"password":pw})
    h1={"Authority": "kite.zerodha.com","method": "POST","path": "/api/twofa","scheme": "https","accept": "application/json, text/plain, */*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,mr;q=0.8,hi;q=0.7",
    "cache-control": "no-cache","content-length": "109","content-type": "application/x-www-form-urlencoded","cookie":cookie,"dnt": "1","origin": "https://kite.zerodha.com","pragma": "no-cache","referer": "https://kite.zerodha.com/",
    "sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36","x-csrftoken": "jDFGuxgIODRRA26hsMYXr203zdckPO8X","x-kite-userid": "YF6709","x-kite-version": "2.6.3"}
    res1=s.post("https://kite.zerodha.com/api/twofa",headers=h1,data={"user_id":uid,"request_id":res.json()["data"]["request_id"],"twofa_value":twofa})
    print(res1.text)
    try:
        cookie="__cfduid="+s.cookies.get_dict()["__cfduid"]+"; kf_session="+s.cookies.get_dict()["kf_session"]+"; public_token="+s.cookies.get_dict()["public_token"]+"; user_id=YF6709"+"; enctoken="+self.enctoken
    except:
        print("error in getting cookies")
    global enctoken
    enctoken=s.cookies.get_dict()["enctoken"]
    global pubtoken
    pubtoken=s.cookies.get_dict()["public_token"]

def orderbook():
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/orders"
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
    "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-version': '2.6.2'}
    return s.get("https://kite.zerodha.com/oms/orders",headers=headers1).json()
def marketwatch():
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/api/marketwatch"
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0","x-csrftoken":pubtoken,'x-kite-version': '2.6.2'}
    mkt=s.get("https://kite.zerodha.com/api/marketwatch",headers=headers1).json()
    return mkt

def position():
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/portfolio/positions"
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
    "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-version': '2.6.2'}
    return s.get("https://kite.zerodha.com/oms/portfolio/positions",headers=headers1).json()

def fund():
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/user/margins"
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
    "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-version': '2.6.2'}
    return S.get("https://kite.zerodha.com/oms/user/margins",headers=headers1).json()

def plceorder(price,quantity,symbol):
    referer="https://kite.zerodha.com/dashboard"
    method="post"
    path="/oms/order/regular"
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-userid': 'YF6709','x-kite-version': '2.6.2'}

    data={"variety": 'regular','exchange': 'NSE','tradingsymbol': symbol,'transaction_type': 'BUY','order_type': "LIMIT",'quantity': quantity,'price': price,'product': 'MIS','validity': 'DAY','disclosed_quantity': '0',
          'trigger_price': '0','squareoff': '0','stoploss': '0','trailing_stoploss': '0','user_id': 'YF6709'}
    return S.post("https://kite.zerodha.com/oms/orders/regular",headers=headers1,data=data).json()

def timestamp():
        tmstmp=str(time.time())
        ciqrand=tmstmp[0]+tmstmp[1]+tmstmp[2]+tmstmp[3]+tmstmp[4]+tmstmp[5]+tmstmp[6]+tmstmp[7]+tmstmp[8]+tmstmp[9]+tmstmp[11]+tmstmp[12]+tmstmp[13]
        return ciqrand

def getdata(token,frdate,todate):
    referer="https://kite.zerodha.com/static/build/chart.html?v=2.6.2"
    method="get"
    path='/oms/instruments/historical/'+token+"/minute?user_id=YF6709&oi=1&from="+frdate+'to='+todate+"&ciqrandom="+timestamp()
    headers1={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","Authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
    
    url='https://kite.zerodha.com/oms/instruments/historical/'+token+"/minute?user_id=YF6709&oi=1&from="+frdate+'&to='+todate+"&&ciqrandom="+timestamp()
    print(url)
    return S.get(url,headers=headers1).json()

headers={"Authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,
      "Connection":"keep-alive","Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
