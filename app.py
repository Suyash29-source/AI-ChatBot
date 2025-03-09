from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Tumhare Local AI ka API (Mobile Flask App)
LOCAL_AI_API = "http://192.168.1.100:5000/chat"  # Mobile ka Flask server IP

@app.route("/")
def home():
    return "Server is Online and Listening for AI responses!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data["message"]

    # Local AI Flask Server Se Response Lo
    try:
        response = requests.post(LOCAL_AI_API, json={"message": user_message})
        ai_reply = response.json().get("response", "No response from AI.")
    except Exception as e:
        ai_reply = "Error: Local AI is not online!"

    return jsonify({"response": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
