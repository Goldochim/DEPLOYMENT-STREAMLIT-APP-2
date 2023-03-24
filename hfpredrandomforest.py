# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:34:49 2023

@author: Gold ICT.
"""

import pickle
import streamlit as st



# loading in the model to predict on the data
pickle_in= open("rfmodel.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs


def predictionfnc(age, sex, cp, sc, fbs, tstr, eia, rer, mhra, nmv, rbp, spe, sdierr):

    prediction = classifier.predict([[age, sex, cp, sc, fbs, tstr, eia, rer, mhra, nmv, rbp, spe, sdierr]])
    print(prediction)
    if (prediction== ['No']):
        return 'NO HEART FAILURE'
    else:
        return 'WARNING!!! HEART FAILURE PREDICTED'



# this is the main function in which we define our webpage
def main():
    html_temp = """
    <div style="background-color:navy;padding:7px">
    <h2 style="color:white;text-align:center;"> Heart Failure Predictor-Random Forest </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.number_input("Age: ", 0.0, 120.0, step=1.0)
    
    sex = st.selectbox("Sex: ", ('1-male', '0-female'))
    if sex=='1-male':
        sex=1
    else:
        sex=0
    cp = st.selectbox("cp: ", ('1-Typical Angina',
                      '2-Atypical Angina', '3-Non Angina', '4-Asymptomatic'))
    if cp=='1-Typical Angina':
        cp=1
    elif cp=='2-Atypical Angina':
        cp=2  
    elif cp=='3-Non Angina':
        cp=3
    else:
        cp=4
        
 
    sc = st.number_input("sc: ", 0.0, 500.0, step=1.0)
    tstr = st.selectbox(
        "tstr: ", ('3-Normal', '6-Fixed Defect', '7-Reversible Defect'))
    if tstr=='3-Normal':
        tstr=3
    elif tstr== '6-Fixed Defect':
        tstr=6
    else:
        tstr=7
        
        
    rer = st.selectbox("rer: ", ('0-Normal', '1-Having ST Wave Abnormality',
                       '2-Showing Probable or Definite Left Ventricular hypertrophy by Estes Criteria'))
    if rer=='0-Normal':
        rer=0
    elif rer== '1-Having ST Wave Abnormality':
        rer=1
    else:
        rer=2
    
    
    nmv = st.number_input("nmv: ", 0.0, 3.0, step=1.0)
    rbp = st.number_input("rbp: ", 0.0, 200.0, step=1.0)
    
    spe = st.selectbox("spe: ", ('1-Upsloping', '2-Flat', '3-Downsloping'))
    if spe=='1-Upsloping':
        spe=1
    elif spe== '2-Flat':
        spe=2
    else:
        spe=3
    
    sdierr = st.number_input("sdierr: ", 0.0, 6.2, step=0.1)
    eia = st.selectbox(
        "eia: ", ('1-Yes', '0-No'))
    if eia=='1-Yes':
        eia=1
    else:
        eia=0
    mhra = st.number_input("mhra: ", 60.0, 200.0, step=1.0)   
    fbs = st.selectbox(
        "fbs > 120 mg/dl: ", ('1-Yes', '0-No'))
    if fbs=='1-True':
        fbs=1
    else:
        fbs=0
        
    
    
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result..
    if st.button("Predict"):
        result = predictionfnc(age, sex, cp, sc, fbs, tstr, eia, rer, mhra, nmv, rbp, spe, sdierr)
    st.success(result)


if __name__ == '__main__':
    main()
