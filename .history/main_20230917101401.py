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


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state = st.text('Loading data...done!')
st.subheader('Raw data')
st.write(data)
SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)

# Scatter Graph 
# customcmap = ListedColormap(["crimson", "mediumblue", "darkmagenta"])
# fig1, ax = plt.subplots(figsize=(8, 6))
# fig1 = plt.scatter(x=data['Salary'], y=data['Location'], s=150,
#                    c=data['Salaries Reported'].astype('category'),
#                    cmap=customcmap)
# ax.set_xlabel('Location', fontsize=14)
# ax.set_ylabel('Salary', fontsize=14)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# # plt.show()
# tab1 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig1, theme=None, use_container_width=True)



st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
