
Live link

# Customer Churn Prediction

## 1. Project Overview

Customer churn is one of the major challenges faced by telecom companies. When customers discontinue their subscriptions, the company loses recurring revenue and must spend additional resources to acquire new customers.

The traditional approach to churn management is reactive: the company identifies a customer only after they have already cancelled their service.

This project focuses on building a **proactive Customer Churn Prediction System** that uses historical customer data and machine learning to identify customers who are likely to churn before they leave.

The system predicts the probability of churn for each customer and converts that probability into a practical business decision such as:

- Low Risk → No immediate action
- Medium Risk → Monitor the customer
- High Risk → Contact the customer with a retention offer

The project covers the complete machine learning lifecycle:

**Data Understanding → EDA → Data Preprocessing → Model Development → Model Comparison → Hyperparameter Tuning → Business Evaluation → Model Interpretation → Deployment**

---

# 2. Business Problem

XYZ Telecom is a mid-sized telecom company with approximately 50,000 active customers.

Over the past year, the company has noticed that a significant number of customers are cancelling their subscriptions.

Currently, the retention team reacts after customers have already left.

The company wants to change this approach and identify customers who are likely to churn **before cancellation occurs**.

The retention team can use this information to provide:

- Discounts
- Better plans
- Additional services
- Loyalty benefits
- Personalized retention offers

However, the retention team has limited capacity and cannot contact every customer.

The team can contact approximately **10–20% of customers**.

Therefore, the goal is not simply to build a model with high accuracy.

The actual business objective is:

> **Identify and prioritize the customers with the highest probability of churn so that the retention team can use its limited resources effectively.**

---

# 3. Problem Statement

Build a machine learning classification system that takes customer information as input and predicts whether the customer is likely to churn.

The system should provide:

1. Churn probability
2. Churn prediction
3. Risk category
4. Recommended business action

Example:

```text
Customer
    ↓
Customer Information
    ↓
Machine Learning Model
    ↓
Churn Probability: 78%
    ↓
Risk Level: HIGH
    ↓
Contact Customer


PROJECT STRUCTURE

Churn Prediction Model/
│
├── app.py
│
├── customer_churn_pipeline.pkl
│
├── Customer_churn_prediction_model.ipynb
│
├── CustomerChurn.csv
│
├── .gitignore
│
└── README.md
