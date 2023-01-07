import streamlit as st
import pickle

st.title('Crop Prediction System')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
n=col1.number_input('Enter Nitrogen')
p=col2.number_input('Enter Phosphorous')
k=col1.number_input('Enter Potassium')
t=col2.number_input('Enter Temperature')
h=col1.number_input('Enter Humidity')
ph=col2.number_input('Enter pH')
r=col1.number_input('Enter Rainfall')

if st.button('Predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    st.success(result)