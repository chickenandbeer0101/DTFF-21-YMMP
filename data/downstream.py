# downstream.py
from data.connect import *
import pandas as pd

def get_crypto_data(crypto_symbol="BTC", start_dt="1960", end_dt="2020"):
   
    sql = "SELECT id FROM coins WHERE symbol='"+crypto_symbol+"'"
    coin_id = pd.read_sql_query(sql, engine)

    sql = "SELECT * FROM historical WHERE coin_id="+ str(coin_id.id[0]) +" LIMIT 100"
    data = pd.read_sql_query(sql, engine)
    
    return data