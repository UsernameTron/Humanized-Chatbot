import streamlit as st
import requests

# API Key setup
XAI_API_KEY = "xai-0KzIQnwRuPlJuvn4F3gbJo1wEnxRib2ws9PI2EEUMq89vt4xbHMmPLSx9jNDsxI5urhhKgEh2cPwrPXx"

# Chatbot function
def chatbot_response(user_message):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {XAI_API_KEY}"}
    data = {
        "messages": [
            {"role": "system", "content": "You are a friendly, empathetic chatbot."},
            {"role": "user", "content": user_message}
        ],
        "model": "grok-beta",
        "temperature": 0.8
    }
    response = requests.post(url, headers=headers, json=data).json()
    return response["choices"][0]["message"]["content"]

# Streamlit interface
st.title("Empathetic Chatbot with Sentiment Analysis")
st.write("Welcome! Ask me anything below:")

user_message = st.text_input("Your message:")
if user_message:
    response = chatbot_response(user_message)
    st.write(f": {response}")