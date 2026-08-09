import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("customer_churn_pipeline.pkl")


# ============================================================
# HEADER
# ============================================================

st.title("Customer Churn Prediction System")

st.write(
    "Enter the customer's information below to estimate "
    "their probability of churn."
)

st.divider()


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.header("Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12,
        step=1
    )

with col2:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

with col3:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=600.0,
        step=10.0
    )


col1, col2, col3 = st.columns(3)

with col1:
    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

with col2:
    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

with col3:
    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


# ============================================================
# CONTRACT & BILLING
# ============================================================

st.divider()
st.header("Contract & Billing")

col1, col2, col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

with col2:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

with col3:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer",
            "Credit card"
        ]
    )


# ============================================================
# PHONE & INTERNET SERVICES
# ============================================================

st.divider()
st.header("Phone & Internet Services")

col1, col2, col3 = st.columns(3)

with col1:
    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

with col2:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No phone service",
            "No",
            "Yes"
        ]
    )

with col3:
    internet_service = st.selectbox(
        "Internet Service",
        [
            "No",
            "DSL",
            "Fiber optic"
        ]
    )


# ============================================================
# ADDITIONAL SERVICES
# ============================================================

st.divider()
st.header("Additional Services")

col1, col2 = st.columns(2)

with col1:

    online_security = st.selectbox(
        "Online Security",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )

with col2:

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "No internet service",
            "No",
            "Yes"
        ]
    )


st.divider()


# ============================================================
# CREATE CUSTOMER DATAFRAME
# ============================================================

customer = pd.DataFrame({
    "Senior Citizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "Tenure": [tenure],
    "Phone Service": [phone_service],
    "Multiple Lines": [multiple_lines],
    "Internet Service": [internet_service],
    "Online Security": [online_security],
    "Online Backup": [online_backup],
    "Device Protection": [device_protection],
    "Tech Support": [tech_support],
    "Streaming TV": [streaming_tv],
    "Streaming Movies": [streaming_movies],
    "Contract": [contract],
    "Paperless Billing": [paperless_billing],
    "Payment Method": [payment_method],
    "Monthly Charges": [monthly_charges],
    "Total Charges": [total_charges]
})


# ============================================================
# PREDICTION
# ============================================================

st.header("Churn Prediction")

predict_button = st.button(
    "Predict Churn",
    type="primary",
    use_container_width=True
)


if predict_button:

    # Get probability of Churn = Yes
    probability = model.predict_proba(customer)[0][1]


    # ========================================================
    # RISK CLASSIFICATION
    # ========================================================

    if probability >= 0.60:

        prediction = "Likely to Churn"
        risk = "HIGH"
        action = "Contact customer with retention offer"

    elif probability >= 0.40:

        prediction = "Moderate Churn Risk"
        risk = "MEDIUM"
        action = "Monitor customer and consider engagement"

    else:

        prediction = "Likely to Stay"
        risk = "LOW"
        action = "No immediate action"


    # ========================================================
    # RESULT
    # ========================================================

    st.divider()

    st.subheader("Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

    with col2:

        st.metric(
            "Risk Level",
            risk
        )

    with col3:

        st.metric(
            "Prediction",
            prediction
        )


    # ========================================================
    # PROBABILITY BAR
    # ========================================================

    st.write("### Churn Risk")

    st.progress(
        float(probability),
        text=f"Churn Probability: {probability * 100:.2f}%"
    )


    # ========================================================
    # BUSINESS RECOMMENDATION
    # ========================================================

    if risk == "HIGH":

        st.error(
            f"🔴 HIGH RISK\n\n"
            f"**Recommended Action:** {action}"
        )

    elif risk == "MEDIUM":

        st.warning(
            f"🟠 MEDIUM RISK\n\n"
            f"**Recommended Action:** {action}"
        )

    else:

        st.success(
            f"🟢 LOW RISK\n\n"
            f"**Recommended Action:** {action}"
        )


    # ========================================================
    # CUSTOMER INFORMATION PREVIEW
    # ========================================================

    with st.expander("View Customer Information"):

        st.dataframe(
            customer,
            use_container_width=True
        )


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.caption(
        "This prediction is based on patterns learned from "
        "historical customer data. It is a decision-support "
        "tool and does not guarantee future customer behavior."
    )