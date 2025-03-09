from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"  # Apna OpenAI API Key yaha daalo

@app.route("/")
def home():
    return "AI Chat API Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_input = data["message"]
    
    # OpenAI API call for better response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Tum ek teasing, seductive aur friendly AI ho."},
                      {"role": "user", "content": user_input}]
        )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply = "Koi error aa gaya! 😢"

    return jsonify({"response": reply}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
