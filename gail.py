import streamlit as st
import random
import time


st.set_page_config(page_title="GAIL Mental Wellness Assistant")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/3_Dashboard.py")
else:
    st.switch_page("pages/1_Login.py")


