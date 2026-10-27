# 🍎 Smart Prediction Suite

A collection of three machine-learning projects built with **Google Teachable Machine**, Python, and browser-based demos. Each project solves a different classification task: fruit freshness, home-safety sound recognition, and exercise-pose detection.

## 📌 Projects

| Project | What it does | Main files |
|---|---|---|
| 🍎 **Fruit Freshness Prediction** | Classifies fruit images as Fresh or Rotten. | `Fruit_Freshness_Prediction.ipynb`, `models/fruit_freshness/` |
| 🎙️ **Home Safety Sound Detector** | Classifies audio into five sound categories. | `Home_Safety_Sound_Detector.html`, `models/home_safety_audio/` |
| 🏋️ **Exercise Counter — Pose Detection** | Classifies body poses and counts squats when a confident **Squat Down → Squat Up** transition is detected. | `Exercise_Counter.ipynb`, `Pose_Demo.html`, `models/pose_detection/`, `web_model/` |

---

## 🍎 1. Fruit Freshness Prediction

An image-classification project that predicts whether a fruit image is **Fresh** or **Rotten** using a model trained with Google Teachable Machine and exported as a Keras model.

### Features
- Fresh vs. Rotten fruit classification
- Image preprocessing and prediction
- Prediction confidence score
- Testing on multiple fruit images
- Confusion-matrix evaluation

### Model files
`models/fruit_freshness/`
- `keras_model.h5`
- `labels.txt`

Test images are stored in `Data/Testing_Fruit_Images/`.

---

## 🎙️ 2. Home Safety Sound Detector

A browser-based audio-classification project using a Teachable Machine model.

### Audio classes
- Alarm
- Background Noise
- Door Knock
- Glass Break
- Siren

### Demo and model files
- **HTML demo:** `Home_Safety_Sound_Detector.html`
- **Model folder:** `models/home_safety_audio/`
  - `model.json`
  - `metadata.json`
  - `weights.bin`

The HTML demo requires microphone permission. The Streamlit web application is maintained separately.

### Live demo
[Open Home Safety Sound Detector](https://home-safety-detection.streamlit.app/)

### Related repositories
- [Main project repository](https://github.com/PareeSojitra0803/Smart_Prediction_Suite_Using_CNN)
- [Home Safety Detection web app](https://github.com/PareeSojitra0803/Home_Safety_Detection_WebApp)

---

## 🏋️ 3. Exercise Counter — Pose Detection

A webcam-based pose-classification demo trained with Google Teachable Machine. The model classifies the pose shown in the camera and uses squat-pose transitions to count repetitions.

### Pose classes
- `Squat Down`
- `Squat Up`
- `Rest`
- `Arm Raised`
- `Arm Down`

### Features
- Live webcam pose classification
- Predicted pose and confidence display
- Confidence scores for each class
- Squat repetition counter: a confident **Squat Down** prediction followed by **Squat Up** adds one repetition

**Note:** Arm poses are classified, but they do not increment the squat counter. Prediction quality depends on the training examples, camera view, lighting, and visibility of the body. This is a demonstration project, not a medical or professional fitness assessment.

### Model and demo files
- **Notebook:** `Exercise_Counter.ipynb`
- **Browser demo:** `Pose_Demo.html`
- **Exported model:** `models/pose_detection/`
  - `model.json`
  - `metadata.json`
  - `weights.bin`
- **Browser model copy:** `web_model/` (used by the HTML demo)

The browser demo needs webcam permission.

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- TensorFlow.js
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Pillow
- Scikit-learn
- Google Teachable Machine
- Jupyter Notebook
- HTML, CSS, and JavaScript

---

## 📁 Project Structure

```text
Smart_Prediction_Suite_Using_CNN/
│
├── Data/
│   └── Testing_Fruit_Images/
│       ├── freshapple.jpg
│       ├── freshpear.jpg
│       ├── freshstrawberry.jpg
│       ├── rottenapple.jpg
│       └── rottengrapes.jpg
│
├── models/
│   ├── fruit_freshness/
│   │   ├── keras_model.h5
│   │   └── labels.txt
│   │
│   ├── home_safety_audio/
│   │   ├── model.json
│   │   ├── metadata.json
│   │   └── weights.bin
│   │
│   └── pose_detection/
│       ├── model.json
│       ├── metadata.json
│       └── weights.bin
│
├── scripts/
│   └── download_fruit.py
│
├── web_model/                 # Model files used by Pose_Demo.html
├── Fruit_Freshness_Prediction.ipynb
├── Exercise_Counter.ipynb
├── Home_Safety_Sound_Detector.html
├── Pose_Demo.html
├── README.md
└── requirements.txt
```

*The structure above shows the expected project files; local files may vary if you have not created or retained every listed item.*

---

## ▶️ How to Run

### Install Python dependencies

From the repository folder, run:

```bash
pip install -r requirements.txt
```

Use a compatible Python environment/kernel for the installed TensorFlow version.

### Fruit Freshness Prediction
1. Open `Fruit_Freshness_Prediction.ipynb` in Jupyter Notebook or VS Code.
2. Select your Python kernel.
3. Run the cells from top to bottom.
4. Test images from `Data/Testing_Fruit_Images/` can be used for predictions.

### Exercise Counter — Pose Detection
1. Open `Pose_Demo.html` in a browser using a local HTTP server from the repository folder:

   ```bash
   python -m http.server 8000
   ```

2. Visit `http://localhost:8000/Pose_Demo.html`.
3. Allow webcam access and start the demo.

If the browser demo cannot load the model, confirm that `web_model/` contains the model files and that the paths in `Pose_Demo.html` match the folder structure. Stop the local server with `Ctrl+C`.

### Home Safety Sound Detector
Open `Home_Safety_Sound_Detector.html` through a local HTTP server and allow microphone access. The separate Streamlit app is available through the live-demo link above.


---

<div align="center">

## 👩‍💻 Author

***Paree Sojitra***

### ✨ Turning Ideas into Intelligent Solutions

*Built with curiosity, powered by AI, and driven by continuous learning.*

**Paree Sojitra** 💻

[GitHub](https://github.com/PareeSojitra0803) · [Explore My Projects](https://github.com/PareeSojitra0803?tab=repositories)

⭐ *If you find this project interesting, consider giving it a star!*

</div>

---
