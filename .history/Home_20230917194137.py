import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go

st.title("Latest Data Professionals Salary")


def load_data():
    return pd.read_csv("./Partially Cleaned Salary Dataset.csv")


if "shared" not in st.session_state:
    st.session_state["shared"] = True


# data_load_state = st.text('Loading data...')
data = load_data()
# data_load_state = st.text('Loading data...done!')
st.subheader('Raw data')
st.write(data)
SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)

# Scatter Graph

