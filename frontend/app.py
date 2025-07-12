import streamlit as st
import requests


# Retrieve history only once at app startup
if "messages" not in st.session_state:
    try:
        res = requests.get("http://backend:5000/api/chat/history")
        res.raise_for_status()
        st.session_state.messages = res.json()
    except Exception as e:
        st.session_state.messages = []
        st.error(f'error occured: {e}')


def clear_chat_and_save():
    # send the empty list to the backend
    try:
        requests.post(
            "http://backend:5000/api/chat",
            json={"message": []},
            timeout=5
        )
    except Exception as e:
        st.error(f"Error!: {e}")

    # clearing up the local session_state.messages too
    st.session_state.messages.clear()


st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")
st.title("Chatbot")
tabs = st.tabs(['Default chat room'])
st.button("clear chat",on_click=clear_chat_and_save)

# チャット履歴を表示
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# get the user input?
user_input = st.chat_input("talk to me...I'm the real chatbot!")

if user_input:
    # append user input to the conversation
    st.session_state.messages = st.session_state.messages + [{"role": "user", "content": user_input}]
    with st.chat_message("user"):
        st.markdown(user_input)

    # send request to the backend API
    try:
        response = requests.post(
            "http://backend:5000/api/chat",
            json={"message": st.session_state.messages},
            timeout=10
        ) 
        response.raise_for_status()
        reply = response.json()["response"]

    except Exception as e:
        reply = f"opps! There seems to be an error: {e}"

    # アシスタントの返答を追加
    st.session_state.messages = st.session_state.messages + [{"role": "assistant", "content": reply}]
    with st.chat_message("assistant"):
        st.markdown(reply)


