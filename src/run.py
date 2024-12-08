import streamlit as st

st.image("github.svg", width=702)
st.title(':zap: Github Profile Readme Generator')

# Personal Info
st.header('Personal Info')
with st.expander('Persona Info'):
    col1, col2 = st.columns(2)
    name = col1.text_input('Name')
    location = col2.text_input('Location')
    phone = col1.text_input('Phone')
    homepage = col2.text_input('Homepage')
    email = st.text_input('Email')
    
# Social Media
st.header('Social Media')
with st.expander('Social Media'):
    col1, col2 = st.columns(2)
    name = col1.text_input('Name')
    location = col2.text_input('Location')
    phone = col1.text_input('Phone')
    homepage = col2.text_input('Homepage')
    email = st.text_input('Email')