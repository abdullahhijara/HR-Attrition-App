import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------------------------
# Load trained model
# ---------------------------
log_reg_model = joblib.load("log_reg_model.pkl")

st.title("HR Employee Attrition Prediction")
st.write("""
This app predicts whether an employee is likely to leave the company (attrition) based on input features.
""")

# ---------------------------
# User Inputs
# ---------------------------
st.header("Employee Information")

# Numeric inputs
age = st.slider("Age", min_value=18, max_value=60, value=30)
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000)
distance_from_home = st.slider("Distance From Home (km)", min_value=1, max_value=50, value=10)
years_at_company = st.slider("Years at Company", min_value=0, max_value=40, value=5)
total_working_years = st.slider("Total Working Years", min_value=0, max_value=40, value=10)
stock_option_level = st.slider("Stock Option Level", min_value=0, max_value=3, value=0)

# Categorical inputs
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing",
                                                    "Technical Degree", "Other", "Human Resources"])
gender = st.selectbox("Gender", ["Male", "Female"])
job_role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician",
                                    "Manufacturing Director", "Healthcare Representative",
                                    "Manager", "Sales Representative", "Research Director", "Human Resources"])
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
overtime = st.selectbox("OverTime", ["No", "Yes"])

# ---------------------------
# Prepare input dataframe
# ---------------------------
input_dict = {
    "Age": age,
    "MonthlyIncome": monthly_income,
    "DistanceFromHome": distance_from_home,
    "YearsAtCompany": years_at_company,
    "TotalWorkingYears": total_working_years,
    "StockOptionLevel": stock_option_level,
    # One-hot columns (will be aligned automatically)
    f"BusinessTravel_{business_travel}": 1,
    f"Department_{department}": 1,
    f"EducationField_{education_field}": 1,
    f"Gender_{gender}": 1,
    f"JobRole_{job_role}": 1,
    f"MaritalStatus_{marital_status}": 1,
    f"OverTime_{overtime}": 1
}

user_input = pd.DataFrame([input_dict])

# Align columns with training
model_features = log_reg_model.feature_names_in_

for col in model_features:
    if col not in user_input.columns:
        user_input[col] = 0

user_input = user_input[model_features]

# ---------------------------
# Predict
# ---------------------------
if st.button("Predict Attrition"):
    prediction = log_reg_model.predict(user_input)[0]
    prediction_prob = log_reg_model.predict_proba(user_input)[0][1]

    if prediction == 1:
        st.error(f"The employee is likely to leave (Attrition). Probability: {prediction_prob:.2f}")
    else:
        st.success(f"The employee is likely to stay. Probability of leaving: {prediction_prob:.2f}")
