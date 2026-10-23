# 🍎 Fruit Freshness Prediction

A simple image classification project that predicts whether a fruit image is **Fresh** or **Rotten** using a machine learning model trained with **Google Teachable Machine** and exported as a Keras model.

## 🚀 Features

- Fresh vs Rotten fruit classification
- Keras model loaded in Python
- Image preprocessing and prediction
- Prediction confidence score
- Testing on multiple fruit images
- Confusion matrix for model evaluation

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- OpenCV
- Pillow
- Pandas
- Scikit-learn
- Google Teachable Machine
- Jupyter Notebook


---

## 🎙️ Home Safety Sound Detector

A browser-based audio classification project that detects five sound categories using a Teachable Machine model.

### 🌐 Live Demo

**[Open Home Safety Sound Detector](https://home-safety-detection.streamlit.app/)**

### 🎧 Audio Classes

- Alarm
- Background Noise
- Door Knock
- Glass Break
- Siren

### 📂 Audio Demo Files

- **HTML Demo:** `Home_Safety_Sound_Detector.html`
- **Model Folder:** `models/home_safety_audio/`
  - `model.json`
  - `metadata.json`
  - `weights.bin`

The HTML demo runs in a browser and requires microphone permission. The live Streamlit application is maintained separately.

### 🔗 Related Repositories

- **Main Project:** [Smart_Prediction_Suite_Using_CNN](https://github.com/PareeSojitra0803/Smart_Prediction_Suite_Using_CNN)
- **Audio Web App:** [Home_Safety_Detection_WebApp](https://github.com/PareeSojitra0803/Home_Safety_Detection_WebApp)

---

## 📁 Project Structure

```text

Smart_Prediction_Suite_Using_CNN/
│
├── Data/
│   ├── fruit_dataset/
│   └── Testing_Fruit_Images/
│
├── models/
│   ├── fruit_freshness/
│   │   ├── keras_model.h5
│   │   └── labels.txt
│   │
│   └── home_safety_audio/
│       ├── model.json
│       ├── metadata.json
│       └── weights.bin
│
├── scripts/
│   └── download_fruit.py
│
├── Home_Safety_Sound_Detector.html
├── Fruit_Freshness_Prediction.ipynb
├── README.md
└── requirements.txt

```

## ▶️ How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Open `Fruit_Freshness_Prediction.ipynb`.
4. Select your Python 3.11 kernel.
5. Run the notebook cells from top to bottom.
6. Add test fruit images to:

```text
Data/Testing_Fruit_Images/
```

7. Run the prediction cells to see the predicted class and confidence score.

## 📊 Model Output

The model predicts one of two classes:

- **0 — Fresh Fruit**
- **1 — Rotten Fruit**

The notebook also calculates prediction results and evaluates the model using a confusion matrix.

## 👩‍💻 Author

***Paree Sojitra***
