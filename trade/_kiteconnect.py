import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

S=requests.session()
#ent=0
#    for token in mkt['data']:
#	tokens.update[{t['data'][ent]['tradingsymbol']:t['data'][ent]['instrument_token']}]
#	ent=ent+1
symbols=['IBULHSGFIN','AUROPHARMA','ADANIGREEN','CUMMINSIND','INDHOTEL','CHOLAFIN','FORTIS','COROMANDEL','M&MFIN','CADILAHC','NAUKRI','AARTIIND','SHREECEM','TORNTPHARM','ADANITRANS','BALKRISIND','GRASIM','ADANIGAS','HINDZINC',
'PAGEIND','BATAINDIA','SRF','SUNPHARMA','BIOCON','ABCAPITAL','ASHOKLEY','JUBLFOOD','SIEMENS','ITC','BAJAJHLDNG','INFRATEL','COFORGE','EDELWEISS','ADANIENT','BHEL','APOLLOTYRE','MANAPPURAM','EMAMILTD','GLENMARK','L&TFH','OIL',
'RAMCOCEM','NAM-INDIA','VGUARD','PETRONET','GSPL','LTTS','TATACHEM','EICHERMOT','HDFCLIFE','IPCALAB','DALBHARAT','HINDUNILVR','JSWENERGY','MGL','ZEEL','DABUR','HINDALCO','SAIL','CIPLA','TATAMOTORS','GICRE','ESCORTS','NMDC','MRF',
'UBL','PEL','NAVINFLUOR','TECHM','SYNGENE','CROMPTON','DIVISLAB','LUPIN','MOTHERSUMI','GAIL','BAJAJFINSV','IDEA','HEROMOTOCO','TITAN','LT','EXIDEIND','PRESTIGE','APLLTD','INDIGO','TATACONSUM','MINDTREE','SANOFI','HUDCO','ENDURANCE',
'IRCTC','OFSS','TVSMOTOR','GMRINFRA','SUNTV','BAJFINANCE','BRITANNIA','MUTHOOTFIN','PNB','M&M','ISEC','BHARTIARTL','AMBUJACEM','COLPAL','BAJAJ-AUTO','LTI','AMARAJABAT','GODREJAGRO','FRETAIL','CASTROLIND','HDFCAMC','RBLBANK','NATCOPHARM',
'ACC','NESTLEIND','ICICIPRULI','PIDILITIND','ULTRACEMCO','GODREJPROP','HINDPETRO','RELIANCE','ALKEM','CONCOR','IDFCFIRSTB','IOC','BERGEPAINT','UNIONBANK','BEL','LALPATHLAB','WIPRO','BANDHANBNK','HCLTECH','GODREJIND','HAVELLS','AUBANK',
'SBILIFE','BHARATFORG','MFSL','BPCL','TORNTPOWER','ABFRL','DRREDDY','POWERGRID','MARUTI','PIIND','INFY','NATIONALUM','HDFCBANK','ASIANPAINT','ADANIPORTS','DMART','ICICIGI','GODREJCP','PFC','TATASTEEL','GUJGASLTD','BANKINDIA','TCS',
'DLF','ABBOTINDIA','FEDERALBNK','AJANTPHARM','JINDALSTEL','CESC','MARICO','HDFC','POLYCAB','NTPC','UPL','PFIZER','CUB','VOLTAS','JSWSTEEL','AXISBANK','RECLTD','ONGC','PGHH','TATAPOWER','WHIRLPOOL','VBL','MCDOWELL-N','IGL','INDUSINDBK',
'SBIN','ICICIBANK','COALINDIA','YESBANK','SBICARD','CANBK','BANKBARODA','BOSCHLTD','KOTAKBANK','LICHSGFIN','APOLLOHOSP','SRTRANSFIN']

options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')
referer="https://kite.zerodha.com/static/build/chart.html?v=2.6.1"
method="get"
path=""
driver = webdriver.Chrome(options=options)
driver.maximize_window()
  
def login():
    if driver.current_url!="https://kite.zerodha.com/":
       driver.get("https://kite.zerodha.com/")
    
    driver.find_element(By.ID, "userid").click()
    driver.find_element(By.ID, "userid").send_keys("YF6709")
    driver.find_element(By.ID, "password").send_keys("Rahul@123")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.CSS_SELECTOR, ".button-orange").click()
    time.sleep(3)
    driver.find_element(By.ID, "pin").send_keys("159753")
    driver.find_element(By.ID, "pin").send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, ".button-orange").click()

def orderbook(S=S):
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/orders"
    return S.get("https://kite.zerodha.com/oms/orders",headers=head).json()

def marketwatch(S=S):
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/api/marketwatch"
    headers1={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0","x-csrftoken":pubtoken,'x-kite-version': '2.6.2'}
    mkt=S.get("https://kite.zerodha.com/api/marketwatch",headers=headers1).json()
    return mkt

def position(S=S):
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/portfolio/positions"
    headers1={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-version': '2.6.2'}
    return S.get("https://kite.zerodha.com/oms/portfolio/positions",headers=headers1).json

def fund(S=S):
    referer="https://kite.zerodha.com/dashboard"
    method="get"
    path="/oms/user/margins"
    headers1={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",'x-kite-version': '2.6.2'}
    return S.get("https://kite.zerodha.com/oms/user/margins",headers=headers1).json()

def plceorder(price,quantity,symbol):
    referer="https://kite.zerodha.com/dashboard"
    method="post"
    path="/oms/order/regular"
    headers1={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,"Connection":"keep-alive",
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
    headers1={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,"Connection":"keep-alive",
              "Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest":"empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
    
    url='https://kite.zerodha.com/oms/instruments/historical/'+token+"/minute?user_id=YF6709&oi=1&from="+frdate+'&to='+todate+"&&ciqrandom="+timestamp()
    print(url)
    return S.get(url,headers=headers1).json()    
login()
time.sleep(3)
try:    
    cookie="__cfduid="+driver.get_cookies()[4]['value']+"; kf_session="+driver.get_cookies()[3]['value']+"; public_token="+driver.get_cookies()[2]['value']+"; user_id=YF6709"+"; enctoken="+driver.get_cookies()[1]['value']
except:
    print("error")

enctoken="enctoken "+driver.get_cookies()[1]['value']
pubtoken=driver.get_cookies()[2]['value']

head={"authority": "kite.zerodha.com","method": method,"path": path,"scheme": "https","Accept":"*/*","Accept-Encoding":"utf-8","Accept-Language":"en-US,en;q=0.5","authorization":enctoken,
      "Connection":"keep-alive","Cookie":cookie,"Host":"kite.zerodha.com","Referer":referer,"sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin",
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
