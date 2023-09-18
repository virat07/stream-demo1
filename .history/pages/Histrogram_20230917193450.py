import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# import data 
st.markdown("Histrogram ❄️")
st.sidebar.markdown("# Page 2 ❄️")
st.write(st.session_state["shared"])

SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)