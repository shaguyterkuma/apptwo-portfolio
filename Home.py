from tkinter import Image

import row
import streamlit as st
import pandas
from PIL import Image
from PIL.ImageOps import expand

col1,col2 = st.columns(2)
col3 = st.columns(1)

with col1:
    img = Image.open("images/IMG_7589.jpg")
    rot_img = img.rotate(-90,expand=True)
    st.image(rot_img)

with col2:
    st.title("Terkuma Sesugh Shaguy")
    content = """
    Hello my name is Terkuma Sesugh Shaguy and i hope to work for microsoft one day and i want to go to MIT and make my family proud in every way possible i want to marry a
    woman who values me and we look forward to eachothers goals and reach them together as a couple    
    """
    st.write(content)


morestuff = """Below you can find some of the apps I have built in python , Feel free to contact me """
st.write(morestuff)

col4,col_m,col5 = st.columns([1.5,0.5,1.5]) #The numbers represent the ratio dimensions of the columns The first colum would be three times wider than the middle column adn the first and the third column are the same width

df = pandas.read_csv("data.csv",sep=";")

with col4:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")



with col5:
    for index,row in df[10:20].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image( "images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

