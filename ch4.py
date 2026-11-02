import streamlit as st
import pandas as pd
import numpy as np


df=pd.read_csv("data.csv",encoding="ISO-8859-1")
st.title("Chapter-4")
st.write(df.head(5))

file= st.file_uploader("Upload your file",type=["csv","xlsx"])

st.write(df.describe())