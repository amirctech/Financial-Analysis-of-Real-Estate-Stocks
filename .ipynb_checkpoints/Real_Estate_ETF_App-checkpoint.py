import streamlit as st
import pandas as pd
from Crypto_Wallet import *
from typing import Any, List
from web3 import Web3
from PIL import Image
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Load your CSV data
icf_returns_df = pd.read_csv("ICF_Cumulative_Df.csv")
icf_aglo_evaluation_df = pd.read_csv("ICF_Algo_Evaluation_Df.csv")
corn_returns_df = pd.read_csv("Farmland_ETF_Returns.csv")
corn_algo_evaluation_df = pd.read_csv("Farmland_Backtest.csv")
xlre_returns_df = pd.read_csv("XLRE_Returns_Df.csv")
xlre_algo_evaluation_df = pd.read_csv("XLRE_Backtest.csv")


# Define ETFs and their details
etf_database = {
    "ICF: Commercial Real Estate": {
        "Name": "ICF: iShares Cohen & Steers REIT ETF",
        "Ethereum ETF Address": "0x27d2B045b40A279C7b11E51DCB187753b548a6Dd",
        "Cumulative Returns": -0.161367,
        "Closing Price": 0.03311506251312659,
        "Image": "Images/commercial_realestate.jpg"
    },
    "CORN: Agriculture Real Estate": {
        "Name": "CORN: Teucrium Corn Fund",
        "Ethereum ETF Address": "0x7b11532BD84e2cA98467E3591d162E728a2C0f6e",
        "Cumulative Returns": 0.0121000,
        "Closing Price": 0.01337631776821826,
        "Image": "Images/agriculture_realestate.jpg"
    },
    "XLRE: Housing Real Estate": {
        "Name": "XLRE: Real Estate Select Sector SPDR Fund",
        "Ethereum ETF Address": "0xd4008409A7dFEdc20Af7CdD22c9FD6EaFAe48D97",
        "Cumulative Returns": -0.161367,
        "Closing Price": 0.02239939602606963,
        "Image": "Images/housing_realestate.jpg"
    }
}

# Create a list of ETF names
etfs = list(etf_database.keys())

# New session state variables - global
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'phone' not in st.session_state:
    st.session_state.phone = ""
if 'address' not in st.session_state:
    st.session_state.address = ""
if 'transaction_hash' not in st.session_state:
    st.session_state.transaction_hash = ""
if 'years' not in st.session_state:
    st.session_state.years = ""
if 'total' not in st.session_state:
    st.session_state.total = ""
if 'etfname' not in st.session_state:
    st.session_state.etfname = ""
if 'etf_details' not in st.session_state:
    st.session_state.etf_details = ""
    
# Streamlit app

def descriptor():
    st.markdown("# REAL ESTATE ETF INVESTMENT APP")
    st.markdown("## Invest In Real Estate ETFs w/ Ethereum")
    st.text('''
    The Real Estate ETF Investment App displays comprehensive insights and investment opportunities in the real estate stock market.
    The financial analysis runs on the computation of algorithmic returns for three carefully chosen real estate stocks, each representing a distinct sector: agriculture, commercial, and housing. 
    This initiative combines data-driven analysis, machine learning, and blockchain technology to empower investors with valuable tools and details that allow for high returns and profits.
    ''')
    landing = Image.open('Images/real_estate_stock_landing_page.jpg')
    st.image(landing, caption='High rises overlayed with analytical graphs')
    
