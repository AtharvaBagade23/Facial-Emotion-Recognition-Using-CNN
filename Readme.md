# 😊 Facial Emotion Recognition using CNN

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)  
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)  
![MIT License](https://img.shields.io/badge/License-MIT-green)

A deep learning-based **Facial Emotion Recognition System** using **Convolutional Neural Networks (CNNs)**.  
It predicts **7 emotions** from facial images:

😠 Angry | 🤢 Disgust | 😨 Fear | 😀 Happy | 😐 Neutral | 😢 Sad | 😲 Surprise  

---

## 📸 Demo

### 🔹 Web App Interface
![Web Demo](static/demo_web.png)  
*(Upload an image → Get emotion prediction instantly!)*  

### 🔹 Example Predictions
| Input Image | Predicted Emotion |
|-------------|-------------------|
| ![Happy](static/sample_happy.jpg) | 😀 Happy |
| ![Sad](static/sample_sad.jpg)     | 😢 Sad |
| ![Surprise](static/sample_surprise.jpg) | 😲 Surprise |

---

## 🚀 Features

✅ CNN-based emotion recognition  
✅ Flask-powered Web UI  
✅ REST API for predictions (`/predict`)  
✅ Real-time & offline support  
✅ Easy training on custom datasets  

---

## 📂 Project Structure

```
CNN-Project/
│
├── data/                  # Dataset (train/test)
│   ├── train/
│   └── test/
│
├── saved_models/          # Trained model
│   └── fer_cnn_best.h5
│
├── static/                # Static files (CSS, images)
│   ├── style.css
│   └── demo_web.png
│
├── templates/             # HTML templates
│   └── index.html
│
├── app.py                 # Flask app
├── train_from_folders.py  # Model training script
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AtharvaBagade23/Facial-Emotion-Recognition-Using-CNN.git
   cd Facial-Emotion-Recognition-Using-CNN
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. Start the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser:
   ```
   http://127.0.0.1:5000/
   ```

3. Upload a face image → 🎭 Get emotion prediction  

---

## 📡 API Endpoint

### 🔹 Predict Emotion
**POST** `/predict`

Request:
```bash
curl -X POST -F "file=@happy.jpg" http://127.0.0.1:5000/predict
```

Response:
```json
{
  "emotion": "Happy",
  "confidence": 0.98
}
```

---

## 🧠 Model Training

To retrain the CNN model:
```bash
python train_from_folders.py
```

You can replace the dataset inside `/data/train` and `/data/test` to fine-tune on new faces.

---

## 📌 Requirements

- Python 3.8+  
- TensorFlow / Keras  
- Flask  
- NumPy  
- OpenCV (optional, for live webcam prediction)

Install them all with:
```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Atharva Bagade**  
📌 GitHub: [AtharvaBagade23](https://github.com/AtharvaBagade23)

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share 🚀
