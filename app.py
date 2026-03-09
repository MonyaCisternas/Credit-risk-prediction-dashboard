import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title = "Credit Risk Prediction Dashboard", page_icon = "📊", layout = "centered")
st.title("Credit Risk & Default Prediction Dashboard")
st.write("Enter borrower information to predict credit risk.")
st.markdown("---")
col1, col2 = st.columns(2)
model = joblib.load("credit_risk_model.pkl")

# Borrower Input Section
with col1:
    st.subheader("Borrower Information")
    age = st.slider("Age", 18, 80, 35)
    income = st.number_input("Monthly Income", value = 5000)
    debt_ratio = st.slider("Debt Ratio", 0.0, 1.0, 0.3)
    utilization = st.slider("Credit Utilization", 0.0, 1.0, 0.4)
    late_payments = st.number_input("Total Late Payments", 0, 50)
    credit_lines = st.number_input("Open Credit Lines", 0, 20)
    real_estate = st.number_input("Real Estate Loans", 0, 10)

input_data = pd.DataFrame([[
    age,
    income,
    debt_ratio,
    utilization,
    late_payments,
    credit_lines,
    real_estate
]], columns=[
    "age",
    "monthly_income",
    "debt_ratio",
    "revolving_utilization",
    "total_late_payments",
    "open_credit_lines",
    "real_estate_loans"
])

# Risk label mapping
risk_labels = {
    0: "High Risk",
    1: "Low Risk",
    2: "Medium Risk",
    3: "Very High Risk",
    4: "Very Low Risk"
}

# Risk order for probabilities
risk_order = [
    "High Risk",
    "Low Risk",
    "Medium Risk",
    "Very High Risk",
    "Very Low Risk"
]

# Prediction Output Section
with col2:
    st.subheader("Prediction Results")
    if st.button("Predict Risk Segment"):
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        st.metric(label="Predicted Risk Category", value=risk_labels[prediction])
        
        if prediction == 3 or prediction == 0:
            st.error("⚠️ High credit risk detected")
        elif prediction == 2:
            st.warning("⚠️ Medium credit risk")
        else:
            st.success("✓ Low credit risk borrower")

        st.subheader("Risk Probability Distribution")
        prob_df = pd.DataFrame({
            "Risk Category": risk_order,
            "Probability": probabilities * 100
        })

        st.bar_chart(prob_df.set_index("Risk Category"))
        st.write(prob_df.style.format({"Probability": "{:.2f}%"}))
        risk_score = probabilities[prediction] * 100
        st.metric(label="Model Confidence", value = f"{risk_score:.1f}%")
        st.progress(int(risk_score))