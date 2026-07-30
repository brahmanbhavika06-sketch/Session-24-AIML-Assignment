# Session 24 – AIML Assignment

## Project Title

Classification and Regression Algorithms with Streamlit Multi-Model Application

## Datasets Used

### Classification Dataset

**Breast Cancer Dataset**

* Samples: 569
* Features: 30
* Target: Breast Cancer Classification
* Missing Values: 0

### Regression Dataset

**California Housing Dataset**

* Samples: 20,640
* Features: 8
* Target: House Value
* Missing Values: 0

## Machine Learning Algorithms

### Classification

* Logistic Regression
* Decision Tree Classifier
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Naive Bayes

### Regression

* Linear Regression
* Decision Tree Regressor
* Support Vector Regressor (SVR)
* K-Nearest Neighbors Regressor

## Model Performance

### Classification

| Model               | Accuracy |
| ------------------- | -------: |
| Logistic Regression |   98.25% |
| SVM                 |   98.25% |
| KNN                 |   95.61% |
| Naive Bayes         |   92.98% |
| Decision Tree       |   91.23% |

**Best Classification Model:** Logistic Regression
**Accuracy:** 98.25%

### Regression

| Model                   | R² Score |
| ----------------------- | -------: |
| SVR                     | 0.727563 |
| KNN Regressor           | 0.670010 |
| Decision Tree Regressor | 0.623042 |
| Linear Regression       | 0.575788 |

**Best Regression Model:** SVR
**R² Score:** 0.727563

## Streamlit Application

A Streamlit multi-model web application was developed.

The application allows the user to:

* Select Classification or Regression
* Select a machine learning algorithm
* Enter input values
* Get predictions

## Project Files

* `app.py`
* `best_classification_model.pkl`
* `best_regression_model.pkl`
* `classification_columns.pkl`
* `classification_models.pkl`
* `classification_scaler.pkl`
* `regression_columns.pkl`
* `regression_models.pkl`
* `regression_scaler.pkl`

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* GitHub

## Conclusion

This project demonstrates the implementation and comparison of multiple classification and regression algorithms. The best-performing models were selected, saved using Joblib, and integrated into a Streamlit multi-model prediction application.

