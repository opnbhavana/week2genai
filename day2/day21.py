from openai import OpenAI
import streamlit as st
import time


client = OpenAI(
    api_key=""
);

def get_prompt(prompt):
    response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=2,
    )
    return response.data

st.title("image generator app")

with st.sidebar:
    st.title("powred by Open AI")
    st.write("This is an app")

prompt = st.text_input('enter image description')

if prompt:
    image_response = get_prompt(prompt)
    with st.spinner('Wait for it...'):
        time.sleep(5)
    for x in image_response:
        st.image(x.url)
