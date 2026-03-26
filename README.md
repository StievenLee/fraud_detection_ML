# 🛡️ Fraud Detection System

Sistem Machine Learning untuk mendeteksi potensi transaksi fraud secara real-time menggunakan model klasifikasi dan antarmuka interaktif berbasis Streamlit.

---

## 📌 Overview

Project ini bertujuan untuk:

* Mengidentifikasi transaksi mencurigakan (fraud)
* Memberikan **probabilitas risiko**
* Menyediakan **insight tambahan** seperti:

  * Risk level (Rendah → Sangat Tinggi)
  * Pola mencurigakan (flags)
  * Rekomendasi tindakan

Aplikasi dilengkapi dengan UI interaktif sehingga user dapat langsung melakukan simulasi transaksi.

---

## 🚀 Features

* 🔍 Prediksi fraud secara real-time
* 📊 Probabilitas fraud dengan visual progress bar
* ⚠️ Deteksi pola mencurigakan (rule-based flags)
* 🧠 Risk classification (Low, Medium, High)
* 💡 Rekomendasi tindakan berdasarkan hasil prediksi
* 🧪 Automated testing menggunakan pytest
* 🎯 Feature engineering custom (`BalanceDiffTransformer`)

---

## 🏗️ Project Structure

```
fraud_detection_ML/
│
├── app/
│   ├── __init__.py
│   ├── predictor.py        # Logic inference
│   ├── config.py           # Konfigurasi & constants
│   └── streamlit_app.py    # UI aplikasi
│
├── model/
│   └── fraud_detection_pipeline.pkl
│
├── src/
│   └── transformer.py      # Feature engineering
│
├── tests/
│   └── test_predictor.py   # Automated testing
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3.12
* Scikit-learn
* Pandas
* Streamlit
* Pytest

---

## ▶️ How to Run

### 1. Clone repository

```bash
git clone https://github.com/your-username/fraud_detection_ML.git
cd fraud_detection_ML
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app/streamlit_app.py
```

---

## 🧪 Testing

Project ini menggunakan automated testing untuk memastikan sistem berjalan dengan baik.

Jalankan test dengan:

```bash
pytest -v
```

Testing mencakup:

* Validasi output model
* Konsistensi hasil prediksi
* Edge case handling
* Deteksi flags

---

## 📊 Dataset

Dataset yang digunakan berasal dari Kaggle:

👉 https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset

Dataset berisi:

* Tipe transaksi
* Jumlah transaksi
* Saldo sebelum & sesudah
* Label fraud (0 = normal, 1 = fraud)

---

## 🧠 Model

Model yang digunakan:

* Random Forest Classifier

Pipeline mencakup:

* Feature Engineering
* Preprocessing
* Classification

Contoh fitur tambahan:

* `balanceDiffOrig`
* `balanceDiffDest`

---

## ⚠️ Disclaimer

Hasil prediksi bersifat **probabilistik** dan tidak menggantikan keputusan manusia.
Selalu lakukan verifikasi manual untuk transaksi dengan nilai tinggi.

---

## 📈 Future Improvements

* Dashboard evaluasi model (confusion matrix, precision/recall)
* Threshold tuning untuk meningkatkan recall fraud
* Deployment ke cloud (Streamlit Cloud / Docker)
* Logging & audit trail system

---

## 👨‍💻 Author

Dikembangkan sebagai project portfolio Machine Learning.

---