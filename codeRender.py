import streamlit as st
import streamlit.components.v1 as components

def render_mermaid(code):
    mermaid_html = f"""
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{startOnLoad:true}});
            
            function downloadDiagram() {{
                const svgElement = document.querySelector('svg');
                const serializer = new XMLSerializer();
                const source = serializer.serializeToString(svgElement);

                const blob = new Blob([source], {{type: 'image/svg+xml'}});
                const url = URL.createObjectURL(blob);

                // Create a download link
                const a = document.createElement('a');
                a.href = url;
                a.download = 'diagram.svg';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }}
        </script>
        <style>
            .mermaid {{
                width: 100%;
                height: auto;
            }}
            .download-btn {{
                margin-top: 10px;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
            }}
            .download-btn:hover {{
                background-color: #45a049;
            }}
        </style>
    </head>
    <body>
        <div class="mermaid">
            {code}
        </div>
        <button class="download-btn" onclick="downloadDiagram()">Download Diagram as SVG</button>
    </body>
    </html>
    """
    components.html(mermaid_html, height=1000, scrolling=False)

