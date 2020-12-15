import requests
#from websocket import create_connection
from datetime import datetime
import json
import time
import pandas as pd

s=requests.session()

def login(email, password,pan):
    headers={'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5',
        'Connection':'keep-alive','Content-Length':'127','Content-Type':'application/x-www-form-urlencoded','Host':'shoonya.finvasia.com','Origin':'https://shoonya.finvasia.com',
        'Referer':'https://shoonya.finvasia.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
    s.get("https://shoonya.finvasia.com/")
    d1={"userName":email,"pan":pan,"role":"admin","pass": password}
    data={str(d1):""}
    global enctoken
    enctoken=s.post("https://shoonya.finvasia.com/jwt/token",headers=headers,data=data).text
    h=headers
    h.update({'Authorisation':'Token '+enctoken})
    response=s.post("https://shoonya.finvasia.com/trade/login",headers=h,data=data)
    global cookie
    cookie=response.headers['Set-Cookie'].replace("; Path=/; HttpOnly","")
    global tokenid
    global key
    tokenid=response.json()["userdata"]["TOKENID"]
    key=response.json()["key"]

def fund():
    temp={"token_id":tokenid,"keyid":key,"userid":"FA27632","clienttype":"C","usercode":"13549","pan_no":"CJEPG1375B"}
    data={str(temp):""}
    headers={"Host": "shoonya.finvasia.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "249",
    "Referer": "https://shoonya.finvasia.com/",
    "Origin": "https://shoonya.finvasia.com",
    "Connection": "keep-alive",
    "Cookie": cookie, "Authorisation":"Token "+enctoken} 
    global balance
    acbalance=s.post("https://shoonya.finvasia.com/trade/getLimits",headers=headers,data=data).json()
    balance=float(acbalance[0]['AVAILABLE_BALANCE'])
    return acbalance

def orderbook():
    temp={"row_1":"","row_2":"","exch":"","seg":"","product":"","status":"","inst":"","symbol":"","str_price":"","place_by":"","opt_type":"","exp_dt":"","token_id":tokenid,"keyid":key,"userid":"FA27632","clienttype":"C","usercode":"13549","pan_no":"CJEPG1375B"}
    data={str(temp):""}
    headers={"Host": "shoonya.finvasia.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "536",
    "Referer": "https://shoonya.finvasia.com/",
    "Origin": "https://shoonya.finvasia.com",
    "Connection": "keep-alive",
    "Cookie": cookie, "Authorisation":"Token "+enctoken} 
    return s.post("https://shoonya.finvasia.com/trade/getOrderbook",headers=headers,data=data).json()

def position():
    temp={"row_1":"","row_2":"","exch":"","seg":"","product":"","v_mode":"","status":"","Inst":"","symbol":"","str_price":"","place_by":"","opt_type":"","exp_dt":"","token_id":tokenid,"keyid":key,"userid":"FA27632","clienttype":"C","usercode":"13549","pan_no":"CJEPG1375B"}
    data={str(temp):""}
    headers={"Host": "shoonya.finvasia.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "560",
    "Referer": "https://shoonya.finvasia.com/",
    "Origin": "https://shoonya.finvasia.com",
    "Connection": "keep-alive",
    "Cookie": cookie, "Authorisation":"Token "+enctoken} 
    return s.post("https://shoonya.finvasia.com/trade/getNetposition",headers=headers,data=data).json()

def order(price,qty,secid):
    temp={"qty":qty,"price":price,"odr_type":"LMT","product_typ":"I","trg_prc":0,"validity":"DAY","disc_qty":0,"amo":False,"sec_id":"17963","inst_type":"EQUITY","exch":"NSE","buysell":"B","gtdDate":"0000-00-00","mktProtectionFlag":"N","mktProtectionVal":0,"settler":"000000000000","token_id":tokenid,"keyid":key,"userid":"FA27632","clienttype":"C","usercode":"13549","pan_no":"CJEPG1375B"}
    data={str(temp):""}
    headers={"Host": "shoonya.finvasia.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "560",
    "Referer": "https://shoonya.finvasia.com/",
    "Origin": "https://shoonya.finvasia.com",
    "Connection": "keep-alive",
    "Cookie": cookie, "Authorisation":"Token "+enctoken}
    return s.post("https://shoonya.finvasia.com/trade/placeorder",headers=headers,data=data).json()

def getdata(secid,fdt=1,tdt=1,S=s):
    headers={'Host': 'shoonyabrd.finvasia.com',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Accept": "*/*","Accept-Encoding": "utf-8","Accept-Language": "en-USen;q=0.5",
    "Content-Length": "197",
    'Origin': 'https://shoonyabrd.finvasia.com',
    'Connection': 'keep-alive',
    'Referer': 'https://shoonyabrd.finvasia.com/Charts/chartw.html'}
    temp={"Exch":"NSE","Seg":"E","ScripId":secid,"FromDate":fdt,"ToDate":tdt,"Time":1}
    data={"Count": 10,"Data": str(temp),"DoCompress": False,
    "RequestCode": 800,"Reserved": "","Source": "W","UserId": "FA27632"}
    t=timestamp()
    return S.post("https://shoonyabrd.finvasia.com/TickPub/api/Tick/LiveFeed?ciqrandom="+t,headers=headers,data=data).json()

def timestamp():
    tmstmp=str(time.time())
    ciqrand=tmstmp[0]+tmstmp[1]+tmstmp[2]+tmstmp[3]+tmstmp[4]+tmstmp[5]+tmstmp[6]+tmstmp[7]+tmstmp[8]+tmstmp[9]+tmstmp[11]+tmstmp[12]+tmstmp[13]
    return ciqrand
