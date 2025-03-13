
# Step 2: Import Libraries
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import os

app = Flask(__name__)
CORS(app)

# Step 3: Default Model Name (Isko Change Karke Model Set Karna)
MODEL_NAME = "microsoft/DialoGPT-medium"  # Default Chat Model

# Step 4: Function To Load Any Model Dynamically
def load_model(model_name):
    global tokenizer, model, generator
    try:
        if "text-to-image" in model_name:
            from diffusers import StableDiffusionPipeline
            generator = StableDiffusionPipeline.from_pretrained(model_name).to("cuda")
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(model_name).half().cuda()
        return "Model Loaded Successfully"
    except Exception as e:
        return str(e)

# Step 5: Load Default Model at Startup
load_model(MODEL_NAME)

# Step 6: Route to Change Model
@app.route("/set_model", methods=["POST"])
def set_model():
    global MODEL_NAME
    data = request.get_json()
    MODEL_NAME = data.get("model_name", MODEL_NAME)
    response = load_model(MODEL_NAME)
    return jsonify({"message": response})

# Step 7: Chat Route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data["message"]

        if "text-to-image" in MODEL_NAME:
            image = generator(user_input).images[0]
            image_path = "static/generated.png"
            image.save(image_path)
            return jsonify({"image": image_path})

        input_ids = tokenizer.encode(user_input, return_tensors="pt").cuda()
        response_ids = model.generate(input_ids, max_length=200)
        response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)

        return jsonify({"reply": response_text})

    except Exception as e:
        return jsonify({"error": str(e)})

# Step 8: Web Interface Route
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
