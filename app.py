from flask import Flask, request, jsonify  
import openai  

app = Flask(__name__)  

openai.api_key = "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"  # Apni API key yaha daal  

modes = {  
    "normal": "You're a friendly and fun AI.",  
    "teasing": "You're a playful and flirty AI who enjoys teasing the user.",  
    "seductive": "You're a seductive AI that subtly flirts and seduces the user."  
}  

def generate_response(user_input, mode="teasing"):  
    prompt = f"{modes[mode]} Respond to: {user_input}"  
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])  
    return response["choices"][0]["message"]["content"]  

@app.route("/chat", methods=["POST"])  
def chat():  
    data = request.json  
    user_input = data.get("message")  
    mode = data.get("mode", "teasing")  # Default mode "teasing" rahega  
    response = generate_response(user_input, mode)  
    return jsonify({"response": response})  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000, debug=True)
