# downstream.py
from data.connect import *

from datetime import datetime as dt
import pandas as pd
import requests
import json
import time

def get_crypto_data_USD_sql(crypto_symbol="BTC", start_dt="1960", end_dt="2020"):
   
    sql = "SELECT id FROM coins WHERE symbol='"+crypto_symbol+"'"
    coin_id = pd.read_sql_query(sql, engine)

    sql = "SELECT * FROM historical WHERE coin_id="+ str(coin_id.id[0]) +" LIMIT 100"
    data = pd.read_sql_query(sql, engine)
    
    return data



def get_crypto_data_binance(symbol="BTCUSDT", startTime="21-6-15"): 

    #calculate unix time
    d = dt.strptime(startTime, '%y-%m-%d')
    unixtime = int(time.mktime(d.timetuple())*1000) ##unix time in miliseconds
    
    #conduct query
    query = {'symbol':symbol, 'interval':'1d', 'startTime': int(unixtime), 'limit': '75'}
    response = requests.get('https://api.binance.com/api/v3/klines', params=query)

    #store values as a pandas df
    json_data = response.json()
    df = pd.DataFrame.from_dict(json_data)

    #clean data
    df = df.rename(columns={0: "date", 1: "open", 2: "high", 3: "low", 4: "close"}) #rename columns of df
    df['datetime']=df['date'].apply(lambda x: dt.utcfromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))  #convert unix to datetime
    df_output=df[['date', 'datetime', 'open','high','low','close']] #rearange can keep relevant data

    return df_output