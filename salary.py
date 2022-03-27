import streamlit as st
from predict import show_predict
from explore import show_explore
from app import show_app


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict()
else:
    show_explore()