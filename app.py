import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
     page_title='Linear models and their presentation by AI Education final project',
     layout='wide',
     initial_sidebar_state='expanded',
)

def intro():
    st.markdown('''
        # Welcome to "Linear models and their presentation" 👋

        Aim of this course is to learn what linear models are, how to 
        build and interpret them. This course is organized by [AI Education](https://github.com/aiedu-courses) team. 
        Final project that you're seing right now is made by me, [@timofann](https://github.com/timofann).
        Feel free to write or contribute if you have some questions about project, issues, ideas for improvement or offers.

        **👈 Select a stage from the dropdown on the left** to see all
        of what we've learnt!
    '''
    )

def eda():
    st.text('eda')

def baseline():
    st.text('baseline')

def model():
    st.text('model')

def predict():
    st.text('predict')

page_names_to_funcs = {
    "---": intro,
    "EDA": eda,
    "Baseline": baseline,
    "Ready model": model,
    "Try it now": predict
}

stage_name = st.sidebar.selectbox("Choose a stage", page_names_to_funcs.keys())

page_names_to_funcs[stage_name]()