import streamlit as st
import pandas as pd

st.title("Nairobi Housing Predictor")
price = st.slider("Select Budget (KSh)", 0, 1000000)
st.write(f"Showing houses under {price}")
# You can drop your Housing CSV or ML Model here!
