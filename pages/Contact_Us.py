import streamlit as st


st.header("Contact Me")

with st.form(key="Email_Form"):
    user_email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")