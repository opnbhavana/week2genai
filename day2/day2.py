from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=""
);

def get_prompt(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=2,
    )
    return response.data[0]

st.title("image generator app")

with st.sidebar:
    st.title("powred by Open AI")
    st.write("This is an app")

prompt = st.text_input('enter image description')

if prompt:
    image_response = get_prompt(prompt)
    if image_response:
        st.image(image_response.url)
    else:
        st.write("loading...")