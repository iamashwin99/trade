import requests
#from websocket import create_connection
from datetime import datetime
import json
import time
import pandas as pd

s=requests.session()
response=""
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
    tokenid=response()["userdata"]["TOKENID"]
    key=response()["key"]

def fund(tokenid,key):
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
    return s.post("https://shoonya.finvasia.com/trade/getLimits",headers=headers,data=data).json()
