from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 🔹 OpenAI API Key (Apni API key daalo)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI Chat API is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "message" not in data:
            return jsonify({"error": "Invalid request"}), 400

        user_input = data["message"]
        
        # 🔹 Naya OpenAI API Syntax
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tum ek teasing, seductive aur friendly AI ho."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content  # ✅ Naya syntax yeh use karega

        return jsonify({"response": reply}), 200
    
    except Exception as e:
        print("❌ Error:", str(e))  # 🔹 Print error in Render logs
        return jsonify({"error": "Server error!", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
