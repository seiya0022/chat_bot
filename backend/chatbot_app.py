from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify


load_dotenv()   # load .env file
client = OpenAI()
response = client.responses.create(
    model="gpt-4.1-nano",
    input="Do you think I work too much?"
)
print(response.output_text)



app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = client.responses.create(
            model="gpt-4.1-nano",
            input=user_input
        )
        return jsonify({'response': response.output_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

