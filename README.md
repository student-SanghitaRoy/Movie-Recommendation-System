# 🎬 Movie Recommendation System using Content-Based Filtering

## 🔗 Live Deployment

🚀 **Deployed Application:**  
👉 https://movie-recommendation-system-39k4.onrender.com

---

## 📌 Project Overview

This project implements a **Content-Based Movie Recommendation System** that suggests similar movies based on their metadata such as genres, cast, keywords, and overview.

The system processes textual features using **NLTK**, computes similarity between movies, and provides recommendations through a deployed **Flask web application** with real-time poster display.

This project demonstrates an end-to-end machine learning pipeline — from data preprocessing to model building and cloud deployment.

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing

- Merged movie and credit datasets  
- Selected relevant features (genres, keywords, cast, overview)  
- Handled missing values  
- Combined important textual attributes into a single feature column  

### 2️⃣ Text Processing (NLTK)

- Tokenization  
- Lowercasing  
- Stemming  
- Noise removal  

### 3️⃣ Feature Representation

- Converted processed text into numerical vectors  
- Built a similarity matrix using cosine similarity  

### 4️⃣ Recommendation Logic

For a selected movie:

- Retrieve its similarity scores  
- Sort movies based on similarity  
- Return top 5 most similar movies  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- NLTK  
- Flask  
- HTML & CSS  
- OMDb API (for poster fetching)  
- Gunicorn  
- Render (Cloud Deployment)  

---

## ✨ Features

- Content-based movie recommendations  
- Text preprocessing using NLTK  
- Real-time movie poster fetching  
- Clean and responsive user interface  
- Cloud deployed application  

---

## 📂 Project Structure

Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── favicon.ico
│
└── README.md


---

## 📊 System Workflow

User Input → Movie Title Matching → Similarity Score Retrieval →  
Top Recommendations → Poster Fetching via API → Results Displayed in Web Interface

---

## 🔮 Future Improvements

- Hybrid Recommendation System (Content + Collaborative Filtering)  
- User profile-based personalization  
- Feedback-based recommendation refinement  
- Performance optimization for larger datasets  
- UI enhancements with filtering and sorting options  

---

## 📚 Learning Outcomes

- Practical implementation of content-based filtering  
- Text preprocessing using NLTK  
- Feature engineering for recommendation systems  
- Flask backend integration  
- API handling and poster retrieval  
- Cloud deployment of ML applications  

---

## 👩‍💻 Project Information

- **Project Title:** Movie Recommendation System  
- **Author Name:** Sanghita Roy  
- **Roll Number:** 23035010421  
- **Program:** B.Sc. (Hons.) Data Science & Artificial Intelligence  
- **Institute:** IIT Guwahati  

---

## ⭐ Academic Purpose

This project was developed as part of academic learning to demonstrate understanding of:

- Recommendation systems  
- Text processing techniques  
- Similarity-based modeling  
- End-to-end ML application deployment  
