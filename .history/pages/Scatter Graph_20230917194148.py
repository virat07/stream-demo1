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

st.markdown("Scatter Graph ❄️")
# st.sidebar.markdown("# Page 2 ❄️")
st.write(st.session_state["shared"])

customcmap = ListedColormap(["crimson", "mediumblue", "darkmagenta"])
fig1 = px.scatter(data, x=data['Salary'], y=data['Location'], color="Salary")
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig1, theme=None, use_container_width=True)
