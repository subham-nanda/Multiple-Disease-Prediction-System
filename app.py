import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Load the model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System", ["Diabetes Prediction", "Heart Disease Prediction"],icons=['activity','heart', 'person'] ,default_index = 0)

# Diabetes Prediction Page
if (selected == "Diabetes Prediction"):
    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.00)
    with col3:
        BloodPressure = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=0.00)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value (mm)", min_value=0.00)
    with col2:
        Insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0.00)    
    with col3:
        BMI = st.number_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.number_input("Age", min_value=0, step=1)

    # Code for Prediction
    diabetes_diagnosis = ''
    if st.button("Diabetes Test Result"):
        input_data = np.array([Pregancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1,-1)
        diabetes_prediction = diabetes_model.predict(input_data)
        if (diabetes_prediction[0] == 1):
            st.success("You are Diabetic")
        else:
            st.success("You are not Diabetic")   

          

if (selected == "Heart Disease Prediction"):
    st.title("Heart Disease Prediction") 
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.number_input('Sex (1 = Male ; 0 = Female)', min_value=0, max_value=1, step=1)
    with col3:
        cp = st.number_input('Chest Pain Type (0: Typical Angina, 1: Atypical Angina, 2: Non-Anginal Pain, 3: Asymptomatic)', min_value=0, max_value=3, step=1)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0.00)
    with col2:
        chol = st.number_input('Cholestrol Level (mg/dL)', min_value=0.00)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dL (1 = True; 0 = False)', min_value=0, max_value=1, step=1)
    with col1:
        restecg = st.number_input('Resting ECG Results (0: Normal, 1: ST-T Wave Abnormality, 2: Left Ventricular Hypertrophy)', min_value=0, max_value=2, step=1)
    with col2:
        thalach = st.number_input('Max Heart Rate Achieved (bpm)', min_value=0, step=1)
    with col3:
        exang = st.number_input('Exercise Induced Angina (1 = Yes; 0 = No)', min_value=0, max_value=1, step=1)
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.00)
    with col2:
        slope = st.number_input('Slope of the Peak Exercise ST Segment (0: Upsloping, 1: Flat, 2: Downsloping)', min_value=0, max_value=2, step=1)
    with col3:
        ca = st.number_input('Number of Major Vessel Colored by Flourosopy', min_value=0, max_value=3 ,step=1)   
    with col1:
        thal = st.number_input('Thalassemia (0: Normal, 1: Fixed Defect, 2: Reversable Defect)', min_value=0, max_value=2, step=1)
    
    if st.button("Heart Disease Test Result"):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            st.success("You have Heart Disease")
        else:
            st.success("You does not have any Heart Disease")
             