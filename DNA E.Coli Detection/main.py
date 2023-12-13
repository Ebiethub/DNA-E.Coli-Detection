#Library imports
import numpy as np
import pandas as pd
import streamlit as st
import cv2
import sklearn
import pickle


#Loading the Model
encoder = pickle.load(open('EColi-encoder1.pickle', 'rb'))
model = pickle.load(open('EColi.pickle', 'rb'))


#Setting Title of App
st.title("DNA EColi Disease Detection")
st.write('<h3>Use this app to check if your DNA sequence contains EColi Virus</3>', unsafe_allow_html=True)
st.write("<h5>Use the DNA sequence below as an example</h5>", unsafe_allow_html=True)
st.write("ttaacattaataaataaggaggctctaatggcactcattagccaatcaatcaagaat")
Text = st.text_input('DNA Sequence')

submit = st.button('Predict')
#On predict button click
if submit:


    if Text is not None:
        genome_list = list(Text)
        print(genome_list)
        df_test = pd.DataFrame(genome_list)
        df_test = df_test.transpose()


        # Convert the encoder to array
        data_test = encoder.transform(df_test).toarray()

        # Make Prediction
        result = model.predict(data_test)[0]

        newmapper = {0: 'The DNA sequence does not contain EColi Virus', 1: 'The DNA sequence contains EColi Virus'}


        st.title(newmapper[result])


