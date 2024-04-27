import streamlit as st
import os 
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint

load_dotenv()


def get_response(input_text):
    huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    llm=HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct',huggingfacehub_api_token=huggingfacehub_api_token)
    response = llm.invoke(input_text)
    return response


def main():
    st.title("Hugging Face Chat")

    input_text = st.text_area("Enter your question : ")

    if st.button("Submit"):
        if input_text.strip() != "":
            response = get_response(input_text)
            st.write(">>", response)
        else:
            st.warning("Please enter a question.")

if __name__=="__main__":
    main()


