from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBRoCsPwVBPKr65wSq8PF79WB1_kT2YyIM"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_input = data["message"]

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"error": "API Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
