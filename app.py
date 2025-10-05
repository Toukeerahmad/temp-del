import streamlit as st

# Page configuration
st.set_page_config(page_title="My First Streamlit App", page_icon="✨", layout="centered")

# Title and header
st.title("✨ Welcome to My Streamlit App!")
st.header("A simple app ready for deployment")

# Simple input and output
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider example
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# Checkbox example
if st.checkbox("Show a fun fact"):
    st.info("Streamlit makes it super easy to build web apps in pure Python!")

# Footer
st.markdown("---")
st.write("Deployed on Streamlit Cloud 🚀")
