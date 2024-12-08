import pdfplumber as pp

def extract_text(pdf):
    with pp.open(pdf) as file:
        return "".join(page.extract_text() for page in file.pages)
    
def extract_mermaid(output):
    import re

    matches = re.findall(r'```mermaid(.*?)```', output, re.DOTALL)
    
    code = ''
    for match in matches:
        code += match.strip()
    
    return code

