import streamlit as st
import random
import time
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load Lottie animations
money_animation = load_lottie_url("https://lottie.host/687f59a0-0c20-44ad-a81d-927f9d14b6f2/kWsZtDzAwc.json")  
idea_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_5tkzkblw.json") 
quote_animation = load_lottie_url("https://lottie.host/55c20df6-920f-4c24-a4ad-503fe7ea9836/0s4pwA90Ni.json")  

# Set page config
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSuccess {
        color: #4CAF50;
        font-size: 18px;
        font-weight: bold;
    }
    .stTitle {
        color: #FFFFFF;
        text-align: center;
    }
    .stHeader {
        color: #FFFFFF;
    }
    body {
        background-color: #1E90FF;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='stTitle'>💰 Money Making Machine</h1>", unsafe_allow_html=True)

# Instant Cash Generator Section
st.markdown("<h2 class='stHeader'>💸 Instant Cash Generator</h2>", unsafe_allow_html=True)
if st.button("Generate Money"):
    with st.spinner("Counting your money..."):
        time.sleep(2)
        amount = random.randint(1, 1000)
        st.success(f"🎉 You made ${amount}!")
        if money_animation:
            st_lottie(money_animation, height=300, key="money")


# Side Hustle Ideas Section
st.markdown("<h2 class='stHeader'>💡 Side Hustle Ideas!</h2>", unsafe_allow_html=True)
if st.button("Generate Hustle"):
    with st.spinner("Fetching a side hustle idea..."):
        try:
            response = requests.get("http://127.0.0.1:8000/side_hustles?apiKey=1234567890")
            if response.status_code == 200:
                hustles = response.json()
                idea = hustles["side_hustle"]
            else:
                idea = "Freelancing"
        except:
            idea = "Something went wrong!"
        st.success(f"🚀 {idea}")
        if idea_animation:
            st_lottie(idea_animation, height=300, key="idea")


# Money-Making Motivation Section
st.markdown("<h2 class='stHeader'>🔥 Money-Making Motivation</h2>", unsafe_allow_html=True)
if st.button("Get Motivated"):
    with st.spinner("Fetching a motivational quote..."):
        try:
            response = requests.get("http://127.0.0.1:8000/money_quotes?apiKey=1234567890")
            if response.status_code == 200:
                quotes = response.json()
                quote = quotes["money_quote"]
            else:
                quote = "Love the process!"
        except:
            quote = "Error due to some issues."
        st.success(f"💬 {quote}")
        if quote_animation:
            st_lottie(quote_animation, height=300, key="quote")



# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Amjad Afzal Ahmed")