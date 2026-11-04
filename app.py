import streamlit as st 
st.title('Zakat calculator')
cash=st.number_input('Cash you have on you or at home ')
bank=st.number_input('Money in your bank accounts')
gold_grams=st.number_input('Gold you own (in grams)')
debts=st.number_input('Debts you must pay soon ')
