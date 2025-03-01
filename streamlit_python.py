import streamlit as st
import pandas as pd
import seaborn as sns
# path = kagglehub.dataset_download("laotse/credit-risk-dataset")
# print("Path to dataset files:", path)
df = pd.read_csv("credit_risk_dataset.csv")

st.set_page_config(
    page_title="Credit Risk Analysis",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Credit Risk Analysis")
st.title("Risk Analysis and Portfolio Management")
st.subheader("NgernTurbo")

st.table(df.head(20).style.highlight_max(subset=['person_income'], color='pink'))
