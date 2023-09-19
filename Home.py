import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import plotly.express as px




st.title("Latest Data Professionals Salary")

def load_data():
    return pd.read_csv("./Partially Cleaned Salary Dataset.csv")

if "shared" not in st.session_state:
    st.session_state["shared"] = True


data = load_data()
st.subheader('Raw data')
st.write(data)

# st.markdown("Histrogram ❄️")
# # st.sidebar.markdown("# Page 2 ❄️")
# st.write(st.session_state["shared"])

# SALARY_DATA = "Salary"

# hist_values = np.histogram(
#     data[SALARY_DATA], bins=20)
# st.bar_chart(hist_values)



# st.markdown("Scatter Graph ❄️")
# # st.sidebar.markdown("# Page 2 ❄️")
# st.write(st.session_state["shared"])

# fig1 = px.scatter(data, x=data['Salary'], y=data['Location'], color="Salary")
# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig1, theme=None, use_container_width=True)
