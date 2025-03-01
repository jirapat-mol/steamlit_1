import streamlit as st
import pandas as pd
# path = kagglehub.dataset_download("laotse/credit-risk-dataset")
# print("Path to dataset files:", path)
df = pd.read_csv("credit_risk_dataset.csv")


# st.title('Streamlit Example')