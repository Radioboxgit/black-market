# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:29:27 2022

@author: Chinedu
"""
#importing the necessary libs
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date
import json
from datetime import date


#declaring the url
URL = 'https://nairablackmarket.com/page/Black-market-exchange%20rates'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
print('running...')
response = requests.get(URL, headers=header)

df_list = pd.read_html(response.text)
'''
check for the latest Update:
remove rows that contains only NaN values in all columns of dataframe

'''

def process_table(dataframe_object):
  
  dataframe_object.dropna(axis = 0, how = 'all',inplace=True)

  # #replace '"' with P2P and label NA columns with immediate ones above it

  dataframe_object[4].replace('"','P2P',inplace=True)

  dataframe_object.fillna(method='ffill',inplace=True) 

  dataframe_object.replace('**','N/A',inplace=True)

  dataframe_object.replace('Lagos Aboki/BDC','Aboki Rate',inplace=True)

  dataframe_object.replace('Inflow/Bank Transfer Rates','BDC_Inflow_Bank_Transfer_Rates',inplace=True)

  dataframe_object[1]=df_list[0][1].str.rstrip('**')

  dataframe_object[2]=df_list[0][2].str.rstrip('**')


  list_d=dataframe_object.values.tolist()

  tickers=['USD','EUR','GBP']

  list_d=[sub for sub in list_d if sub[0] in tickers]

  black_markets=[{'ticker':b[0],'buyRates':b[1],'sellRates':b[2],'source':b[-1]} for b in list_d]
  return black_markets


print(len(df_list))


today = date.today().strftime("%d/%m/%Y")
market_period={'Morning':0, 'Afternoon':1,'Evening':2}
black_markets={'Date':today}

# get all the amrket period tickers
for key,value in market_period.items():
  try:
    black_markets[key]=process_table(df_list[value])
  except:
    print('market for time duration {}'.format(key))

print(black_markets)

file_dump=json.dumps(black_markets)
