# 🧠 Toxic Comment Detector (Full Stack ML Project)

A production-ready machine learning web application that detects toxic comments using NLP techniques and serves predictions via a FastAPI backend with a clean frontend UI.

---

## Live  Demo

https://toxic-comment-detector-knns.onrender.com

---

## 🚀 Features

- 🔍 Detect toxic vs non-toxic comments
- ⚡ FastAPI backend (high performance)
- 🎯 ML model using TF-IDF + Logistic Regression
- 💾 MongoDB Atlas integration (store predictions)
- 🎨 Modern UI (HTML, CSS, JavaScript)
- 🌐 Deployable on cloud platforms

---

## 🛠 Tech Stack

**Backend**
- FastAPI
- Python

**Machine Learning**
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

**Frontend**
- HTML
- CSS
- JavaScript

**Database**
- MongoDB Atlas

---

## 📊 Dataset

Dataset is not included due to size limitations.

You can download it from:
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge

After downloading:
- Place it in `data/raw/`
- Run the pipeline to generate processed data


---

## ⚙️ How It Works

1. User enters text
2. Text sent to FastAPI API
3. Vectorizer converts text → numerical features
4. ML model predicts toxicity
5. Result stored in MongoDB
6. Response shown on UI

---

## ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

---

## 🤝 Author

Durgesh Maurya