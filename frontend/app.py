import streamlit as st
import requests
import os
from dotenv import load_dotenv



# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Adult Income Predictor",
    page_icon="💰",
    layout="wide"
)

# =========================
# API URL
# =========================

load_dotenv()
API_URL = os.getenv("API_URL")

# =========================
# Mappings (UI -> Dataset/Alias Values)
# =========================
workclass_mapping = {
    "Private Sector": "Private",
    "Local Government": "Local-gov",
    "Self Employed (Not Incorporated)": "Self-emp-not-inc",
    "Self Employed (Incorporated)": "Self-emp-inc",
    "Federal Government": "Federal-gov",
    "State Government": "State-gov",
    "Without Pay": "Without-pay",
    "Never Worked": "Never-worked"
}

marital_status_mapping = {
    "Never Married": "Never-married",
    "Married (Civ Spouse)": "Married-civ-spouse",
    "Widowed": "Widowed",
    "Divorced": "Divorced",
    "Separated": "Separated",
    "Married (Spouse Absent)": "Married-spouse-absent",
    "Married (AF Spouse)": "Married-AF-spouse"
}

education_mapping = {
    "High School Graduate": "HS-grad",
    "Some College": "Some-college",
    "11th Grade": "11th",
    "10th Grade": "10th",
    "9th Grade": "9th",
    "12th Grade": "12th",
    "1st-4th Grade": "1st-4th",
    "5th-6th Grade": "5th-6th",
    "7th-8th Grade": "7th-8th",
    "Bachelors": "Bachelors",
    "Masters": "Masters",
    "Doctorate": "Doctorate",
    "Prof School": "Prof-school",
    "Assoc Academic": "Assoc-acdm",
    "Assoc Vocational": "Assoc-voc",
    "Preschool": "Preschool"
}

race_mapping = {
    "White": "White",
    "Black": "Black",
    "Asian": "Asian-Pac-Islander",
    "Other": "Other",
    "American Indian": "Amer-Indian-Eskimo"
}

occupation_options = {
    "Machine Operator / Inspector": "Machine-op-inspct",
    "Farming / Fishing": "Farming-fishing",
    "Protective Services": "Protective-serv",
    "Other Service Jobs": "Other-service",
    "Professional Specialty": "Prof-specialty",
    "Craft Repair": "Craft-repair",
    "Admin Clerical": "Adm-clerical",
    "Executive Managerial": "Exec-managerial",
    "Tech Support": "Tech-support",
    "Sales": "Sales",
    "Private Household Service": "Priv-house-serv",
    "Transport Moving": "Transport-moving",
    "Handlers Cleaners": "Handlers-cleaners",
    "Armed Forces": "Armed-Forces"
}

# =========================
# Title
# =========================
st.title("💰 Adult Income Prediction App")
st.markdown("Predict whether income is >50K using Machine Learning")

# =========================
# Layout
# =========================
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 30)

    workclass_display = st.selectbox("Workclass", list(workclass_mapping.keys()))

    fnlwgt = st.number_input("Final Weight (fnlwgt)", 1, 1000000, 100000)

    education_display = st.selectbox("Education", list(education_mapping.keys()))

    educational_num = st.number_input("Educational Number", 1, 20, 10)

    marital_status_display = st.selectbox("Marital Status", list(marital_status_mapping.keys()))

    occupation = st.selectbox("Occupation", list(occupation_options.keys()))

with col2:
    relationship = st.selectbox(
        "Relationship",
        ['Own-child','Husband','Not-in-family','Unmarried','Wife','Other-relative']
    )

    race = st.selectbox(
        "Race",
        list(race_mapping.keys())
    )

    gender = st.selectbox("Gender", ['Male','Female'])

    capital_gain = st.number_input("Capital Gain", 0, 100000, 0)

    capital_loss = st.number_input("Capital Loss", 0, 100000, 0)

    hours_per_week = st.slider("Hours Per Week", 1, 100, 40)

    native_country = st.text_input("Native Country", "United-States")

# =========================
# Predict
# =========================

if st.button("Predict Income"):

    payload = {
        "age": age,
        "workclass": workclass_mapping[workclass_display],
        "fnlwgt": fnlwgt,
        "education": education_mapping[education_display],
        "educational-num": educational_num,
        "marital-status": marital_status_mapping[marital_status_display],
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital-gain": capital_gain,
        "capital-loss": capital_loss,
        "hours-per-week": hours_per_week,
        "native-country": native_country
    }

    try:
        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()
            prediction = int(result.get("prediction"))

            label_map = {
                0: "💼 Less than or equal to 50K",
                1: "💰 Greater than 50K"
            }

            st.success(f"Income Prediction: {label_map[prediction]}")
            st.info(f"Model Output: {prediction}")

            if prediction == 1:
                st.balloons()

        else:
            st.error("API Error")
            st.write(response.text)

    except Exception as e:
        st.error("Cannot connect to backend")
        st.write(str(e))