def main():
    # Streamlit application headings
    st.markdown("# RealEstateETFApp")
    st.markdown("## Invest In Real Estate ETFs")
    st.text(" \n")

    # Display ETF details
    selected_etf = st.selectbox("Select an ETF", etfs)
    st.session_state.etf_details = etf_database[selected_etf]

    st.image(st.session_state.etf_details["Image"], width=200)
    st.write("Name:", st.session_state.etf_details["Name"])
    st.write("Ethereum ETF Address:", st.session_state.etf_details["Ethereum ETF Address"])
    st.write(f"Cumulative Returns: {st.session_state.etf_details['Cumulative Returns']:.6f}")
    st.write(f"Current Price Per Share: {st.session_state.etf_details['Closing Price']} eth")

    # Set the Google Finance URLs
    url_icf = "https://www.google.com/finance/quote/ICF:BATS?sa=X&sqi=2&ved=2ahUKEwibwaqC-K2BAxUBkIkEHXgGBVgQ3ecFegQIGhAf"
    url_corn = "https://www.google.com/finance/quote/CORN:NYSEARCA?sa=X&ved=2ahUKEwiE7L-t-q2BAxXGJTQIHfqvDksQ3ecFegQIFxAf"
    url_xlre = "https://www.google.com/finance/quote/XLRE:NYSEARCA?sa=X&ved=2ahUKEwjXzKqMt7WBAxXGjokEHVzpAyoQ3ecFegQIHBAf"

    # Create buttons to show analysis
    if st.button("Show Financial Analysis"):
        st.write(f"Financial Analysis for {st.session_state.etf_details['Name']}")
        if selected_etf == "ICF: Commercial Real Estate":
            st.markdown("ICF Financial Evaluation Metrics")
            st.table(icf_aglo_evaluation_df)
            st.markdown("ICF Returns 2018-11-19 to 2023-03-27 $")
            st.line_chart(icf_returns_df)
            st.markdown("Checkout [Google Finance ICF Breakdown](%s)" % url_icf)
        elif selected_etf == "CORN: Agriculture Real Estate":
            st.markdown("CORN Financial Evaluation Metrics")
            st.table(corn_algo_evaluation_df)
            st.markdown("CORN Returns 2018-11-19 to 2023-03-27 $")
            st.line_chart(corn_returns_df)
            st.markdown("Checkout [Google Finance CORN Breakdown](%s)" % url_corn)
        elif selected_etf == "XLRE: Housing Real Estate":
            st.markdown("XLRE Financial Evaluation Metrics")
            st.table(xlre_algo_evaluation_df)
            st.markdown("XLRE Returns 2018-11-19 to 2023-03-27 $")
            st.line_chart(xlre_returns_df)
            st.markdown("Checkout [Google Finance XLRE Breakdown](%s)" % url_xlre)

    # Streamlit Sidebar Code - Start
    st.sidebar.markdown("## ETF Account Addresses & Ethernet Balance in Ether")

    # Call the 'generate_account' function and save it as the variable 'account'
    account = generate_account()

    # Write the client's Ethereum account address to the sidebar
    # Use the 'account' variable
    st.sidebar.write(account.address)

    # Call the 'get_balance' function and pass it your account address
    # Write the returned ether balance to the sidebar
    # Use the 'balance' variable
    balance = get_balance(w3, account.address)
    st.sidebar.write(balance)

    # Create a select box to choose a Real Estate ETF
    selected_etf_sidebar = st.sidebar.selectbox("Select a Real Estate ETF", etfs)

    # Add an event handler to update etfname based on the selected ETF
    if st.session_state.etfname != selected_etf_sidebar:
        st.session_state.etfname = selected_etf_sidebar

    # Create an input field to record the number of shares requested
    shares = st.sidebar.number_input("Number of Shares")

    st.sidebar.markdown("## Real Estate ETF Name, Price per Share, & Ethereum Address")

    # Identify the Real Estate ETF
    st.session_state.etfname = st.session_state.etf_details["Name"]

    # Write the Real Estate ETF's name to the sidebar
    st.sidebar.write(st.session_state.etfname)

    # Identify the Real Estate ETF's closing price
    closing_price = st.session_state.etf_details["Closing Price"]

    # Write the closing price to the sidebar
    st.sidebar.write(closing_price)

    # Identify the Real Estate ETF's Ethereum Address
    etfs_address = st.session_state.etf_details["Ethereum ETF Address"]

    # Write the ETF's Ethereum Address to the sidebar
    st.sidebar.write(etfs_address)

    # Write the total shares in Ether
    st.sidebar.markdown("## Total Shares in Ether")

    # Calculate total shares in eth for the ETF
    st.session_state.total = st.session_state.etf_details["Closing Price"] * shares

    # Write the 'total' calculation to the Streamlit sidebar
    st.sidebar.write(st.session_state.total)

    st.session_state.name = st.sidebar.text_input("Name of Investor")
    st.session_state.phone = st.sidebar.text_input("Phone Number")
    st.session_state.address = st.sidebar.text_input("Address")
    st.session_state.years = st.sidebar.slider("How many years would you like to invest?", 0,5)
    name = st.session_state.name
    phone = st.session_state.phone
    etfname = st.session_state.etfname
    address = st.session_state.address
    years = st.session_state.years
    total = st.session_state.total
    
    # Save the transaction hash that the 'send_transaction' function returns as a variable and have it display on the application's web interface
    if st.sidebar.button("Send Transaction"):
        
        # Call the send_transaction function and pass it the necessary parameters
        st.session_state.transaction_hash = send_transaction(w3, account, etfs_address, total, name, phone, address, years)
        
        # Markdown for the transaction hash
        st.sidebar.markdown("#### Validated Transaction Hash")
        
        # Write the returned transaction hash to the screen
        st.sidebar.write(st.session_state.transaction_hash)
        
        #Call hash_view
        #hash_view()

def hash_view():
    st.markdown("# Review Transaction Hash Details")
    
    if st.button("View Transaction Details"):
        st.markdown("## Transaction Details")
        st.write(f"Name: {st.session_state.name}")
        st.write(f"Phone Number: {st.session_state.phone}")
        st.write(f"ETF: {st.session_state.etfname}")
        st.write(f"Address: {st.session_state.address}")
        st.write(f"Total Ethereum: {st.session_state.total}")
        st.write(f"Years: {st.session_state.years}")
        st.write(f"Transaction Hash: {st.session_state.transaction_hash}")

page_names_to_funcs = {
    "Real Estate ETF App Breakdown": descriptor,
    "Real Estate ETF Investment Page": main,
    "Financial Planner Hash View": hash_view
}

def main_app():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", list(page_names_to_funcs.keys()))
    page_function = page_names_to_funcs[selected_page]
    page_function()

if __name__ == "__main__":
    main_app()