import streamlit as st

st.markdown("Histrogram ❄️")
st.sidebar.markdown("# Page 2 ❄️")


SALARY_DATA = "Salary"

hist_values = np.histogram(
    data[SALARY_DATA], bins=20)
st.bar_chart(hist_values)