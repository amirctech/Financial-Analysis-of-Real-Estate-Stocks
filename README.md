## Final Project Located in Files

- Farmland Portfolio-CORN.ipynb
- Commercial Portfolio-ICF.ipynb
- Housing Portfolio-XLRE.ipynb
- Crypto_Wallet.py
- Real_Estate_ETF_App.py

## Description

Financial Analysis in Real Estate Stocks project focused on computing algorithmic returns for three real estate stocks. The team researched the 3 best real estate stocks in the agriculture, commercial and housing industry and pulled the ticker data from Alpaca APIs. Utilizing machine learning models such as Logistic Regression and Single Moving Averages, the team aimed for the best accuracy, precision, and f-1 score in the confusion matrix to establish a buy/sell signal. With the signal, the team computed algorithmic returns for each of the real estate stocks and ensured it outperformed the actual returns. We then calculated portfolio evaluation metrics for each of the real estate stocks to ensure users can make a sound investment decision. After completing the financial analysis, the team created the crypto wallet using Web3 and a streamlit app for users to select, visualize the returns, and invest in the real estate stocks via Ethereum.

The tool provides a mechanism for users to create financial analysis of real estate stocks to visualize and invest on a Streamlit using cryptocurrency.


## Project Procedure

1. **Data Collection**
   - Gather historical financial data, including closing prices, for the past 5 years for the selected real estate stocks. This data is obtained from reliable sources or APIs such as Alpaca.

2. **Algorithmic Returns Calculation**
   - Implement machine learning models, such as Logistic Regression and Single Moving Averages, to calculate algorithmic returns for the chosen real estate stocks. The objective is to generate buy/sell signals that maximize accuracy, precision, and F1 score through the use of a confusion matrix.

3. **Portfolio Evaluation Metrics**
   - Compute a comprehensive set of portfolio evaluation metrics to assess the performance of each real estate stock. These metrics include:
     - Annualized return: A measure of the annual profit or loss percentage.
     - Cumulative returns: The overall returns over the investment period.
     - Annual volatility: A gauge of the investment's price fluctuations over a year.
     - Sharpe ratio: Evaluates the risk-adjusted return of the portfolio.
     - Sortino ratio: Assesses the return relative to downside risk, focusing on negative returns.

4. **Results Compilation**
   - Organize and compile the computed results into three separate CSV files, each representing an Exchange-Traded Fund (ETF). These CSV files serve as data sources for the dashboard.

5. **Dashboard Development**
   - Utilize Streamlit, Python, and the Web3 library to design and create an interactive dashboard. This dashboard should provide the following functionalities:
     - Selection of one of the three distinct Real Estate ETFs (Agriculture, Commercial, Housing).
     - Visualization of financial metrics and algorithmic returns using informative charts and graphs.
     - Integration of Crypto Wallets for both ETFs and investors, allowing seamless cryptocurrency transactions.
     - Input areas for investors to provide their personal details, including name, address, and contact number.
     - Enable users to buy/invest in the selected ETFs directly through the platform.
     - Implement validation mechanisms to confirm transactions and display the associated transaction hash.

6. **Prototype Testing**
   - Rigorously test the Streamlit app prototype to ensure its functionality and user-friendliness. Verify the app's performance by selecting different ETFs and completing cryptocurrency transactions.

## Libraries & Imports

- Pandas
- APIs
- Numpy
- Pathlib
- SkLearn
- LogisticRegression
- Datetime
- StandardScaler
- Train_test_split
- Confusion_matrix
- Accuracy_score
- Classifcation_report
- Streamlit
- W3
- Dataclasses
- Os
- Requests
- Dotenv
- Bip44
- Web3.gas_strategies.time-based


## Requirements
To use this script, you will need to have Python installed along with the libraries mentioned above. 

## How to Use

Follow these steps to utilize the Financial Analysis in Real Estate Stocks platform effectively:

1. **Install Dependencies**
   - Ensure that all necessary dependencies, including Python, W3, Ganache, and Streamlit, are properly installed on your system.

2. **Clone the Repository**
   - Clone the project repository to your local machine using Git or your preferred version control tool. This can be done with the following command:
     ```
     git clone <repository_url>
     ```

3. **Run the Jupyter Notebook Script**
   - Navigate to the project directory and run the Jupyter Notebook script provided. This script is responsible for data collection and algorithmic returns calculation.

4. **Launch the Streamlit App**
   - Open a terminal and navigate to the project directory.
   - Run the Streamlit app using the following command:
     ```
     streamlit run Real_Estate_ETF_App.py
     ```

5. **Select a Real Estate ETF**
   - Within the Streamlit app interface, choose one of the three real estate ETF options (Agriculture, Commercial, Housing) to analyze and invest in.

6. **View Financial Analysis**
   - Click the "Show Financial Analysis" button to access detailed financial metrics and algorithmic returns for the selected ETF.

7. **Provide Investor Details**
   - In the sidebar, fill in the necessary details about the investor, including name, address, and contact number. This information may be required for transaction processing and record-keeping.

8. **Initiate the Transaction**
   - Hit the "Transact" button to initiate the investment transaction in the chosen ETF. The system will process the transaction request.

9. **Transaction Validation**
   - Ensure that the sidebar validates the transaction and displays the transaction hash. This hash serves as a confirmation of your investment in the real estate ETF.

By following these steps, you can effectively use the platform to analyze real estate stocks, make investment decisions, and conduct transactions securely via cryptocurrency.

## Images & Visuals

## Next Steps

- Financial Planner tab that visualizes the details of each transaction
- Live conversion of Dollars to Cryptocurrency for the returns & metrics
- More interactive visuals and components of the streamlit app
- Creating a side by side or comparison view of each of the real estate stocks
- Different machine learning models to increase the returns of each stock
