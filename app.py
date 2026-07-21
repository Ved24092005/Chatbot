from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating my prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. please respond to the question asked"),
        ("user","Question:{question}")
    ]
)


#streamlit code
st.title("Where should be begin !")
input_text = st.text_input("what question do you have")

#Now we are using LLM Model (gemma2:2b)
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

#validation based input
if input_text:
    st.write(chain.invoke({"question":input_text}))
