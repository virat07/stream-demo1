import streamlit as st
import pandas as pd
import numpy as np

st.title("Latest Data Professionals Salary")
def load_data (): 
    return pd.read_csv("./Salary Dataset.csv")
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state = st.text('Loading data...done!')
st.subheader('Raw data')
st.write(data)
SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=1000000000)
st.bar_chart(hist_values)