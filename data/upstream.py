# upstream.py
import pandas as pd
import quandl

from connect import DATAPATH

quandl.ApiConfig.api_key = os.environ.get("QUANDL_API_KEY")

def put_fx_data():
  """Store FX data to the DB."""

  data = quandl.get_table('FXCM/H1', date='2021-01-01', symbol='EUR/CAD')

  filename = DATAPATH + "eurcad-hf-data.ftr"

  data.to_feather(filename)