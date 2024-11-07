import streamlit as st
import google.generativeai as genai

from api_key import api_key

GOOGLE_API_KEY = api_key

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")

def main():
    st.set_page_config(page_title="Python Code Generator")
    
    st.markdown("""
    <div style="text-align: center;">
        <h1>Python Query Generator</h1>
        <h3>I can generate Python code for you!</h3>
        <h4>With Explanation as well!!!</h4>
        <p>This tool generates Python code based on your plain English description.</p>
    </div>    
    """, unsafe_allow_html=True)

    text_input = st.text_area("Enter your Python code description in Plain English:")

    submit = st.button("Generate Python Code")

    if submit:
        if text_input.strip() == "":
            st.warning("Please enter a valid query description.")
        else:
            with st.spinner("Generating Python code..."):
                template = """
                    Create a Python code snippet to execute based on the following description:

                    Description: {text_input}

                    Output: Python code to generate the wanted program from the descprition.
                """

                formatted_template = template.format(text_input=text_input)
                response=model.generate_content(formatted_template)

                with st.container():
                    st.success("Python Code generated succesfully! Here is your code below:")
                pyhton_query = response.text
                st.write(pyhton_query)

                pyhton_query = pyhton_query.strip().lstrip("```python").rstrip("```")



                explanation = """
                    Explain this Pyhton code:
                    ...
                    {pyhton_query}
                    ...
                    Please provide with simplest of explanation:
                
                """
                explanation_formatted = explanation.format(pyhton_query = pyhton_query)
                explanation = model.generate_content(explanation_formatted)
                explanation = explanation.text
                st.write(explanation)

main()

              

                