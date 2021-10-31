# downstream.py
import pandas as pd
from connect import DATAPATH

def get_fx_data(subset, start_dt="1960", end_dt="2020"):
  """Get FX data from the DB."""
  filename = DATAPATH + "fx-data-1980-2020-d.ftr"

  data = pd.read_ftr(filename)

  return data