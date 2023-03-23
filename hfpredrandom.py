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


def prediction(Age, sex, cp, sc, tstr, rer, nmv, rbp, spe, sdierr):

    prediction = classifier.predict([[Age, sex, cp, sc, tstr, rer, nmv, rbp, spe, sdierr]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    html_temp = """
    <div style="background-color:tomato;padding:8px">
    <h1 style="color:white;text-align:center;"> Heart Failure Predictor-AdaBoost J48 </h1>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)

    Age = st.number_input("Age: ", 0.0, 120.0, step=1.0)
    sex = st.selectbox("Sex: ", ('1-male', '0-female'))
    cp = st.selectbox("cp: ", ('1-Typical Angina',
                      '2-Atypical Angina', '3-Non Angina', '4-Asymptomatic'))
    sc = st.number_input("sc: ", 0.0, 500.0, step=1.0)
    tstr = st.selectbox(
        "tstr: ", ('3-Normal', '6-Fixed Defect', '7-Reversible Defect'))
    rer = st.selectbox("rer: ", ('0-Normal', '1-Having ST Wave Abnormality',
                       '2-Showing Probable or Definite Left Ventricular hypertrophy by Estes Criteria'))
    nmv = st.number_input("nmv: ", 0.0, 3.0, step=1.0)
    rbp = st.number_input("rbp: ", 0.0, 200.0, step=1.0)
    spe = st.selectbox("spe: ", ('1-Upsloping', '2-Flat', '3-Downsloping'))
    sdierr = st.number_input("sdierr: ", 0.0, 6.2, step=0.1)
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Age, sex, cp, sc, tstr, rer, nmv, rbp, spe, sdierr)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
