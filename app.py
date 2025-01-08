# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:14:21 2024

@author: User
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu # creating side bar option menu / navigation panel in Web App

# loading the saved model

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('heart_model.sav', 'rb'))

# creating side bar option menu / navigation panel in Web App

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           
                           icons = ['activity', 'heart'], # insert icons in web app
                           
                           default_index = 0) # default_index = 0 to make the first page as default page
    
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    # page title
    
    st.title('Diabetes Prediction using ML')
    
    # create input data for user
    
      # columns for input fields
      
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('The Age of the Person')
    
    # create predict button to display the result
    
    diabetes_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diabetes_prediction[0] == 1):
            diabetes_diagnosis = 'The person is Diabetic'
            
        else:
            diabetes_diagnosis = 'The person is not Diabetic'
        
    st.success(diabetes_diagnosis)
    
    
# Heart Disease Prediction Page

if (selected == 'Heart Disease Prediction'):
    
    # page title
    
    st.title('Heart Disease Prediction using ML')
    
    # create input data for user
    
      # columns for input fields
      
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Enter Patient Age')
    
    with col2:
        sex = st.text_input('Enter Patient Gender (1 = male ; 0 = female)')
    
    with col1:
        cp = st.text_input('Chest Pain Type (4 values)')
    										
    with col2:
        trestbps = st.text_input('Resting Blood Pressure Value')
    
    with col1:
        chol = st.text_input('Serum Cholestoral Level in mg/dl')
    
    with col2:
        fbs = st.text_input('Fasting Blood Sugar Level > 120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results Value (0, 1, 2)')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved Value')
        
    with col1:
        exang = st.text_input('Exercise Induced Angina (1 = yes ; 0 = no)')
            
    with col2:
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
                
    with col1:
        slope = st.text_input('The Slope of the Peak Exercise ST Segment')

    with col2:
        ca = st.text_input('Number of Major Vessels (0-3) Colored by Flourosopy')
        
    with col1:
        thal = st.text_input('Enter : 0 = normal ; 1 = fixed defect ; 2 = reversable defect')
    
    # create predict button to display the result
    
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0] == 0):
            heart_diagnosis = 'The person has Healthy Heart'
            
        else:
            heart_diagnosis = 'The person has Defected Heart'
        
    st.success(heart_diagnosis)
    
    
    