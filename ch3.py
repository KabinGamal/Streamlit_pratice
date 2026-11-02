import streamlit as st 
st.title("Home Page")
col1 ,col2 = st.columns(2)



with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBkebSFFrm0CMQEgmCazWtkyT02VcojQOGfPZoDhpEqw&s=10",width=200)

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRoYf4tMsqMwkbOuy_Kr5Ymh8ULI0lRGPyH9J6nVsz8g&s=10",width=200)

if col1:
    st.write("Redbull")

if col2:
    st.write("Ferrerai")

name=st.sidebar.text_input("Enter your name:")
tea=st.sidebar.selectbox("select your tea",["green tea","hot leamon with honey","black tea","milk tea","chamomile tea","earl grey tea","oolong tea","white tea","herbal tea","matcha tea"])
if name:
    st.write(f"Welcome {name} your chai is being brewed!")

with st.expander("Click here to see the table"):
    st.write(""" 
    1. Boil water 
    2. Add tea leaves or tea bag
    3. Let it steep for 3-5 minutes
    """)

    