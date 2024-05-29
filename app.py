import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_gpt3_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Streamlit UI 설정
st.title("GPT-3.5 Turbo Chatbot")

user_input = st.text_area("Ask a question:")

if st.button("Get Response"):
    if user_input:
        response = get_gpt3_response(user_input)
        st.write("Response from GPT-3.5 Turbo:")
        st.write(response)
    else:
        st.write("Please enter a question.")
