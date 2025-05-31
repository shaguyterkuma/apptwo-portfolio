import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Terkuma Sesugh Shaguy")
    content = """
    Hello my name is Terkuma Sesugh Shaguy and i hope to work for microsoft one day and i want to go to MIT and make my family proud in every way possible i want to marry a
    woman who values me and we look forward to eachothers goals and reach them together as a couple    
    """
    st.write(content)