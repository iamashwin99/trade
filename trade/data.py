from requests import session
import time
import pandas as pd
s=session()
def timestamp():
    tmstmp=str(time.time())
    ciqrand=tmstmp[0]+tmstmp[1]+tmstmp[2]+tmstmp[3]+tmstmp[4]+tmstmp[5]+tmstmp[6]+tmstmp[7]+tmstmp[8]+tmstmp[9]+tmstmp[11]+tmstmp[12]+tmstmp[13]
    return ciqrand
def data(secid,fdt=1,tdt=1):
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
    return pd.DataFrame(s.post("https://shoonyabrd.finvasia.com/TickPub/api/Tick/LiveFeed?ciqrandom="+t,headers=headers,data=data).json())
