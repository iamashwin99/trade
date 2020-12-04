#Auther:-@RahulGhuge
import requests
#from websocket import create_connection
from datetime import datetime
import json
import time
import pandas as pd

"""class scalpert:
    def __init__(self):
        self.session = requests.Session()
        self.headers={"Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5",
                     "Connection":"keep-alive","Content-Length":"42","Content-Type":"application/json;charset=utf-8",
                     "Host":"staging.finvasia.com:3000","Origin":"https://trade.finvasia.com","Referer":"https://trade.finvasia.com/login",
                     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
        self.enctoken=""
        self.response=""

    def login(self,email=None, password=None):
        self.session.get("https://trade.finvasia.com/")
        self.session.post("https://staging.finvasia.com:3000/get/question")
        data={"email":email,"password":password}
        self.response=self.session.post("https://staging.finvasia.com:3000/api/login",data=data)
        self.enctoken=self.response.json()["data"]['user']['token']

    def getdata(self,scripcode):
        tmstmp=str(time.time())
        tm=tmstmp[0]+tmstmp[1]+tmstmp[2]+tmstmp[3]+tmstmp[4]+tmstmp[5]+tmstmp[6]+tmstmp[7]+tmstmp[8]+tmstmp[9]+tmstmp[11]+tmstmp[12]+tmstmp[13]
        url='https://staging.finvasia.com:3000/api/ws-chart-engine/intraday/data?identifier='+scripcode+'&startdate=NaN&interval=minute&period=1&exh=NSE&extended=0&ciqrandom='+tm
        headers={'Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5',
        'Authorization':'Bearer '+self.enctoken,
        'Cache-Control':'no-cache','Connection':'keep-alive','Host':'staging.finvasia.com:3000', 'Origin':'https://trade.finvasia.com',
        'Pragma':'no-cache','Referer':'https://trade.finvasia.com/trader','TE':'Trailers','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
        return self.session.get(url,headers=headers).json()
        
    def timestamp(self):
        tmstmp=str(time.time())
        ciqrand=tmstmp[0]+tmstmp[1]+tmstmp[2]+tmstmp[3]+tmstmp[4]+tmstmp[5]+tmstmp[6]+tmstmp[7]+tmstmp[8]+tmstmp[9]+tmstmp[11]+tmstmp[12]+tmstmp[13]
        return ciqrand
    
    def placeorder(self,sym,qty,price='0.00',prctype="MKT"):
        headers1={'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Cache-Control':'no-cache','Connection':'Upgrade',
        'Host':'awspricefeed.finvasia.com','Origin':'https://trade.finvasia.com','Pragma':'no-cache',
        'Sec-WebSocket-Extensions':'permessage-deflate','Sec-WebSocket-Key':'9gyGwUX6a7fAly8Dyh6yDg==','Sec-WebSocket-Version':'13','Upgrade':'websocket',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
        ws = create_connection('wss://awspricefeed.finvasia.com/price-feed',headers=headers1)
        ws.send(json.dumps({"auth":self.enctoken,"defaults":[1,2]}))
        time.sleep(1)
        dt=datetime.utcnow().isoformat()[:-3]+'Z'
        print(ws.send(json.dumps({"orderDetail":{"exch":"NSE","symbol":sym,"date":dt,"Pcode":"MIS","Ttranstype":"B","ret":"DAY","QTY":qty,"discqty":'0',"price":price,"TrigPrice":"0.00","MktPro":0,"Prctype":prctype,"AMO":"NO"}})))

    def logs(self):
        url="https://staging.finvasia.com:3000/get/user/log/"
        headers={'Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5',
        'Authorization':'Bearer '+self.enctoken,
        'Cache-Control':'no-cache','Connection':'keep-alive','Host':'staging.finvasia.com:3000', 'Origin':'https://trade.finvasia.com',
        'Pragma':'no-cache','Referer':'https://trade.finvasia.com/trader','TE':'Trailers','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
        return self.session.post(url,headers=headers).json()
    def squareoff(sym,qty,token,Pcode="MIS",seg="NSEEQ"):
        headers1={'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Cache-Control':'no-cache','Connection':'Upgrade',
        'Host':'awspricefeed.finvasia.com','Origin':'https://trade.finvasia.com','Pragma':'no-cache',
        'Sec-WebSocket-Extensions':'permessage-deflate','Sec-WebSocket-Key':'9gyGwUX6a7fAly8Dyh6yDg==','Sec-WebSocket-Version':'13','Upgrade':'websocket',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
        ws = create_connection('wss://awspricefeed.finvasia.com/price-feed',headers=headers1)    
        time.sleep(1)
        ws.send(json.dumps({"auth":self.enctoken,"defaults":[1,2]}))
        dt=datetime.utcnow().isoformat()[:-3]+'Z'
        print(ws.send(json.dumps({squareoff: {'Pcode': "MIS", 'Netqty': qty, 'Token': token, 'Symbol': sym, 'Exchangeseg': seg}})))
"""
# from finvasia import scalpert
# trade=scalpert()
# trade.login("FA27632","Rahul@123")
# trade.getdata('236')   
class shoonya:
    def __init__(self):
        self.session = requests.Session()
        self.headers={'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5',
        'Connection':'keep-alive','Content-Length':'127','Content-Type':'application/x-www-form-urlencoded','Host':'shoonya.finvasia.com','Origin':'https://shoonya.finvasia.com',
        'Referer':'https://shoonya.finvasia.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
        self.enctoken=""
        self.response=""
        self.tokenid=""
        self.key=""
        self.cookie=""
        self.uid=""
        self.ucode=""
        
    def login(self,email=None, password=None,pan=None):
        self.session.get("https://shoonya.finvasia.com/")
        d1="{\"userName\":"+email+",\"pan\":"+pan+",\"role\":\"admin\",\"pass\":"+password+"}"
        data={d1:""}
        self.uid=email
        self.enctoken=self.session.post("https://shoonya.finvasia.com/jwt/token",headers=self.headers,data=data).text
        h=self.headers
        h.update({'Authorisation':'Token '+self.enctoken})
        self.response=self.session.post("https://shoonya.finvasia.com/trade/login",headers=h,data=data).json()
        self.key=self.response['key']
        self.tokenid=self.response['userdata']['TOKENID']
        self.cookie="JSESSIONID="+self.session.cookies.get_dict()["JSESSIONID"]["value"]
        self.pan=['userdata']["USERID"]["PANNO"]
        self.ucode=self.response['userdata']["USERID"]
    def marketwatch():
        t1="{\"token_id\":"+self.tokenid+",\"keyid\":"+self.keyid+",\"userid\":"+self.uid+"\"clienttype\":\"C\",\"usercode\":"+self.ucode+",\"pan_no\":"+self.pan+"}"
        data={t1:""}
        h={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,mr;q=0.8,hi;q=0.7","Authorisation": "Token "+self.enctoken,"Cache-Control": "no-cache","Connection": "keep-alive","Content-Length": "247",
        "Content-Type": "application/x-www-form-urlencoded","Cookie": self.cookie,"DNT": "1","Host": "shoonya.finvasia.com","Origin": "https://shoonya.finvasia.com","Pragma": "no-cache",
        "Referer": "https://shoonya.finvasia.com/","Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

        return self.session.post("https://shoonya.finvasia.com/trade/getWatchlistName",headers=h,data=data).json()
