#!/usr/bin/env python
# coding: utf-8

# In[1]:


### THIS IS MY STREAMLIT APP


# In[2]:


##Author: Omoboade Afolabi


# In[3]:


### import libraries
import pandas as pd
import pandas as pd
import streamlit as st
import pickle


# In[4]:



#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


# In[5]:


#######################################################################################################################################
### Create a title
st.markdown("<h1 style='text-align: center; color: blues;'>Gestational Diabetes Mellitus Prediction Using Machine Learning</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>Author: Omoboade Afolabi </h3>", unsafe_allow_html=True)


# In[6]:


#######################################################################################################################################
### DATA LOADING
df = pd.read_csv("gestational_diabetes.csv")


# In[11]:


#######################################################################################################################################
### MODEL LOADING
pickle_in = open('my_best_log1.pkl', 'rb')
classifier = pickle.load(pickle_in)


# In[8]:


################################################## MEDICAL CONDITION MEASUREMENTS #####################################################
#st.markdown("<h4 style='text-align: center; color: grey;'> Please answer the following questions: </h4>", unsafe_allow_html=True)

def get_input():
    
    Age = st.number_input('Enter your age')
    Family_History_of_Diabetes = st.number_input('Do you have a Family History of Diabetes? Yes=1, No=0')
    Prediabetes = st.number_input('Do you have Prediabetes? Yes=1, No=0')
    PCOS = st.number_input('Do you have Polycystic Ovary Syndrome(PCOS)? Yes=1, No=0')
    Previous_Pregnancy_Gestation = st.number_input('Have you had a previous pregnancy? Yes=1, No=0')
    Unexplained_Prenetal_Loss = st.number_input('Have you had an unexplained Prenetal Loss? Yes=1, No=0')
    Large_Child_or_Birth_Default = st.number_input('Have you had a Large Child or Birth Default ? Yes=1, No=0')
    Sedentary_Lifestyle = st.number_input('Do you have a Sedentary Lifestyle? Yes=1, No=0')
    Healthy_weight = st.number_input('Do you have a Healthy weight? Yes=1, No=0')
    Obese = st.number_input('Are you obese? Yes=1, No=0')
    Overweight = st.number_input('Are you Overweight? Yes=1, No=0')
    Underweight = st.number_input('Are you Underweight? Yes=1, No=0')
    ElevatedBP = st.number_input('Do you have an Elevated BP? Yes=1, No=0')
    Hypertension_stage_1 = st.number_input('Do you have Hypertension stage 1? Yes=1, No=0')
    Hypertension_stage_2 = st.number_input('Do you have Hypertension stage 2? Yes=1, No=0')
    NormalBP = st.number_input('Do you have an Normal BP? Yes=1, No=0')
    OGTT = st.number_input('What is your Oral Glucose Test Tolerance result?')
    BMI = st.number_input('What is your Body Mass Index?')
    HDL = st.number_input('What is your High Density Lipoprotein/Good protein(mg/dL)?')
    SystolicBP = st.number_input('What is your Systolic Blood Pressure in mmHg?')
    DiastolicBP = st.number_input('What is your Diastolic Blood Pressure in mmHg?')
    Hemoglobin = st.number_input('What is your Hemoglobin measurement in g/dL')
    Number_of_Pregnancy = st.number_input('How many pregnancies have you had?')
    
    
    user_info = {'Age': Age, 
                 'Number_of_Pregnancy': Number_of_Pregnancy, 
                 'Previous_Pregnancy_Gestation': Previous_Pregnancy_Gestation, 
                 'BMI': BMI, 
                 'HDL': HDL,
                 'Family_History_of_Diabetes': Family_History_of_Diabetes ,
                 'Unexplained_Prenetal_Loss': Unexplained_Prenetal_Loss,
                 'Large_Child_or_Birth_Default': Large_Child_or_Birth_Default , 
                 'PCOS': PCOS, 
                 'SystolicBP': SystolicBP , 
                 'DiastolicBP': DiastolicBP,
                 'OGTT': OGTT,
                 'Hemoglobin': Hemoglobin, 
                 'Sedentary_Lifestyle': Sedentary_Lifestyle , 
                 'Prediabetes': Prediabetes, 
                 'Healthy_weight': Healthy_weight, 
                 'Obese': Obese, 
                 'Overweight': Overweight, 
                 'Underweight': Underweight , 
                 'ElevatedBP': ElevatedBP ,
                 'Hypertension_stage_1': Hypertension_stage_1 , 
                 'Hypertension_stage_2': Hypertension_stage_2, 
                 'NormalBP': NormalBP, 
                }
    
    predictors = pd.DataFrame(user_info, index=[0])  
    return predictors

user_input = get_input()  


# In[9]:


submit = st.button('Predict Gestational Diabetes')    
 
if submit:
    
    prediction = classifier.predict(user_input)  
    print(prediction)
    if prediction == 0:
            st.write('Congratulations!''We predict that you do not have gestational diabetes')
    else:
            st.write(" We predict that you may have Gestational Diabetes. Please consult your doctor")


# In[ ]:




