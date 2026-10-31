import streamlit as st 
import pandas as pd


st.title("Chapter-2 ")

if st.button("Visit"):
    tea=st.selectbox("select your tea",["green tea","hot leamon with honey","black tea","milk tea","chamomile tea","earl grey tea","oolong tea","white tea","herbal tea","matcha tea"])
    st.write(f"you have selected {tea} you have a great taste!")

st.slider("How much sugar do you want in your tea",0,10,5)

cups=st.number_input("How many cups of tea do you want to drink",1,10,5)

name=st.text_input("Enter your name")
if name:
    st.write(f"Welcome {name} your chai is being brewed!")


from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Current time: {current_time}")



date_of_birth = st.date_input(
    "Enter your date of birth",
    min_value=datetime(1900, 1, 1).date(),
    max_value=datetime.now().date()
)
if date_of_birth:
    age= datetime.now().date()-date_of_birth
    st.write(f"Your age is {age.days//365} years and {age.days%365} days")  
