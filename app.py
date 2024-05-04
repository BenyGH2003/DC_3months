import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

columns= [['Age', 'Infarction volume', 'Comorbidity']]



model = joblib.load('DC_3m.pkl')


st.title('Prediction of 3 month mortality of patients undergoing DC :brain:')

age = st.number_input("Enter the patient age")
mrs = st.number_input("Enter the MRS of patients while discharging")
comorbidity= st.selectbox('Choose the comorbidity? Diabetes(1),Hypertension(2),Ischemic Heart Disease(3),Coagulopathy disorder(4),unknown(5),negative(6),Pneumonia(7),Metabolic Syndrome(8),cancer(9),cerebral vascular accident(10)',
                       [1,2,3,4,5,6,7,8,9,10])



def predict(): 
    row = np.array([age,mrs,comorbidity]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict_proba(X)
    if prediction[0][1] >= 0.35: 
        st.error('The patients is more likely not to survive, based on our model :heavy_exclamation_mark:')
    elif prediction[0][1] < 0.35:
        st.success('The patients is more likely to survive, based on our model :white_check_mark:') 
        

trigger = st.button('Predict', on_click=predict)
