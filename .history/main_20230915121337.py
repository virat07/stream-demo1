import streamlit as st
import pandas as pd
import numpy as np

st.title("Latest Data Professionals Salary")
def load_data (): 
    data = pd.read_csv("/Salary Dataset.csv")
data = load_data()