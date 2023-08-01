# Import packages
import streamlit as st
import pandas as pd
import joblib, os
import pickle

# Interface
st.write('''# Store Sales Prediction
         This app was built to predict the sales of a grocery store based in Ecuador.
'''
)

# Input
date = st.date_input("Which date are you interested in?")

promotion_status = st.selectbox(('What is the promotion status on the selected date?'), ('Promotion', 'No Promotion'))

holiday_status = st.selectbox(('What is the holiday status on the selected date?'), ('Holiday', 'No Holiday'))

oil_price = st.number_input('What is the oil price on the selected date?', min_value=10.00, max_value=1000.00)

state = st.selectbox(('Which state are you interested in?'), ('Pichincha', 'Cotopaxi', 'Chimborazo','Imbabura',
       'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
       'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
       'El Oro', 'Esmeraldas', 'Manabi'))
