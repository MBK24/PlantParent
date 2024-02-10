import langchain_helper as lch 
import streamlit as st
import textwrap

st.title("Plant Parent IO")

with st.sidebar:
    with st.form(key='my_form'):
        typeOfPlant = st.sidebar.text_area("What is the name of the plant?", max_chars=50)
        question = st.sidebar.text_area(label="What would you like to know?", max_chars=50, key="question")
        submitButton = st.form_submit_button(label="Submit")

if question and typeOfPlant:
    response = lch.plant(typeOfPlant, question)
    st.subheader("Answer:")
    
    # Assuming the value you want to display is in the 'answer' key
    answer_text = response.get('answer', '')
    
    st.text(textwrap.fill(answer_text, width=80))