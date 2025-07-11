import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")
st.title("Chatbot_deploy")

# セッション状態にチャット履歴を保存
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャット履歴を表示
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ユーザーからの入力を受け取る
user_input = st.chat_input("talk to me...I'm the real chatbot!")

if user_input:
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # バックエンド API にリクエストを送信
    try:
        st.write(st.session_state.messages)
        response = requests.post(
            "http://backend:5000/api/chat",
            json={"message": st.session_state.messages},
            timeout=10
        )
        
        response.raise_for_status()
        st.write(response.raise_)
        data = response.json()
        reply = data["response"]
    except Exception as e:
        reply = f"opps! There seems to be an error: {e}"

    # アシスタントの返答を追加
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)


