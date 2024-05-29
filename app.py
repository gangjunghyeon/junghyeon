import streamlit as st
import openai


openai.api_key = st.secrets[sk-proj-49djuWDxDdMfseFzHufwT3BlbkFJUmOr3Q2fIxAeUZM6LzzO]

def get_gpt3_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']


st.title("GPT-3.5 Turbo Chatbot")

user_input = st.text_area("Ask a question:")

if st.button("Get Response"):
    if user_input:
        response = get_gpt3_response(user_input)
        st.write("Response from GPT-3.5 Turbo:")
        st.write(response)
    else:
        st.write("Please enter a question.")
