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
vaches=int(st.number_input("Combien de vaches possédez-vous?"))
hawl_vaches=st.radio("Possédez-vous ces vaches depuis au moins un an (année lunaire)", ["Oui" , "Non"])
chameaux=int(st.number_input("Combien de chameaux possédez-vous?"))
hawl_chameaux=st.radio("Possédez-vous ces chameaux depuis au moins un an (année lunaire)", ["Oui" , "Non"])
moutons_chevres=int(st.number_input("Combien de chèvres et moutons possédez-vous"))
hawl_moutons_chevres=st.radio("Possédez-vous ces moutons et chèvres depuis au moins un an (année lunaire)", ["Oui" , "Non"])
if st.button("Calculer",type="primary"):
  # Vaches
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
    st.success(f"Vaches: Vous devez donner {groupe30} veau(x) d'un an et {groupe40} vache(s) de deux.")
    #Chameaux
  if chameaux<5 or hawl_chameaux=="Non":
    st.info("Pas de zakat sur vos chameaux : il faut au moins 5 chameaux possédés depuis un an .")
  elif  chameaux <= 9:
    st.success("Chameaux: vous devez donner 1  bête :1 mouton ou 1 chèvre.")
  elif chameaux <= 14:
    st.success("Chameaux: vous devez donner 2  bêtes. Vous pouvez donner 2 moutons, ou 2 chèvres, ou 1 mouton et 1 chèvre")
  elif chameaux <=19:
    st.success("Chameaux: vous devez donner 3  bêtes. Vous pouvez donner 3 moutons, ou 3 chèvres, ou un mélange des  deux (par exemple 2 moutons et 1 chèvre)")
  elif chameaux <=24:
    st.success("Chameaux: vous devez donner 4  bêtes. Vous pouvez donner 4 moutons, ou 4 chèvres, ou un mélange des deux (par exemple 2 moutons et 2 chèvres)")
  elif chameaux <=35:
    st.success("Chameaux: vous devez donner une chamelle d'un an")
    st.caption("Si vous n'avez pas de chamelle d'un an, vous pouvez donner à la place un jeune chameaux mâle de deux ans.")
  elif chameaux <=45:
    st.success("Chameaux: vous devez donner 1 chamelle de deux ans")
  elif chameaux <= 60:
    st.success("Chameaux: vous devez donner une chamelle de trois ans")
  elif chameaux <= 75:
    st.success("Chameaux: vous devez donner une chamelle de quatre ans")
  elif chameaux <= 90:
    st.success("Chameaux: vous devez donner 2 chamelles de deux  ans")
  elif chameaux <= 120:
    st.success("Chameaux: vous devez donner 2 chamelles de trois  ans")
  else:
    chameaux_arrondies= (chameaux // 10)*10
    groupe50=chameaux_arrondies // 50
    while ( chameaux_arrondies-groupe50 * 50) % 40 != 0:
      groupe5O=groupe50-1
    groupe40=(chameaux_arrondies-groupe50*50)//40
    st.success(f"Chameaux: vous devez donner {groupe40} chamelle(s) de deux ans et {groupe50} chamelle(s) de trois ans")
    # Moutons et chèvres 
  if moutons_chevres < 40 or hawl_moutons_chevres=="Non":
    st.info("Pas de Zakat sur vos moutons et chèvres : il faut au minimum 40  animaux possédés depuis un an.")
  elif  moutons_chevres <= 120:
    st.success("Moutons et chèvres : vous devez donner une bête : 1 mouton ou 1 chèvre.")
  elif moutons_chevres <=200:
     st.success("Moutons et chèvres: vous devez donner 2 bêtes: 2 moutons, ou 2 chèvres, ou 1 mouton et 1 chèvre")
  elif moutons_chevres <= 399:
     st.success("Moutons et chèvres : vous devez donner 3 bêtes : 3 moutons, ou 3 chèvres, ou un mélange des deux")
  else:
     groupe100 = moutons_chevres // 100
     st.success(f"Moutons et chèvres: vous devez donner {groupe100} bêtes, {groupe100} moutons, ou {groupe100} chèvres, ou un mélange des deux")
st.header("Zakat al-fitr")
personnes=int(st.number_input("Combien de personnes nourrissez-vous, vous compris ?", min_value=0))
aliment=st.selectbox("Quel aliment allez-vous donner ?" , ["Mil","Riz","Sorgho","Maïs","Blé"])
if st.button("Calculer ma zakat al-fitr",type="primary"):
  if personnes==0:
     st.info("Indiquez au moins une personne.")
  else: 
    kilos=personnes*2.5
    st.success(f"Vous devez donner {kilos} kilos de {aliment.lower()}.")
    st.caption("Soit un sâ , environ 2,5 kilos par personne. A donner aux pauvres, avant prière de l'Aïd.")
st.header("Récolte")
nom_recolte=st.text_input("Quel est le nom de votre récolte")
type_recolte=st.radio("Votre récolte est-elle une céréale ou un légume sec (haricots,niébé....)?",["Oui","Non"], horizontal=True)
type_fruit="Non"
if type_recolte=="Non":
   type_fruit=st.radio("Votre récolte est-elle des dattes, des raisins secs, des olives ou du sésame?",["Oui","Non"], horizontal=True)
kilos_recolte=st.number_input("Combien de kilos avez-vous récoltés?", min_value=0.0)
type_arrosage=st.radio("Comment votre champ a-t-il été arrosé?",["Par la pluie (ou un fleuve)","Par arrosage avec effort ou en payant (pompe,puits...)","les deux à part égales"])





    














    











    
    






























    
    


  
