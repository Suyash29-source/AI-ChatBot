from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# AI Model Load
model_name = "mosaicml/mpt-7b-instruct"  # Alternative: "TheBloke/Llama-2-7B-Chat-GGUF"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# AI Chat Function
def chat_with_ai(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=150, temperature=0.9, top_k=50, top_p=0.85)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# API Route for AI chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    ai_response = chat_with_ai(user_input)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
