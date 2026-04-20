import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📧 Email Spam Classifier")

user_input = st.text_area("Paste your email text here:")

if st.button("Classify"):
    if user_input.strip() != "":
        features = vectorizer.transform([user_input])
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.error("🚨 Spam Detected")
        else:
            st.success("✅ Safe Email")
    else:
        st.warning("Please enter some text to classify.")
