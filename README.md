# 🧠 Toxic Comment Detection App

> 🚀 An AI-powered web application that detects whether a comment is **toxic or non-toxic** using Machine Learning.

---

## 🌟 Overview

This project uses **Natural Language Processing (NLP)** and a **Naive Bayes classifier** to analyze user input and classify it as toxic or safe in real-time.

It is designed as a **lightweight, fast, and deployable ML application** using Streamlit.

---

## 🚀 Live Demo
🔗https://toxicity-comment-detector-ai.streamlit.app

---

## 🎯 Key Features

✨ Real-time toxicity detection  
⚡ Fast predictions using optimized model  
📊 Confidence score display  
🎨 Clean and interactive UI  
🌐 Easy deployment using Streamlit Cloud  

---

## 🖥️ Demo Preview

> Example:

| Input Comment | Output |
|--------------|--------|
| "I hate you" | 🚨 Toxic Comment |
| "Great work!" | ✅ Non-Toxic Comment |

---

## 🧠 How It Works

1. User enters a comment  
2. Text is preprocessed (lowercasing, cleaning)  
3. Converted into numerical form using **TF-IDF Vectorization**  
4. Passed into **Naive Bayes model**  
5. Model predicts:
   - Toxic 🚨  
   - Non-Toxic ✅  

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🤖 Scikit-learn  
- 🌐 Streamlit  

---

## 📂 Project Structure

## toxic-comment-detector
│
### Streamlit web application
├── [app.py](https://github.com/durx95/toxic-comment-detector/blob/main/app.py)
### Model training notebook
├── [naive_bayes_classifition.ipynb](https://github.com/durx95/toxic-comment-detector/blob/main/naive_bayes_classifition.ipynb)   
### Trained machine learning model
├── [model.pkl](https://github.com/durx95/toxic-comment-detector/blob/main/model.pkl)  

├── [vectorizer.pkl](https://github.com/durx95/toxic-comment-detector/blob/main/vectorizer.pkl)                    
### Training dataset
├── [train.csv](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data?select=train.csv.zip)                      
### Required Python libraries
├── [requirements.txt](https://github.com/durx95/toxic-comment-detector/blob/main/requirements.txt)               
### Project documentation
└──[README.md](https://github.com/durx95/toxic-comment-detector/blob/main/README.md)