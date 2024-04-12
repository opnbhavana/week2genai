from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=""
);

currentData = []

def get_prompt(prompt, newdata):
    curr = newdata
    curr.append({"role": "user", "content":prompt})
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=curr
    )
    curr.append({"role": "system", "content": completion.choices[0].message.content})
    for data in curr:
        st.title(data["role"]+":")
        st.markdown(data["content"])

st.title("Language Learning Assistent")

prompt = st.text_input('Enter Text:')

if prompt:
    response = get_prompt(prompt, currentData)