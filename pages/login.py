import streamlit as st

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "test" and password == "1234":
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Logged in!")
        st.switch_page("pages/2_Questionnaire.py")
    else:
        st.error("Invalid credentials.")

