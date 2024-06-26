
# home.py

import streamlit as st
import time
from io import StringIO
import pdfplumber

# Functions 
def extract_data(feed):
    data = []
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_tables())
    return data



# Main page 
st.title('Aptio AI')
st.subheader('job finder! PLACE HOLDER')

radio_input = st.radio("",['Text Input','File Upload'],horizontal=True)

if radio_input == 'Text Input':
    text_input = st.text_input("Paste resume contents here",label_visibility ='collapsed',placeholder ='Paste resume contents here')

if radio_input == 'File Upload':
    file = st.file_uploader("Upload resume contents",type=['doc','docx','pdf','txt'])
    if file:
        file_data = extract_data(file)
        st.write(file_data)



