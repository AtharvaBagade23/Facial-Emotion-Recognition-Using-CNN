import os
import cv2
import numpy as np
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# Load trained model
MODEL_PATH = "saved_models/fer_cnn_best.h5"
model = load_model(MODEL_PATH)

# Emotion labels (FER-2013 dataset)
LABELS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Image preprocessing
def preprocess_image(image):
    image = cv2.resize(image, (48, 48))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# ---------------------------
# Web UI Route
# ---------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# ---------------------------
# Predict API Route
# ---------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        img = Image.open(file.stream).convert("RGB")
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        processed = preprocess_image(img_cv)

        preds = model.predict(processed)[0]
        top_idx = int(np.argmax(preds))
        emotion = LABELS[top_idx]
        confidence = float(preds[top_idx])

        return jsonify({"emotion": emotion, "confidence": round(confidence * 100, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
