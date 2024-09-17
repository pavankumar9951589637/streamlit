import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Add a slider
age = st.slider("Select your age:", 1, 100, 25)

# Display the input
if name:
    st.write(f"Hello, {name}! You are {age} years old.")
