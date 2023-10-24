import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import datetime
from catboost import CatBoostRegressor
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# Useful functions
def load_ml_components(fp):
    'Load the ML component to re-use in app'
    with open(fp, 'rb') as f:
        object = pickle.load(f)
        return object

# Variables and Constants
DIRPATH = os.path.dirname(os.path.realpath(__file__))
ml_core_fp = os.path.join(DIRPATH, 'Assets', 'export', 'ml_components.pkl')

# Load the Machine Learning components
ml_components_dict = load_ml_components(fp=ml_core_fp)

# Extract the ML components
best_model = ml_components_dict['model']
encoder = ml_components_dict['encoder']
scaler = ml_components_dict['scaler']

# Preprocess the data
def preprocess_data(input_df, encoder, scaler):
    categorical_features = ['family', 'onpromotion']
    numerical_features = ['sales', 'transactions', 'oil_price']
    
    df = input_df.copy()

    # Separate the categorical and numeric features
    categorical_df = df[categorical_features]
    numerical_df = df[numerical_features]

    # Encode the categorical features
    encoded_df = encoder.transform(categorical_df)

    # Scale the numeric features
    scaled_df = scaler.transform(numerical_df)

    # Concatenate the encoded categorical and scaled numeric features
    processed_df = np.concatenate((scaled_df, encoded_df), axis=1)

    # Get the names of columns after preprocessing
    encoded_feature_names = encoder.get_feature_names_out(categorical_features)
    all_feature_names = numerical_features + list(encoded_feature_names)

    # Convert the NumPy array to a pandas DataFrame
    processed_df = pd.DataFrame(processed_df, columns=all_feature_names)

    st.write('Columns in the DataFrame:', processed_df.columns.tolist())
    st.write('DataFrame Shape:', processed_df.shape)

    return processed_df

def main():
    st.set_page_config(page_title='Sales Prediction App', page_icon='📊', layout='wide')
    st.title('Sales Prediction App')
    st.markdown(
    """
<style>
    body {
        background-color: #008080;  /* Blue background color */
        color: #000000;  /* Text color */
    }
</style>
    """,
    unsafe_allow_html=True
)


    # User input section
    family = st.selectbox('Family', ['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'BREAD/BAKERY', 'CELEBRRATION', 'CLEANING',
                                     'DAIRY', 'DELI', 'EGGS', 'MEATS', 'PERSONAL CARE', 'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY',
                                     'PREPARED FOODS', 'PRODUCE',
                                     'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD'])
    onpromotion = st.radio('On Promotion', ['No Promotion', 'Promotion'])
    transactions = st.number_input('Transactions', min_value=0.0, step=0.01)
    oil_price = st.number_input('Oil Price', min_value=0.0, step=0.01)
    sales = st.number_input('Sales', min_value=0.0, step=0.01)


    # Predict button
    if st.button('Predict Sales'):
        # Prepare input data for prediction
        input_data = {
            'family': [family],
            'onpromotion': [onpromotion],
            'transactions': [transactions],
            'oil_price': [oil_price],
            'sales': [sales],
        }

        input_df = pd.DataFrame(input_data)

        # Preprocess the input data
        df = preprocess_data(input_df, encoder, scaler)

        # Make predictions using the loaded CatBoost model
        prediction = best_model.predict(df)

        # Display the prediction
        st.write(f'Predicted Sales: {prediction[0]:.2f}')

if __name__ == '__main__':
    main()