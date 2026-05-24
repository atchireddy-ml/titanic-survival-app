# Titanic Survival Prediction App

A Machine Learning web application built using Streamlit that predicts whether a passenger survived the Titanic disaster using trained classification models and feature engineering techniques.

---

# Project Overview

This project demonstrates an end-to-end Machine Learning workflow including:

- Data preprocessing
- Feature engineering
- Polynomial feature generation
- Model training
- Hyperparameter tuning
- Pipeline creation
- Web app deployment

The application takes passenger details as input and predicts survival probability using a trained Machine Learning model.

---

# Technologies Used

## Programming Language
- Python

## Libraries & Frameworks
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

# Machine Learning Concepts Used

## Data Preprocessing

The dataset was cleaned and transformed using:
- Missing value handling
- Encoding categorical variables
- Feature scaling
- Train-test split

---

## Feature Engineering

Additional feature transformations were performed to improve model performance.

### Polynomial Features

Polynomial Features were generated to capture nonlinear relationships between input variables.

Example:
- Age²
- Fare²
- Age × Fare

Different polynomial degrees were tested iteratively to identify the best-performing configuration.

---

## Machine Learning Algorithms Used

The project experimented with multiple classification algorithms:

### Logistic Regression
Used as a baseline linear classification model.

### Decision Tree Classifier
Used to capture nonlinear decision boundaries.

### Random Forest Classifier
Improved accuracy using ensemble learning.

### Support Vector Machine (SVM)
Used for high-dimensional classification.

### K-Nearest Neighbors (KNN)
Distance-based classification algorithm.

---

# Model Selection Strategy

The best model was selected based on:
- Accuracy Score
- Cross Validation
- Generalization Performance
- Overfitting Analysis

GridSearchCV was used for hyperparameter tuning and selecting optimal parameters.

---

# Pipeline Workflow

Scikit-learn Pipeline was used to combine preprocessing and model training steps into a single workflow.

Pipeline stages included:

text
Input Data
   ↓
Data Preprocessing
   ↓
Feature Scaling
   ↓
Polynomial Feature Generation
   ↓
Model Training
   ↓
Prediction


Benefits of Pipeline:
- Cleaner workflow
- Prevents data leakage
- Easier deployment
- Reproducible training process

---

# Project Structure

bash
titanic-survival-app/
│
├── app.py
├── model.pkl
├── titanic.csv
├── requirements.txt
├── runtime.txt
└── README.md


---

# Installation

Clone the repository:

bash
git clone https://github.com/your-username/titanic-survival-app.git


Move into the project folder:

bash
cd titanic-survival-app


Install dependencies:

bash
pip install -r requirements.txt


Run the application:

bash
streamlit run app.py


---

# Requirements

text
streamlit
pandas
numpy
scikit-learn==1.5.1
joblib==1.4.2


---

# Python Version

text
python-3.12


---

# Streamlit Features Used

- st.title()
- st.write()
- st.number_input()
- st.selectbox()
- st.button()
- st.success()

---

# Deployment

This application can be deployed using:
- Streamlit Community Cloud
- Render
- Railway

---

# Future Improvements

- Deep Learning implementation
- Advanced feature engineering
- Model explainability using SHAP
- Interactive visualizations
- Docker containerization
- CI/CD integration

---

# Learning Outcomes

This project helped in understanding:
- End-to-end ML workflow
- Feature engineering
- Polynomial transformations
- Pipeline creation
- Hyperparameter tuning
- Model deployment
- Frontend integration with Streamlit

---

# Author

Developed as part of an AI & Data Science learning roadmap.

---

# License

This project is open-source and available under the MIT License.
