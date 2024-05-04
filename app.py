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
<<<<<<< HEAD
comorbidity= st.selectbox('Choose the comorbidity? Diabetes(1),Hypertension(2),Ischemic Heart Disease(3),Coagulopathy disorder(4),unknown(5),negative(6),Pneumonia(7),Metabolic Syndrome(8),cancer(9),cerebral vascular accident(10)',
=======
comorbidity= st.selectbox('Choose the comorbidity? 1:Diabetes,2:Hypertension,3:Ischemic Heart Disease,4:Coagulopathy disorder,5:unknown,6:negative,7:Pneumonia,8:Metabolic Syndrome,9:cancer,10:cerebral vascular accident',
>>>>>>> 1cf9dc582441e4836b49edc7432a0e9e46c0b28f
                       [1,2,3,4,5,6,7,8,9,10])



def predict(): 
    row = np.array([age,mrs,comorbidity]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict_proba(X)
<<<<<<< HEAD
    if prediction[0][1] >= 0.35: 
        st.error('The patients is more likely not to survive :thumbsdown:')
    elif prediction[0][1] < 0.35:
        st.success('The patients is more likely to survive :thumbsup:') 
=======
    if prediction[0] >= 0.35: 
        st.error('The patients is more likely not to survive, based on our model :heavy_exclamation_mark:')
    elif prediction[0] < 0.35:
        st.success('The patients is more likely to survive, based on our model :white_check_mark:') 
>>>>>>> 1cf9dc582441e4836b49edc7432a0e9e46c0b28f
        

trigger = st.button('Predict', on_click=predict)
