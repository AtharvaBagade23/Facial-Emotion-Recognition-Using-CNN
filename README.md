Got it 👍
Here’s a **README.md** for your **Facial Emotion Recognition using CNN** project based on your `app.py` and folder structure:

---

```markdown
# 😊 Facial Emotion Recognition using CNN

This project is a **Facial Emotion Recognition System** built using **Convolutional Neural Networks (CNNs)**.  
It classifies facial expressions into **seven categories**:

- Angry  
- Disgust  
- Fear  
- Happy  
- Neutral  
- Sad  
- Surprise  

---

## 🚀 Features

- Deep Learning model trained on facial expression dataset  
- Flask web app for UI and API  
- Real-time emotion prediction  
- REST API endpoint (`/predict`) to accept images and return prediction  
- Simple web interface (`index.html`) to upload images  

---

## 📂 Project Structure

```

CNN-Project/
│
├── data/                  # Dataset (train/test folders)
│   ├── train/
│   └── test/
│
├── saved\_models/          # Trained models
│   └── fer\_cnn\_best.h5
│
├── static/                # Static files (CSS, JS, images)
│   └── style.css
│
├── templates/             # HTML templates
│   └── index.html
│
├── app.py                 # Flask web app
├── train\_from\_folders.py  # Training script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AtharvaBagade23/Facial-Emotion-Recognition-Using-CNN.git
   cd Facial-Emotion-Recognition-Using-CNN
````

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

3. Upload an image → Get predicted emotion 🎭

---

## 📡 API Endpoint

* **POST** `/predict`
  Accepts an uploaded image and returns predicted emotion in JSON format.

Example (using `curl`):

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

* The CNN model was trained on a facial emotion dataset.
* You can retrain using:

  ```bash
  python train_from_folders.py
  ```

---

## 📌 Requirements

* Python 3.8+
* TensorFlow / Keras
* Flask
* NumPy
* OpenCV (optional, for real-time detection)

Install them via:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Atharva Bagade**
📌 GitHub: [AtharvaBagade23](https://github.com/AtharvaBagade23)

---

## 📜 License

This project is licensed under the MIT License.

```

---

Do you also want me to make the **README more visual** (with images, badges, usage screenshots)? That would make your GitHub repo look professional.
```
