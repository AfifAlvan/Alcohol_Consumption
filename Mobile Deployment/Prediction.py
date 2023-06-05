import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import joblib
import json

with open('model_scaler.pkl', 'rb') as file_1:
  model_scaler = joblib.load(file_1)
with open('model_encoder.pkl', 'rb') as file_2:
  model_encoder = joblib.load(file_2)
with open('list_num_cols.txt', 'r') as file_3:
  list_num_cols = json.load(file_3)  
with open('list_cat_cols.txt', 'r') as file_4:
  list_cat_cols = json.load(file_4)
with open('Model_Forest.pkl', 'rb') as file_5:
  Model_Forest = joblib.load(file_5)

def run():
    #Membuat Form
    with st.form(key='Parameter'):
        nama = st.text_input('Name', value='')
        Age = st.number_input('Age', min_value=15, max_value=22, value=20, step=1)
        sex = st.selectbox('Sex', ('F','M'))
        studytime = st.number_input('Study Time', min_value=0.0, max_value=4.0 , step = 0.5)    
        freetime = st.selectbox('Free Time',(1,2,3,4,5), index=1, 
                               help='''
    Intensity Free Time:
    
    1. Very Low 
    2. Low                               
    3. Netral
    4. High
    5. Very High''')
        
        Walc = st.selectbox('Walc',(1,2,3,4,5), index=1, help='''
    Consumption Alcohol per Week:
    
    1. Very Low 
    2. Low                               
    3. Netral
    4. High
    5. Very High''')   
        Dalc = st.selectbox('Dalc',(1,2,3,4,5), index=1, help='''
    Consumption Alcohol per Day:
    
    1. Very Low 
    2. Low                               
    3. Netral
    4. High
    5. Very High''')
        st.markdown('----')
        
        submitted = st.form_submit_button('Predict Grade')

    data_inf ={
        'Name' : nama,
        'age' : Age,
        'sex' : sex,
        'studytime' : studytime,
        'freetime' : freetime,
        'Walc' : Walc,
        'Dalc' : Dalc
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]
        
        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
        
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

        y_pred_inf = Model_Forest.predict(data_inf_final)

        st.write('# Predict Grade : ', str(int(y_pred_inf)))
if __name__ == '__eda__':
    run()    