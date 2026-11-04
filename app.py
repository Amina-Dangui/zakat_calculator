import streamlit as st
import requests
st.title('Zakat calculator')
cash=st.number_input('Cash you have on you or at home ')
bank=st.number_input('Money in your bank accounts')
gold_grams=st.number_input('Gold you own (in grams)')
debts=st.number_input('Debts you must pay soon ')
@st.cache_data(ttl=86400)
def get_gold_price():
  key=st.secrets['METALS_API_KEY']
  url='https://api.metals.dev/v1/latest?api_key=' + key + '&currency=EUR&unit=g'
  response=requests.get(url)
  data=response.json()
  return data['metals'] ['gold']
gold_price=get_gold_price()
st.write('Price of 1 gram of gold today:',gold_price,'EUR')
  
