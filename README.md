# 🛡️ Fraud Detection System

> 🚀 End-to-end machine learning fraud detection prototype with interactive Streamlit app, risk scoring, and explainable insights.

---

## 🧩 Problem Statement

Financial fraud poses significant risks in digital transactions. Detecting fraudulent activity accurately and quickly is essential to minimize losses.

This project simulates a real-world fraud detection system that:

* Identifies suspicious transactions
* Estimates fraud probability
* Provides interpretable insights and recommendations

---

## 🏆 Key Features

* 🔍 Fraud prediction using machine learning
* 📊 Probability-based risk scoring
* ⚠️ Rule-based suspicious pattern detection
* 🧠 Risk classification (Low → Critical)
* 💡 Actionable recommendations
* 🧪 Automated testing using pytest
* 🧱 Modular and scalable project structure

---

## 🧠 Machine Learning Pipeline

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

---

## 🖥️ Application (Streamlit)

This project includes an interactive web application where users can:

1. Input transaction data
2. Run prediction
3. View:

   * Fraud probability
   * Risk level
   * Detected flags
   * Recommended actions

---

## 🏗️ Project Structure

```
fraud_detection_ML/
│
├── app/
│   ├── predictor.py        # Inference logic
│   ├── config.py           # Configuration
│   └── streamlit_app.py    # User interface
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

## ▶️ Run Application

```bash
streamlit run app/streamlit_app.py
```

---

## 🧪 Testing

```bash
pytest -v
```

### ✔️ Test Coverage

* Prediction validation
* Edge case handling
* Feature consistency
* Rule-based flag detection

---

## 📊 Dataset

Dataset source:
[https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset)

---

## 🚀 Future Improvements

* Model evaluation dashboard (confusion matrix, precision/recall)
* Threshold tuning for better recall
* Deployment to cloud (Streamlit / Docker)
* Logging and monitoring system

---

## ⚠️ Disclaimer

This project is a prototype. Predictions are probabilistic and should support—not replace—human decision-making.

---

## 👨‍💻 Author

Machine Learning Portfolio Project
