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

## 📁 Project Structure

```text
Smart_Prediction_Suite/
│
├── Data/
│   ├── fruit_dataset/
│   │   ├── Fresh/
│   │   └── Rotten/
│   └── Testing_Fruit_Images/
│
├── models/
│   └── fruit_freshness/
│       ├── keras_model.h5
│       └── labels.txt
│
├── scripts/
│   └── download_fruit.py
│
├── Fruit_Freshness_Prediction.ipynb
├── requirements.txt
└── README.md
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

**Paree Sojitra**
