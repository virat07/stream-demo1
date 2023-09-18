import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd

def load_data():
    return pd.read_csv("./Partially Cleaned Salary Dataset.csv")


if "shared" not in st.session_state:
    st.session_state["shared"] = True


# data_load_state = st.text('Loading data...')
data = load_data()
# data_load_state = st.text('Loading data...done!')

st.markdown("Histrogram ❄️")
st.sidebar.markdown("# Page 2 ❄️")
st.write(st.session_state["shared"])

SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)