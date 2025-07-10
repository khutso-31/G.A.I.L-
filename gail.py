import streamlit as st
import random
import time



Basic setup
st.set_page_config(page_title="GAIL - Wellness Assistant", layout="centered")
st.title("💬 G.A.I.L. - Mental Wellness Assistant")
st.markdown("Hi, I'm GAIL! Your mental wellness companion. Let's talk 🌻")

# Sample wellness tips
tips = [
    "🧘🏽‍♀️ Breathe deeply. Inhale calm, exhale stress.",
    "☀️ Take a walk outside. Even 10 minutes helps.",
    "📒 Write down what you're grateful for today.",
    "📵 Unplug for a while. You deserve quiet.",
    "🎧 Play your favorite feel-good song.",
]

# Chat simulation
user_input = st.text_input("Type how you're feeling today:")

if user_input:
    with st.spinner("GAIL is thinking..."):
        time.sleep(1.5)

    st.success(f"Thank you for sharing that. I’m here with you. 💙")

    st.markdown("🔁 Here's something you can try:")
    st.info(random.choice(tips))
