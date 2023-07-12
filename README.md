# 🌐 Stack Overflow Annual Developer Survey

In May 2023 over 90,000 developers responded to Stack Overflow annual survey about how they learn and level up, which tools they're using, and which ones they want.
     
## ✅ Data description 

There are seven sections in this survey. The 2nd, 3rd, 4th and 5th sections will appear in a random order. Most questions in this survey are optional. Required questions are marked with *. 

1. Basic Information

2. Education, Work, and Career

3. Technology and Tech Culture

4. Stack Overflow Usage + Community

5. Artificial Intelligence

6. Professional Developer Series (Optional)

7. Final Questions


I chose to analyze the data inputs which are listed below:

- Country 
- EdLevel - Education Level
- Experience - Coding working experience in years
- CompConvertedYearly - Devs' salary per year

The data is chosen to predict the yearly salary depending on your country, experience, and level of education.
   
## ✅ Target varible

- CompConvertedYearly

## ✅ Algorithm used - Random Forest (Regression)

Random forests are a way of averaging multiple deep decision trees, trained on different parts of the same training set, with the goal of reducing the variance.

https://www.javatpoint.com/machine-learning-random-forest-algorithm![image](https://github.com/javascript-queen/StackOverflow_Survey_2023_Prediction/assets/90614620/3bc1c597-fa16-4788-afdb-5b482eeb56bb)


## ✅ Data processing steps

Below is the description of the data cleaning steps before substantial training.

1. Data preprocessing.
2. Data cleaning from null values, outliers.
3. Replacing columns with object data type values ​​to numeric ones where needed.
4. Choosing a regression model.

## ✅ Streamlit Webapp - Streamlit Приложение

<img width="794" alt="Screenshot 2023-07-12 at 08 59 34" src="https://github.com/javascript-queen/StackOverflow_Survey_2023_Prediction/assets/90614620/5dae0cd7-a529-4fc6-8d26-aa5fba5650d6">

<img width="791" alt="Screenshot 2023-07-12 at 08 59 20" src="https://github.com/javascript-queen/StackOverflow_Survey_2023_Prediction/assets/90614620/b283c8c5-0989-49f4-8c8f-e8cbb96d3cd0">

