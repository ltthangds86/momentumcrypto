import streamlit as st

st.markdown('### Momentum Factor and Crypto Price Prediction')


st.markdown('----')
st.markdown('# What momentum factors were used?')
st.markdown('mom_10, mom_15, mom_20, mom_25: log_e(Current price divided by price 10,15,20,25 days ago)')
st.markdown('psma_15, psma_20, psma_25, psma_30: Current price divided by the average price of 15, 20, 25, and 30 days ago ')
st.markdown('smaf_2_20, smaf_3_20,smaf_3_25,smaf_5_30: The average price of 2,3,3,5 days ago divided by the average price of 20,20,25,30 days ago ')
st.markdown('rrp_15, rrp_20, rrp_25, rrp_30: The current price minus the 15,20,25,30 day average price divided by the 15,20,25,30 day standard deviation ')
st.markdown('Rank is the ordering from lowest to highest, where the cryptocurrency with the lowest momentum value will have a rank of 1')

st.markdown('----')
st.markdown('# Page return and mom20 ')
st.markdown('Visualizations showing the relationship momentum factor mom_20 with return')

st.markdown('----')
st.markdown('# Page Momentum ')
st.markdown('Visualizations depicting the relationship between return and momentum factors in momentum investment')

st.markdown('----')
st.markdown('# Page LSTM model ')
st.markdown('Using LSTM model to predict crypto price ')


