import streamlit as st
import requests
st.set_page_config(page_title='Zakat calculator', page_icon=':crescent_moon:')
st.title(' :crescent_moon: Zakat calculator')
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
gold_value=gold_grams*gold_price 
silver_value=silver_grams*silver_price
total_wealth=(gold_value + silver_value + cash + bank + business_goods + stocks_value + investments_value)-debts
nisab_gold=85* gold_price
nisab_silver=595* silver_price
nisab_choice=st.radio('Which nisab do you want to use?',['Silver nisab','Gold nisab'])
if nisab_choice=='Silver nisab':
   nisab=nisab_silver
else:
   nisab=nisab_gold
if st.button('Calculate',type='primary'):
   if total_wealth >= nisab:
       zakat=total_wealth * 0.025
       st.success('Your zakat is :' + str(round(zakat,2)) + ' '+ currency)
   else:
       st.info('Your Wealth is below the nisab. You do not owe zakat this year.')
st.header("Animaux")
vaches=st.number_input("Combien de vaches possédez-vous?")
hawl_vaches=st.radio("Possédez-vous ces vaches depuis au moins un an (année lunaire)", ["Oui" , "Non"])
chameaux=st.number_input("Combien de chameaux possédez-vous?")
hawl_chameaux=st.radio("Possédez-vous ces chameaux depuis au moins un an (année lunaire)", ["Oui" , "Non"])
moutons_chèvres=st.number_input("Combien de chèvres et moutons possédez-vous")
hawl_moutons_chèvres=st.radio("Possédez-vous ces moutons et chèvres depuis au moins un an (année lunaire)", ["Oui" , "Non"])
if st.button("Calculer",type="primary"):
  if vaches<30 or hawl_vaches=="Non":
    st.info("Pas de zakat sur vos vaches: il faut au moins 30 vaches possédées depuis un an.")
  elif vaches<=39 and hawl_vaches=="Oui":
    st.success("Vaches: vous devez donner 1 veau d'un an.")
  elif vaches<=59 and hawl_vachse=="Oui":
    st.success("Vaches: vous devez donner 1 vache de deux ans.")
  else:
    vaches_arrondies=(vaches//10)*10
    groupe40=vaches_arrondies//40
    while (vaches_arrondies-groupe40*40)% 30 !=0:
      groupe40=groupe40-1
   groupe30=(vaches_arrondies-groupe40*40)//30
   st.success(f"Vaches: Vous devez donnez {groupe30} veau(x) d'un an et {groupe_40} vache(s) de deux.")















    
    


  
