<img width="721" height="763" alt="Screenshot 2026-03-10 at 00 54 54" src="https://github.com/user-attachments/assets/248409b9-fc4a-4e43-8d58-ed8de456dbfc" /># Credit Risk & Default Prediction Dashboard

This project develops a machine learning model to classify borrowers into credit risk categories based on financial and behavioral characteristics. The goal is to identify key risk indicators and provide an interactive tool for assessing borrower credit risk.


## Project Overview

Financial institutions rely on credit risk models to evaluate the likelihood that a borrower will default on their obligations. This project demonstrates an end-to-end credit risk modelling workflow including:

- Data storage and transformation
- Exploratory Data Analysis (EDA)
- Machine learning model development
- Risk classification
- Deployment through an interactive dashboard

The final model predicts borrower risk segments and visualizes the probability distribution of each risk category.


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- PostgreSQL
- Streamlit
- Matplotlib
- Seaborn
- Joblib


## Project Structure

credit-risk-prediction-dashboard

─ credit-risk-model-development.ipynb
   Jupyter Notebook containing exploratory data analysis,
   feature analysis, and machine learning model development.

─ app.py
   Streamlit dashboard used to interactively predict borrower
   credit risk and visualize model probabilities.

─ credit_risk_model.pkl
   Trained Random Forest machine learning model used by
   the Streamlit application for predictions.

─ credit_risk_dashboard.csv
   Processed dataset used for model training and dashboard
   demonstrations.

─ requirements.txt
   Python dependencies required to run the notebook and
   Streamlit dashboard.

─ README.md
    Project documentation and overview.


## Data Pipeline

1. Raw dataset downloaded from Kaggle
2. Data cleaned and structured within a PostgreSQL database
3. Dataset exported for modelling
4. Feature analysis and exploratory data analysis performed in Jupyter Notebook
5. Random Forest classification model trained to predict borrower risk segments
6. Model deployed in a Streamlit dashboard for interactive predictions


## Machine Learning Model

A **Random Forest Classifier** is used to predict borrower risk categories based on financial indicators such as:

- Age
- Monthly income
- Debt ratio
- Credit utilization
- Late payment history
- Number of credit lines
- Real estate loans

The model classifies borrowers into five risk segments:

- Very Low Risk
- Low Risk
- Medium Risk
- High Risk
- Very High Risk


## Dashboard Features

The Streamlit dashboard allows users to:

- Input borrower financial information
- Predict credit risk segment
- View model confidence
- Visualize risk probability distribution


## Example Prediction

Users can enter borrower details such as income, debt ratio, and credit utilization to receive a predicted risk classification along with probability scores for each risk segment.


## Future Improvements

Potential enhancements include:

- Incorporating additional financial features
- Model explainability using SHAP values
- Hyperparameter tuning
- Integration with real-time data pipelines


## Author

Monya Cisternas  
Finance Data Science/Analytics
