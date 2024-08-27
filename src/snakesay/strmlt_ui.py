import streamlit as st
import pandas as pd
import numpy as np

import sys
import requests 
import linecache
import json

st.title("FILE ANALYZER APP")
st.write("WELCOME to FILE ANALYZER APP")


st.markdown('## NUMBER OF LINE TO READ')
start_num = st.number_input('start_line',min_value=1, max_value=10)
end_num = st.number_input('end_line',min_value=1, max_value=10)

def Process_File(start_num, end_num) -> pd.DataFrame:
  start = int(start_num)
  end = int(end_num)
  # Loop over the JSON file
  i=start
  df = pd.DataFrame()
  while i <= end:
      # read a specific line
      line = linecache.getline('./DATA/SCP_TRAFFIC_FEED.txt', i)
      #print(line)
      # write the line to the API
      myjson = json.loads(line)
      response = requests.post('http://localhost:8002/callproducer', json=myjson)
      # Use this for dedbugging
      #print("Status code: ", response.status_code)
      #print("Printing Entire Post Request")
      print(response.json())
      print(response.status_code)
      data_str = response.json()
      data_dict = json.loads(data_str)
      df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)
      # increase i
      i+=1
  #print(df)
  return df
dfdf = Process_File(start_num, end_num)
st.dataframe(dfdf)
