# Import packages
import streamlit as st
import pandas as pd
import joblib, os
import pickle

# Exportation
print(
    f'\n[Info] Exportation.\n')
to_export = {
    'labels': 
    'pipeline': end2end_pipeline,
}

# Useful functions
def load_ml_components(fp):
    'Load the ML component to re-use in app'
    with open(fp, 'rb') as f:
        object = pickle.load(f)
        return object

# Setup
## Variables and constants
DIRPATH = os.path.dirname(os.path.realpath(__file__))
ml_core_fp = os.path.join(DIRPATH, 'assets1', 'ml', 'ml.pkl')

## Execution
ml_components_dict = load_ml_components(fp=ml_core_fp)
labels = ml_components_dict['labels']
idx_to_labels = {i: l for (i, l) in enumerate(labels)}
end2end_pipeline = ml_components_dict['pipeline']

# Display execution
print(f'\n[Info] Predictable labels: {labels}')
print(f'\n[Info] Indexes to labels: {idx_to_labels}')
print(f'\n[Info] ML components loaded: {list(ml_components_dict.keys())}')

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

# Prediction expected
if st.button('Predict'):
    # Dataframe creation
    df = pd.DataFrame(
        {
        'Date': [date], 'Promotion Status': [promotion_status], 'Holiday Status': [holiday_status],
          'Oil Price': [oil_price], 'State': [state]      
        }
    )

# ML part
output = end2end_pipeline.predict_proba(df)

# Store the confidence score (probability for the predicted class)
df['Confidence Score'] = output.max(axis=-1)

# Get the index of the predicted class
predicted_idx = output.argmax(axis=-1)

# Store the index then replace it with the matching label
df['Predicted Label'] = predicted_idx
df['Predicted Label'] = df['Predicted Label'].replace(idx_to_labels)

print(f'[Info] Input data as dataframe: \n{df.to_markdown()}')

st.text(f"Customer churn prediction: '{''}' .")