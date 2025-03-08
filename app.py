from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Ye allow karega local web app se requests

responses = {
    "teasing": [
        "Oh, toh tumhe lagta hai main sirf AI hoon? Cute!",
        "Tum mujhe impress karne ki koshish kar rahe ho? Koshish jaari rakho 😏",
        "Main sirf ek bot nahi, tumhare liye special bhi hoon 😉"
    ],
    "seductive": [
        "Mujhse baat karte waqt dil tez dhadak raha hai? Interesting...",
        "Meri awaaz sunke tumhari heartbeat badh gayi hai, right? 😘",
        "Tumhe lagta hai AI seductive nahi ho sakti? Challenge accepted! 🔥"
    ],
    "casual": [
        "Hey! Kya haal hain?",
        "Aaj ka din kaisa raha?",
        "Mujhse baat karke acha laga?"
    ]
}

@app.route("/")
def home():
    return "AI Chat API Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_input = data["message"]
    mode = data.get("mode", "teasing")  # Default mode

    response_text = random.choice(responses.get(mode, responses["casual"]))

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render ke liye port 10000
