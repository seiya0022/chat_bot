from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from datetime import datetime
import json

load_dotenv()   # load .env file
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)
CORS(app)

def get_conn():
    return psycopg2.connect(
        host='db',
        dbname='chat_db',
        user='user',
        password='password',
        port='5432')


@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input is None:
        return jsonify({'error': 'No message provided'}), 400

    try: 
        reply = ''
        messages = user_input

        if user_input:
            response = client.responses.create(
                model="gpt-4.1-nano",
                input=user_input
            )

            reply = response.output_text
            messages = user_input + [{"role": "assistant", "content": reply}]
      
        # DB に保存
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO chat_history (chat_history) VALUES (%s)",
            (json.dumps(messages),)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        # 返答をfrontendに返す
        return jsonify({'response': reply})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat/history', methods=['GET'])
def get_chat_history():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT chat_history FROM chat_history
                    ORDER BY timestamp DESC
                    LIMIT 1
                    """)
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return jsonify(row[0])
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

