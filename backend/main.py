from flask import Flask, request, jsonify, send_from_directory
from db import init_db, save_to_db, fetch_answer
from llm_handler import generate_answer
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')

    # 1. Check cache
    cached = fetch_answer(question)
    if cached:
        return jsonify({"answer": cached, "source": "db"})

    # 2. Generate from LLM
    answer = generate_answer(question)

    # 3. Save and return
    save_to_db(question, answer)
    return jsonify({"answer": answer, "source": "llm"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
