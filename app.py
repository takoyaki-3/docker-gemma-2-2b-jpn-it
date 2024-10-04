import torch
from transformers import pipeline
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

# パイプラインの準備 (CPUを使用するように設定)
pipe = pipeline(
    "text-generation",
    model="google/gemma-2-2b-jpn-it",
    device=-1  # CPUを使用
)

# Flaskアプリケーションの設定
app = Flask(__name__)
CORS(app)  # CORSを有効にしてクロスオリジンアクセスを許可

# HTMLの提供用のルートエンドポイント
@app.route('/')
def index():
    return render_template('index.html')

# 対話APIエンドポイント
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # 推論の実行
        messages = [{"role": "user", "content": user_message}]
        outputs = pipe(messages, return_full_text=False, max_new_tokens=256)
        assistant_response = outputs[0]["generated_text"].strip()

        return jsonify({"response": assistant_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
