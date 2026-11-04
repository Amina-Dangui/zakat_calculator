import streamlit as st
import requests
st.title('Zakat calculator')
currency=st.selectbox('Choose your currency',['EUR','USD','XOF','MAD'])
cash=st.number_input('Cash you have on you or at home ')
bank=st.number_input('Money in your bank accounts')
gold_grams=st.number_input('Gold you own (in grams)')
silver_grams=st.number_input('Silver you own (in grams)')
business_goods=st.number_input('Value of business goods/inventory')
stocks_value=st.number_input('Value of stocks and shares ')
investments_value=st.number_input('Value of other investments/long-term savings')
debts=st.number_input('Debts you must pay soon ')
@st.cache_data(ttl=86400)
def get_metal_prices(currency):
  key=st.secrets['METALS_API_KEY']
  url='https://api.metals.dev/v1/latest?api_key=' + key + '&currency=' + currency + '&unit=g'
  response=requests.get(url)
  data=response.json()
  return data['metals'] 
prices=get_metal_prices(currency)  
gold_price=prices['gold']
silver_price=prices['silver']
st.write('Price of 1 gram of gold today:',gold_price,currency)
st.write('Price of 1 gram of silver today:',silver_price,currency)



  
