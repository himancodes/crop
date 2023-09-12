import streamlit as st
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Crop Recommender")

st.sidebar.header("This is a web app")

N = float(st.number_input("Enter Nitrogen"))
P = float(st.number_input("Enter Phosphorus"))
K = float(st.number_input("Enter Potassium"))
Temp = float(st.number_input("Enter Temperature"))
Humidity = float(st.number_input("Enter Humidity"))
Ph = float(st.number_input("Enter Ph"))
Rainfall = float(st.number_input("Enter Rainfall"))




prediction = model.predict([[N,P,K,Temp,Humidity,Ph,Rainfall]])

def pred(prediction):
    clu1=['rice', 'papaya', 'jute', 'coffee', 'pigeonpeas', 'coconut']
    clu2=['chickpea', 'blackgram', 'mothbeans', 'mungbean', 'kidneybeans', 'pomegranate', 'mango', 'lentil', 'orange']
    clu3=['maize', 'banana', 'watermelon', 'muskmelon', 'cotton']
    clu4=['grapes', 'apple']
    
    if prediction ==0:
        return clu1
    elif prediction==1:
        return clu2
    elif prediction==2:
        return clu3
    else: return clu4
    


st.write("Recommended Crops: ", pred(prediction))
