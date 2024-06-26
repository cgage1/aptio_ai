
# home.py

import streamlit as st
import time

st.title('Aptio AI')


if st.radio("",['Text Input','File Upload'],horizontal=True):
    file = st.file_uploader("Upload your data")
    if file:
        with st.spinner("Processing your file"):
            time.sleep(5) #<- dummy wait for demo. 

text_input = st.chat_input("What u want")

