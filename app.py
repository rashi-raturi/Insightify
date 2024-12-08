import streamlit as st
from codeRender import *
from model import *
from processing import *
from views import *


st.title('Diagrammify')
st.write('This app summarizes your pdf through diagrams. Upload your pdf and see the magic!')
st.divider()

with st.sidebar:
    
    file = st.file_uploader('Upload a file')
    choices()

if file: 
    file_content = extract_text(file)
    if file_content: 
        completions = run_model(file_content)
        output = get_output(completions)

        mermaid_code = extract_mermaid(output)
        print(mermaid_code)
        if mermaid_code: render_mermaid(mermaid_code)

# print(output)
# if(file): render_mermaid(file)




