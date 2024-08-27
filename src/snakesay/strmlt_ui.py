import streamlit as st
import pandas as pd
import numpy as np

import sys
import requests 
import linecache
import json

import plotly.express as px

#################################
# DEFINE ALL FUNCTIONS
#################################

def Process_File(start_num, end_num, fapi_server) -> pd.DataFrame:
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
      response = requests.post('http://'+fapi_server+':8002/callproducer', json=myjson)
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

def fetch_data(fapi_server) -> pd.DataFrame:
  df = pd.DataFrame()
  response = requests.post('http://'+fapi_server+':8002/get_fetch_data')
  print("GET FETCH DATA Response Code")
  print(response.status_code)
  data_str = response.json()
  data_dict = json.loads(data_str)
  df = pd.DataFrame()
  for k1, v1 in data_dict.items():
     df = pd.concat([df, pd.DataFrame([v1])], ignore_index=True)
  return df

#################################
# STREAMLIT DEFINITIONS
#################################

st.set_page_config(page_title="FILE ANALYZER APP", page_icon=":bar_chart:", layout="wide")
st.title(" :pushpin: JSON FILE ANALYZER APP")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>",unsafe_allow_html=True)
st.write("WELCOME to FILE ANALYZER APP")
# FOR FUTURE USE
fl = st.file_uploader(":file_folder: upload a file", type=(["json"]))
if fl is not None:
   filename = fl.name
   st.write(filename)
   # Load file to ./DATA FOLDER code
else:
   st.write("USING DEFAULT FILE")

#++++++++++++++++++++++++++++++++
# VARIABLES
#++++++++++++++++++++++++++++++++
fapi_server='172.17.0.1'

#++++++++++++++++++++++++++++++++
# LOAD DATA
#++++++++++++++++++++++++++++++++
load = st.button ('LOAD DATA in DB')
fetch = st.button ('FETCH DATA from DB')

# INITIALIZE SESSION STATE
if "load_state" not in st.session_state:
   st.session_state.load_state = False
if load or st.session_state.load_state:
   st.session_state.load_state = True
   st.markdown('## NUMBER OF LINE TO READ')
   start_num = st.number_input('start_line',min_value=1, max_value=10)
   end_num = st.number_input('end_line',min_value=1, max_value=10)
   dfdf1 = Process_File(start_num, end_num, fapi_server)
   st.dataframe(dfdf1)

#++++++++++++++++++++++++++++++++
# FETCH DATA from DB
#++++++++++++++++++++++++++++++++

# INITIALIZE SESSION STATE
if "fetch_state" not in st.session_state:
   st.session_state.fetch_state = False
if fetch or st.session_state.fetch_state:
   st.session_state.fetch_state = True
   st.markdown('## FETCH FROM DB')
   dfdf2 = fetch_data(fapi_server)
   dfdf2['PATH_SHORT'] = dfdf2['PATH'].str[:8]
   dfdf5 = dfdf2.head(5)
   st.dataframe(dfdf5)
   #++++++++++++++++++++++++++++++++
   # FILTER with SIDEBAR
   #++++++++++++++++++++++++++++++++
   # SIDEBAR for FILTER
   st.sidebar.header("CHOOSE FILTER: ")
   FILTER1='MSG_DIR'
   FILTER2='METHOD'
   #filter = st.sidebar.multiselect("PICK FILTER", ['FILTER1', 'FILTER2'])
   # FILTER1
   f1 = st.sidebar.multiselect("PICK FILTER1", dfdf2[FILTER1].unique())
   if not f1:
      dfdf10 = dfdf2.copy()
   else:
     dfdf10 = dfdf2[dfdf2[FILTER1].isin(f1)]
   # FILTER2
   f2 = st.sidebar.multiselect("PICK FILTER2", dfdf2[FILTER2].unique())
   if not f2:
      dfdf11 = dfdf10.copy()
   else:
      dfdf11 = dfdf10[dfdf10[FILTER2].isin(f2)]
   # IF FILTER1 & FILTER2 are not selected
   if f1 and f2:
      filter_df = dfdf11.copy()
   elif f2:
      filter_df = dfdf11.copy()
   elif f1:
      filter_df = dfdf11.copy()
   else:
      filter_df = dfdf2.copy()
   # If multiple filter
   # check --> https://www.youtube.com/watch?v=7yAw1nPareM

   #++++++++++++++++++++++++++++++++
   # PLOTTING
   #++++++++++++++++++++++++++++++++
   # PLOTTING
   col1, col2 = st.columns((2))
   CATEGORY1='PATH_SHORT'
   CATEGORY2='AUTHORITY'
   CATEGORY11='PATH'
   category_df1 = filter_df.groupby(by = [CATEGORY1], as_index = False)[CATEGORY11].count()
   category_df2 = filter_df.groupby(by = [CATEGORY2], as_index = False)[CATEGORY11].count()
   #st.dataframe(category_df)
   with col1:
      st.subheader("PATH count")
      fig = px.bar(category_df1, x = CATEGORY1, y = "PATH", text = ['{:,.2f}'.format(x) for x in category_df1[CATEGORY11]],
                 template = "seaborn")
      st.plotly_chart(fig,use_container_width=True, height = 200)
   with col2:
      st.subheader("AUTHORITY CATEGORY")
      fig = px.bar(category_df2, x = CATEGORY2, y = "PATH", text = ['{:,.2f}'.format(x) for x in category_df2[CATEGORY11]],
                 template = "seaborn")
      st.plotly_chart(fig,use_container_width=True, height = 200)
  #  with col2:
  #     st.subheader("AUTHORITY wise CATEGORY")
  #     fig = px.pie(filter_df, values = CATEGORY11, names = CATEGORY2, hole = 0.5)
  #     fig.update_traces(text = filter_df[CATEGORY2], textposition = "outside")
  #     st.plotly_chart(fig,use_container_width=True, height = 200)