import streamlit as st

def side_bar():
    with st.sidebar:
        file = st.file_uploader('Upload a file')

        st.divider()



def choices():
    genre = st.radio(
     "Select an action to perform",
     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
     captions=[
         "Laugh out loud.",
         "Get the popcorn.",
         "Never stop learning.",
     ])