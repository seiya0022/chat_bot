import streamlit as st
import requests


# アプリ起動時に一度だけ履歴を取得
if "messages" not in st.session_state:
    try:
        res = requests.get("http://backend:5000/api/chat/history")
        res.raise_for_status()
        st.session_state.messages = res.json()
    except Exception as e:
        st.session_state.messages = []
        st.error(f'error occured: {e}')

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")
st.title("Chatbot")
tabs = st.tabs(['Default chat room'])


def clear_chat_and_save():
    # 空の履歴をバックエンドに送信
    try:
        requests.post(
            "http://backend:5000/api/chat",
            json={"message": []},
            timeout=5
        )
    except Exception as e:
        st.error(f"エラー: {e}")

    # ローカルのセッションもクリア
    st.session_state.messages.clear()


st.button("clear chat",on_click=clear_chat_and_save)
# st.button("session_state", on_click=lambda: st.write(st.session_state))

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
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)


