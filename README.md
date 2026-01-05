# 🎓 Student Ability Classifier & Recommender

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-KMeans-orange)

## 📌 Project Overview
This project is a Machine Learning application designed to streamline the student selection process for higher education courses. By analyzing historical data of student performance (Graduation Marks and Entrance Exam scores), the system uses **Unsupervised Learning (K-Means Clustering)** to categorize new applicants into distinct eligibility groups.

The model helps admission committees make data-driven decisions by automatically classifying students into:
* Selected for Course
* Shortlisted for Interview
* Eligible for Second Round
* Not Selected

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend:** Streamlit (Web App Interface)
* **Machine Learning:** Scikit-Learn (K-Means Clustering)
* **Data Manipulation:** Pandas

## 📊 Methodology
1.  **Data Preprocessing:** * Applied **Standard Scaling** to normalize Graduation and Entrance marks, ensuring that the distance-based K-Means algorithm functions correctly.
2.  **Modeling:**
    * Implemented **K-Means Clustering** to identify 4 distinct student profiles.
    * Determined the optimal number of clusters using the Elbow Method (implied).
3.  **Deployment:**
    * Wrapped the model in a **Streamlit** application for real-time inference.

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YourUsername/student-ability-classifier.git](https://github.com/YourUsername/student-ability-classifier.git)
    cd student-ability-classifier
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run src/app.py
    ```

## 📂 Directory Structure
```text
├── data/               # Contains dataset (clusters_new.xlsx)
├── model/              # Serialized ML model (model.pkl)
├── src/                # Application source code
│   └── app.py
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation