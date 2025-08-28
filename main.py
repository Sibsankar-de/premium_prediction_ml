import streamlit as st
from prediction_helper import predict

st.title("Insurance Information Form")

# Row 1 (Numeric fields)
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col2:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=15, step=1)

# Row 2 (Numeric field + Dropdown)
col1, col2 = st.columns(2)
with col1:
    income_lakhs = st.number_input("Annual Income (in Lakhs)", min_value=0.0, max_value=100.0, step=0.5)
with col2:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=10, step=1)

# Row 3
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ['Male', 'Female'])
with col2:
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

# Row 4
col1, col2 = st.columns(2)
with col1:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
with col2:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])

# Row 5
col1, col2 = st.columns(2)
with col1:
    smoking_status = st.selectbox("Smoking Status", [
        'No Smoking', 'Regular', 'Occasional',
        'Smoking=0', 'Does Not Smoke', 'Not Smoking'
    ])
with col2:
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])

# Row 6
col1, col2 = st.columns(2)
with col1:
    medical_history = st.selectbox("Medical History", [
        'Diabetes', 'High blood pressure', 'No Disease',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ])
with col2:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

# Row 7 (Genetical Risk)


# Store inputs in dictionary
input_dict = {
    'Age': age,
    'Gender': gender,
    'Region': region,
    'Marital_status': marital_status,
    'Number Of Dependants': number_of_dependants,
    'BMI_Category': bmi_category,
    'Smoking_Status': smoking_status,
    'Employment_Status': employment_status,
    'Income_Lakhs': income_lakhs,
    'Medical History': medical_history,
    'Insurance_Plan': insurance_plan,
    'Genetical_Risk': genetical_risk
}

# Example use: trigger storing on submit
if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")
    
    
