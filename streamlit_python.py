import streamlit as st
import pandas as pd
import seaborn as sns
# path = kagglehub.dataset_download("laotse/credit-risk-dataset")
# print("Path to dataset files:", path)
df = pd.read_csv("credit_risk_dataset.csv")

#change the column name
df = df.rename(columns={'person_age': 'Age', 'person_income': 'Income', 'person_home_ownership': 'Home Ownership', 'person_emp_length': 'Employment Length', 'loan_intent': 'Loan Intent', 'loan_grade': 'Loan Grade', 'loan_amnt': 'Loan Amount', 'loan_int_rate': 'Interest Rate', 'loan_status': 'Loan Status', 'loan_percent_income': 'Loan Percent Income', 'cb_person_default_on_file': 'Default on File', 'cb_person_cred_hist_length': 'Credit History Length'})
#round float to 2 decimal

# for col in df.columns:
#     if df[col].dtype == 'float64':
#         # st.write(df[col].dtype)
#         df[col] = df[col].round(2)
# print(df['Employment Length'].head(5))


st.set_page_config(
    page_title="Credit Risk Analysis",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.sidebar.title("Credit Risk Analysis")
st.title("Risk Analysis and Portfolio Management")
# st.subheader("NgernTurbo")

col1, col2, col3 = st.columns(3)

with col1:    
    st.metric("Total Loan Amount", "$" + str(df['Loan Amount'].sum()),border=True)

with col2:
    st.metric("Average Loan Amount", "$" + str(df['Loan Amount'].mean()),border=True)
with col3:
    st.metric("Total Income", "$" + str(df['Income'].sum()),border=True)

st.markdown("### Data Preview")
st.table(df[0:5].style.format(precision=2).highlight_max(subset=['Income'], color='pink'))

st.markdown("### Data Summary")
st.write(df.describe().style.format(precision=2))

st.markdown("### Data Visualization")


#Visualization

#show the distribution of Loan Percent Income
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sns.histplot(df['Loan Percent Income']*100, kde=True, ax=ax,binwidth=5,color='pink')
ax.set_title('Loan Percent Income Distribution')
st.pyplot(fig)

High_LPI = df[df['Loan Percent Income'] > 0.4]
st.write(High_LPI)


