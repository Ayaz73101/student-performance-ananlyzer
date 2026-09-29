# 🎓 Student Performance Analyzer

A Machine Learning based web application that predicts a student's overall academic performance using behavioral, attendance, study and career-related factors.

The application is developed using Python, Scikit-learn and Streamlit.

---

## 🚀 Features

- 🎓 Student performance prediction
- 📊 Interactive Streamlit dashboard
- 🤖 Gradient Boosting Regression model
- 📈 Feature importance analysis
- 🔍 Model comparison
- 📋 Student profile summary
- 📥 Downloadable prediction report
- 🧠 Machine Learning workflow visualization
- 📊 5-Fold Cross Validation evaluation

---

## 🧠 Machine Learning Model

The application uses a **Gradient Boosting Regressor** to predict the student's overall academic score.

### Input Features

| Feature | Type |
|---|---|
| Gender | Categorical |
| Part-Time Job | Boolean |
| Absence Days | Numerical |
| Extracurricular Activities | Boolean |
| Weekly Self-Study Hours | Numerical |
| Career Aspiration | Categorical |

### Target

**Overall Student Performance Score**

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
5-Fold Cross Validation
   ↓
Hyperparameter Tuning
   ↓
Gradient Boosting Model
   ↓
Performance Prediction