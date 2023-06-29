## 🧧 Bank delinquency on a loan - Банковская просрочка по кредиту

The dataset contains information about the clients of a certain bank. Your task is to predict the target variable according to various characteristics of clients - whether the client had a delay of 90 or more days or not (and if he/she did have a delay, the bank will not issue a loan to this client, otherwise it would)

Датасет содержит информацию о клиентах некоторого банка.
Ваша задача состоит в том, чтобы по различным характеристикам клиентов спрогнозировать целевую переменную - имел клиент просрочку 90 и более дней или нет (и если имел, то банк не будет выдавать кредит этому клиенту, а иначе будет)
     
## ✅ Data description - Описание данных

- RevolvingUtilizationOfUnsecuredLines: общий баланс средств (total balance on credit cards and personal lines of credit except real estate and no installment debt like car loans divided by the sum of credit limits)

- age: возраст заемщика

- NumberOfTime30-59DaysPastDueNotWorse: сколько раз за последние 2 года наблюдалась просрочка 30-59 дней

- DebtRatio: ежемесячные расходы (платеж по долгам, алиментам, расходы на проживания) деленные на месячный доход

- MonthlyIncome: ежемесячный доход

- NumberOfOpenCreditLinesAndLoans: количество открытых кредитов (напрмер, автокредит или ипотека) и кредитных карт

- NumberOfTimes90DaysLate: сколько раз наблюдалась просрочка (90 и более дней)

- NumberRealEstateLoansOrLines: количество кредиов (в том числе под залог жилья)

- RealEstateLoansOrLines: закодированное количество кредиов (в том числе под залог жилья) - чем больше код буквы, тем больше кредитов

- NumberOfTime60-89DaysPastDueNotWorse: сколько раз за последние 2 года заемщик задержал платеж на 60-89 дней

- NumberOfDependents: количество иждивенцев на попечении (супруги, дети и др)

- GroupAge: закодированная возрастная группа - чем больше код, тем больше возраст

## ✅ Target varible - Целевая переменная

- SeriousDlqin2yrs: клиент имел просрочку 90 и более дней

## ✅ Algorithm used - Использованный алгоритм

Logistic Regression is used as a Baseline Model. This report presents an approach to predict the credit scores of customers using the Logistic Regression machine learning algorithm. The research objective of this project is to perform a comparative study between feature selection and feature extraction, against the same dataset using the Logistic Regression machine learning algorithm. 

Логистическая регрессия используется в качестве базовой модели. В этом отчете представлен подход к прогнозированию кредитных рейтингов клиентов с использованием алгоритма машинного обучения логистической регрессии. Целью исследования этого проекта является проведение сравнительного исследования между выбором признаков и извлечением признаков на одном и том же наборе данных с использованием алгоритма машинного обучения логистической регрессии.

## ✅ Data processing steps - Обработка данных

Below is the description of the data cleaning steps before substantial training.

1. Data cleaning from duplicates. Replacing columns with object data type values ​​to numeric ones.
2. Determination of correlation dependencies. Replacing Nan values ​​in three columns with median values:
Unknown age: 14733 (>9%)
Unknown monthly income: 29195 (>19%)
Unknown number of dependents: 3824 (>2%)
3. The decision made: not to accept AgeGroup in training the model.

Ниже дано описание шагов по очистке данных перед непосредственно самим обучением.

1. Очистка данных от дубликатов. Замена столбцов со значеними объектного типа данных на числовые.
2. Определение корреляционных зависимостей переменных. Замена значений Nan в трёх столбцах на медианные значения:
Unknown age: 14733 (>9%)
Unknown monthly income: 29195 (>19%)
Unknown number of dependents: 3824 (>2%)
3. Решение не учитывать AgeGroup в обучении модели.
