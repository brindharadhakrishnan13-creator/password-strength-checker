import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add a special character.")

    st.write("### Result")

    if score == 5:
        st.success("✅ Strong Password")
    elif score >= 3:
        st.warning("🟡 Medium Password")
    else:
        st.error("🔴 Weak Password")

    if feedback:
        st.write("### Suggestions")
        for item in feedback:
            st.write(item)