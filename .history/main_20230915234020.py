import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

st.title("Latest Data Professionals Salary")


def load_data():
    return pd.read_csv("./Partially Cleaned Salary Dataset.csv")


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state = st.text('Loading data...done!')
st.subheader('Raw data')
st.write(data)
SALARY_DATA = "Salary"
# data[SALARY_DATA] = data[SALARY_DATA].apply(int)
hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)
customcmap = ListedColormap(["crimson", "mediumblue", "darkmagenta"])
fig, ax = plt.subplots(figsize=(8, 6))
fig1 = plt.scatter(x=data['Location'], y=data['Salary'], s=150,
                   c=data['Salaries Reported'].astype('category'),
                   cmap=customcmap)
ax.set_xlabel(r'Location', fontsize=14)
ax.set_ylabel(r'Salary', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig1, theme=None, use_container_width=True)
