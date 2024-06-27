#
# home.py
# 

import streamlit as st
import time
from io import StringIO
from meta_ai_api import MetaAI   # https://github.com/Strvm/meta-ai-api/blob/main/README.md 
ai = MetaAI()
from PyPDF2 import PdfReader
from docx import Document

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file):
    text = file.read().decode("utf-8")
    return text

def file_read():
    uploaded_file = st.file_uploader("Upload resume", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "pdf":
            content = read_pdf(uploaded_file)
        elif file_extension == "docx":
            content = read_docx(uploaded_file)
        elif file_extension == "txt":
            content = read_txt(uploaded_file)
        else:
            st.error("Unsupported file type")
            return
        
        # st.write(content)
        return content 

# add custom inputs?
# add location inputs, mb as example? 


# Main page 
st.title('Aptio AI')
st.write('#### Enter your resume below and find jobs :mag_right:')

radio_input = st.radio("",['Text Input','File Upload'],horizontal=True)

if radio_input == 'Text Input':
    resume_str = st.text_input("Paste resume contents here",label_visibility ='collapsed',placeholder ='Paste resume contents here')

if radio_input == 'File Upload':
    resume_str = file_read()


prompt = f"""
    List the top 20 currently open jobs near Carlsbad, CA that would be best suited for someone with the resume below. Score the job 
     opportunities on a scale of 1-100 and include the link to the job opening and sort by score:  
    {resume_str}
    """

if st.button("Find jobs!"):
    with st.status('Scouring web...'):
        response = ai.prompt(message=prompt)
        
    st.write(response)




