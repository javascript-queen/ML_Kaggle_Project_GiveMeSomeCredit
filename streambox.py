import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import xgboost as xgb

def main():
    st.title('Can we trust you? :nerd_face:') 
    st.image("biz_man.png")
    model = xgb.Booster()
    model.load_model('xgb_model.json')

    st.subheader('Enter Customer Information')
    revolving_utilization = st.number_input('Revolving Utilization of Unsecured Lines', min_value=0, value=0)
    age = st.number_input('Age', min_value=0, value=0)
    debt_ratio = st.number_input('Debt Ratio', min_value=0.0, value=0.0)
    monthly_income = st.number_input('Monthly Income', min_value=0.0, value=0.0)
    open_credit_lines_loans = st.number_input('Number of Open Credit Lines and Loans', min_value=0, value=0)
    real_estate_loans = st.number_input('Number of Real Estate Loans or Lines', min_value=0, value=0)
    dependents = st.number_input('Number of Dependents', min_value=0, value=0)
    delinquencies_90_days = st.number_input('Total Delinquencies in the Last 90 Days', min_value=0, value=0)
    if st.button('Predict'):
            df = pd.DataFrame({
            'age': [age],
            'MonthlyIncome': [monthly_income],
            'NumberOfOpenCreditLinesAndLoans': [open_credit_lines_loans],
            'NumberRealEstateLoansOrLines': [real_estate_loans],
            'NumberOfDependents': [dependents],
            'RevolvingUtilizationOfUnsecuredLines': [revolving_utilization],
            'DebtRatio': [debt_ratio],
            'TotalDelinquencies90DaysLate': [delinquencies_90_days]})

            preprocessed_data = preprocess_data(df)

            # Predictions
            prediction = model.predict(preprocessed_data)
            prediction_proba = model.predict_proba(preprocessed_data)[:, 1]
            predictions_df = pd.DataFrame({
                'Predicted SeriousDlqin2yrs': prediction,
                'Predicted Probability of default': prediction_proba
            })
            st.subheader('Predictions')
            st.write(predictions_df)

def preprocess_data_csv(test_df):
    test_df = test_df.drop(['SeriousDlqin2yrs'], axis=1)
    test_df['TotalDelinquencies90DaysLate'] = test_df['NumberOfTimes90DaysLate'] + test_df['NumberOfTime60-89DaysPastDueNotWorse'] + test_df['NumberOfTime30-59DaysPastDueNotWorse']
    test_df.drop(['NumberOfTimes90DaysLate', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfTime30-59DaysPastDueNotWorse'], axis=1, inplace=True)

    numeric_features = ['RevolvingUtilizationOfUnsecuredLines', 'age', 'DebtRatio',
                        'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                        'NumberRealEstateLoansOrLines', 'NumberOfDependents', 'TotalDelinquencies90DaysLate']
    # Median
    imputer = SimpleImputer(strategy='median')
    test_df[numeric_features] = imputer.fit_transform(test_df[numeric_features])
    scaler = StandardScaler()
    test_df[numeric_features] = scaler.fit_transform(test_df[numeric_features])
    return test_df

def preprocess_data(test_df):
    numeric_features = ['RevolvingUtilizationOfUnsecuredLines', 'age', 'DebtRatio',
                        'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                        'NumberRealEstateLoansOrLines', 'NumberOfDependents', 'TotalDelinquencies90DaysLate']
    # Median
    imputer = SimpleImputer(strategy='median')
    test_df[numeric_features] = imputer.fit_transform(test_df[numeric_features])
    scaler = StandardScaler()
    test_df[numeric_features] = scaler.fit_transform(test_df[numeric_features])
    return test_df

if __name__ == '__main__':
    main()
    
    
