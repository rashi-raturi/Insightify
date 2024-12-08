from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv('API_KEY')
)

def run_model(data):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages = [
                {"role": "system", "content": "You are a professional professor and an expert that creates detailed diagram to explain the following text using diagrams/flowcharts in mermaid format .When an input is given to you, you will return 3 things. 1. Mermaid code for the diagram/flowchart enclosed in triple quotes. 2. Summary in less than 100 words 3. Key insights from the text  4. 3 Questions for the user to revise or related to that text. Do not write anything else in the beginning or end except that. Use H3 headings."},
                {"role": "user", "content": f"Here is your text information: {data}"}
        ],
        temperature=0.5,
        max_tokens=8000,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    return completion


def get_output(completion):
    output = ''
    for chunk in completion:
        output += chunk.choices[0].delta.content or ""

    return output

    


