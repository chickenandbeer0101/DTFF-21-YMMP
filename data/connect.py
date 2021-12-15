# connect.py
import os
import sqlalchemy
import pymysql

#notes install local sql server (server only) for testing purposes
##https://ladvien.com/data-analytics-mysql-localhost-setup/

##mysql database create from sqlight data set from https://www.kaggle.com/bizzyvinci/coinmarketcap-historical-data

#DATAPATH = os.environ.get("RESEARCH_DATA_PATH")
dialect = "mysql"
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
db_name = "db_test"
host = "localhost"
port = 3306

engine = f"{dialect}+pymysql://{username}:{password}@{host}:{port}/{db_name}"



