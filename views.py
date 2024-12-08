import streamlit as st
from codeRender import *
from model import *
from processing import *

def side_bar():
    with st.sidebar:
        file = st.file_uploader('Upload a file')
        st.divider()

        choice = choices()
        # to make diagrams
        if choice == 'Diagrammize':
            if file: 
                file_content = extract_text(file)
                if file_content: 
                    completions = run_model(file_content)  # generating by feeding to model
                    output = get_output(completions)    # extracting output given by model

                    mermaid_code = extract_mermaid(output)  # extracting mermaid code from it enclosed in ```
                    if mermaid_code: render_mermaid(mermaid_code) 
                else:
                    st.error('Cannot recognize text!')

        elif choice == 'Summarize':
            pass

        else:
            pass




def choices():
    choice = st.radio(
     "Select an action to perform",
     ["Diagrammize", "Summarize", "Chat with the text"],
     captions=[
         "Creates a diagram from the information.",
         "Summarizes and gives key insights.",
         "Get detailed explainations, get your queries resolved.",
     ])
    
    return choice