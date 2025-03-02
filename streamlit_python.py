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

topcol1, topcol2, topcol3 = st.columns(3)

with topcol1:    
    st.metric("Total Loan Amount", "$" + str(df['Loan Amount'].sum()),border=True)
with topcol2:
    st.metric("Average Loan Amount", "$" + str(df['Loan Amount'].mean()),border=True)
with topcol3:
    st.metric("Total Income", "$" + str(df['Income'].sum()),border=True)

st.markdown("### Data Preview")
st.table(df[0:5].style.format(precision=2).highlight_max(subset=['Income'], color='pink').set_properties(**{'background-color': 'white', 'color': '#014888'}))



st.markdown("### Data Summary")
def stream_data():
    # for word in _LOREM_IPSUM.split(" "):
    #     yield word + " "
    #     time.sleep(0.02)

    yield pd.DataFrame(
        df.describe(),
        columns=["Age", "Income", "Employment Length", "Loan Amount", "Interest Rate", "Loan Percent Income", "Credit History Length"],
    )

    # for word in _LOREM_IPSUM.split(" "):
    #     yield word + " "
    #     time.sleep(0.02)


if st.button("Show Summary"):
    st.dataframe(next(stream_data()).style
             .set_properties(**{'background-color': 'white', 'color': '#014888'})
    )
# st.write(df.describe().style.format(precision=2))

st.markdown("### Data Visualization")


#Visualization

#show the distribution of Loan Percent Income
import matplotlib.pyplot as plt

middlecol1, middlecol2 = st.columns(2)

with middlecol1:
    fig, ax = plt.subplots()
    sns.histplot(df['Loan Percent Income']*100, kde=True, ax=ax, binwidth=5, color='pink')
    ax.set_title('Loan Percent Income Distribution', fontsize=16, fontweight='bold')
    ax.set_xlabel('Loan Percent Income (%)', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    sns.despine()
    st.pyplot(fig)

with middlecol2:
    st.markdown("### The Loan Persons that have loan percent income more than 40%")
    High_LPI = df[df['Loan Percent Income'] > 0.4].reset_index(drop=True)
    st.table(
        High_LPI.head(9).style
        .set_properties(**{'background-color': 'white', 'color': '#014888'})
    )


