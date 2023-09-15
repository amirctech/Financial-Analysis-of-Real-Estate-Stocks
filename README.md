# Financial-Analysis-of-Real-Estate-Stocks

## Description

In this project, we created a financial analytics dashboard via Streamlit that presented 3 different real estate ETF portfolios in which anyone could invest through Ethereum.
We selected an ETF from 3 different sectors which included XLRE(Residential), ICF(Commercial) and CORN(Agriculture).
The dashboard provides a brief selection of critical metrics that are useful in deciding whether the selected ETF is worth investing in.

## Procedure

1. Data Collection: We gathered historical market data for each ETF through Yahoo Finance and Alpaca API.

2. Defining Metrics: Using the pandas library, we take the closing prices of each ETF and calculate such metrics as daily returns, annualized returns, cumulative returns, annual volatility, sharpe ratio, and sortino ratio.

4. Trading Algorithm: We defined Short and Long Positions and trained the Logistic Regression model to determine when to buy/sell.

5. Backtesting and Metrics: The trading algorithm's performance is evaluated through backtesting the metrics mentioned above.

6. Display Results: By exporting the dataframes containing the final results into csv files, we then import those csv files into Streamlit for them to be displayed on the dashboard.


## Libraries and Imports Used
- pandas
- Yahoo Finance
- APIs
- numpy
- pathlib
- Sklearn
- LogisticRegression
- datetime
- StandardScaler
- train_test_split
- confusion_matrix
- accuracy_score
- classification_report
- Streamlit

## Requirements
To use this script, you will need to have Python installed along with the libraries mentioned above. 

## How to Use
1. Clone the repository.
2. Run Real_Estate_ETF_App.py file on streamlit using a terminal

## Images

## Findings and Conclusions
