# Import packages
import streamlit as st
import pandas as pd
import joblib, os

st.write("""# Customer Churn Prediction
         This app was built to help identify customers that are likely to churn.
         Kindly select the option that applies to your choice customer.
""")

# Input
st.selectbox(('What is the customer gender?'), ('Male', 'Female'))

st.selectbox(('Is the customer a senior citizen?'), ('Yes', 'No'))

st.selectbox(('Does the customer have a partner??'), ('Yes', 'No'))

st.selectbox(('Does the customer have dependents?'), ('Yes', 'No'))

st.selectbox(('Does the customer have phone service?'), ('Yes', 'No'))

st.selectbox(('Does the customer have multiple lines?'), ('Yes', 'No'))

st.selectbox(('Which interner service does the customer use?'), ('Fiber optic', 'No', 'DSL'))

st.selectbox(('Does the customer have online security?'), ('Yes', 'No'))

st.selectbox(('Does the customer have online backup?'), ('Yes', 'No'))

st.selectbox(('Does the customer have device protection?'), ('Yes', 'No'))

st.selectbox(('Does the customer have tech support?'), ('Yes', 'No'))

st.selectbox(('Does the customer have streaming TV service?'), ('Yes', 'No'))

st.selectbox(('Does the customer have streaming movies service?'), ('Yes', 'No'))

st.selectbox(('What is the customer\'s contract length?'), ('Month-to-month', 'One year', 'Two years'))

st.selectbox(('Does the customer use paperless billing?'), ('Yes', 'No'))

st.selectbox(('What is the customer\'s payment method?'), ('Electronic check', 'Mailed check', 'Credit card (automatic)', 'Bank transfer (automatic)'))

st.slider('What is the customer\'s tenure length?', 0, 50, 100)

st.number_input('What is the customer\'s monthly charge?', min_value=10.00, max_value=120.00)

st.number_input('What is the customer\'s total charge?', min_value=10.00, max_value=10000.00)

