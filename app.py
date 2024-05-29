'''import streamlit as st
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
        st.write("Please enter a question.")'''
import streamlit as st
import openai


openai.api_key = st.secrets["sk-proj-49djuWDxDdMfseFzHufwT3BlbkFJUmOr3Q2fIxAeUZM6LzzO"]


@st.cache(allow_output_mutation=True)
def get_gpt3_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']


if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

def save_input():
    st.session_state.user_input = st.session_state.input_area


st.title("GPT-3.5 Turbo Chatbot")

st.text_area("Ask a question:", key='input_area', on_change=save_input)

if st.button("Get Response"):
    if st.session_state.user_input:
        response = get_gpt3_response(st.session_state.user_input)
        st.write("Response from GPT-3.5 Turbo:")
        st.write(response)
    else:
        st.write("Please enter a question.")

