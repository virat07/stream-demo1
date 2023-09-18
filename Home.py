import streamlit as st
import pandas as pd


st.title("Latest Data Professionals Salary")


def load_data():
    return pd.read_csv("./Partially Cleaned Salary Dataset.csv")


if "shared" not in st.session_state:
    st.session_state["shared"] = True


data = load_data()
st.subheader('Raw data')
st.write(data)


