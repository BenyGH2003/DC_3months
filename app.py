import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

columns= [['Age', 'Infarction volume', 'Comorbidity']]



model = joblib.load('DC3.pkl')


st.title('Prediction of 3 month mortality of patients undergoing DC :brain:')

age = st.number_input("Enter the patient age")
mrs = st.number_input("Enter the MRS of patients while discharging")
comorbidity= st.selectbox('Choose the comorbidity? 1:Diabetes,2:Hypertension,3:Ischemic Heart Disease,4:Coagulopathy disorder,5:unknown,6:negative,7:Pneumonia,8:Metabolic Syndrome,9:cancer,10:cerebral vascular accident'
                       [1,2,3,4,5,6,7,8,9,10])



def predict(): 
    row = np.array([age,mrs,comorbidity]) 
    X = pd.DataFrame([row], columns = columns)
    X= pd.get_dummies(columns=['Comorbidity'])
    prediction = model.predict_proba(X)
    if prediction[0] >= 0.35: 
        st.error('The patients is more likely not to survive :thumbsdown:')
    elif prediction[0] < 0.35:
        st.success('The patients is more likely to survive :thumbsup:') 
        

trigger = st.button('Predict', on_click=predict)