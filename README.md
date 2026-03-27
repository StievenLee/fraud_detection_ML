# 🛡️ Fraud Detection System

> 🚀 Production-style fraud detection system with ML pipeline, real-time inference, explainable risk scoring, and interactive Streamlit UI.

---


## 🧩 Problem Statement

Financial fraud causes significant losses and requires fast, reliable detection.
This project simulates a real-world fraud detection pipeline that:

* Detects suspicious transactions in **real-time**
* Outputs **probability-based risk scores**
* Provides **interpretable insights & recommendations**

---

## 🏆 Key Features

* 🔍 Real-time prediction
* 📊 Fraud probability scoring
* ⚠️ Rule-based anomaly flags
* 🧠 Risk classification (Low → Critical)
* 💡 Actionable recommendations
* 🧪 Automated testing (pytest)
* 🧱 Modular & scalable architecture

---

## 🧠 ML Pipeline Architecture

```mermaid
flowchart LR
A[Raw Input] --> B[Feature Engineering]
B --> C[Preprocessing]
C --> D[Model (Random Forest)]
D --> E[Probability Output]
E --> F[Risk Classification]
F --> G[Insights & Recommendation]
```

### ✨ Feature Engineering

Custom transformer:

* `BalanceDiffTransformer`

Generated features:

* `balanceDiffOrig`
* `balanceDiffDest`

---

## 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 1.00  |
| Precision | 0.95  |
| Recall    | 0.83  |
| F1-score  | 0.89  |

> ⚠️ Fokus utama: **high recall untuk fraud detection**

---

## 🖥️ Streamlit App

### User Flow

1. Input data transaksi
2. Klik predict
3. Lihat:

   * Fraud probability
   * Risk level
   * Flags
   * Recommendation

---

## 🏗️ Project Structure

```
fraud_detection_ML/
│
├── app/
│   ├── predictor.py        # Inference logic
│   ├── config.py           # Constants & configs
│   └── streamlit_app.py    # UI
│
├── model/
│   └── fraud_detection_pipeline.pkl
│
├── src/
│   └── transformer.py      # Feature engineering
│
├── tests/
│   ├── conftest.py         # Shared test fixtures
│   └── test_predictor.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3.12
* pandas==2.3.3
* numpy==2.3.5
* matplotlib==3.10.8
* seaborn==0.13.2
* scikit-learn==1.8.0
* joblib==1.5.2
* pytest==9.0.2

---

## ▶️ Installation

```bash
git clone https://github.com/your-username/fraud_detection_ML.git
cd fraud_detection_ML
pip install -r requirements.txt
```

---

## ▶️ Run App

```bash
streamlit run app/streamlit_app.py
```

---

## 🧪 Testing

```bash
pytest -v
```

### ✔️ Coverage

* Prediction validity
* Edge case handling
* Feature consistency
* Rule-based flag validation

---

## 📊 Dataset

Kaggle Fraud Dataset:
[https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset)

---

## 🚀 Future Improvements

* 📈 Model evaluation dashboard
* 🎯 Threshold tuning (precision vs recall)
* ☁️ Cloud deployment (Streamlit / Docker)
* 🧾 Logging & monitoring system

---

## ⚠️ Disclaimer

Predictions are probabilistic and should support — not replace — human decisions.

---

## 👨‍💻 Author

Machine Learning Portfolio Project 🚀
