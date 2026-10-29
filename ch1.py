import streamlit as st
import pandas as pd 
st.title("Welcome to F1")
st.subheader("This is developed in streamlit")
st.text("Welcome to the Home")
st.write("Hello my name is kabin")

st.write("Table using pandas")
st.write(pd.DataFrame({
    "firstcol":[1,2,3,4],
    "secondcol":[10,20,30,40] 
}))

chai=st.selectbox("select your tea",["green tean","hot leamon with honey","black tea","milk tea"])


st.write(f"You selected {chai} you have a great taste!") 
st.success("You have selected the best tea! ") 



language=st.selectbox("select your fav language",["python","java","c++","javascript","c#","ruby","php","go","swift","kotlin "])
st.write(f"You selected {language} you have a great taste!")

st.success("You hacve selected the on eof the best language ")