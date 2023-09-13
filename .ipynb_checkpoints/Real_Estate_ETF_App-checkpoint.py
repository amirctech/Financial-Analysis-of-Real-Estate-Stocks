import streamlit as st
import pandas as pd

# Load your CSV data
icf_returns_df = pd.read_csv("ICF_Cumulative_Df.csv")
icf_aglo_evaluation_df = pd.read_csv("ICF_Algo_Evaluation_Df.csv")

# Define ETFs and their details
etf_database = {
    "ICF": {
        "Name": "ICF",
        "Ethereum ETF Address": "0x27d2B045b40A279C7b11E51DCB187753b548a6Dd",
        "Cumulative Returns": -0.161367,
        "Closing Price": 55.54,
        "Image": "Images/commercial_realestate.jpg"
    },
    "ABC": {
        "Name": "ABC",
        "Ethereum ETF Address": "0x7b11532BD84e2cA98467E3591d162E728a2C0f6e",
        "Cumulative Returns": -0.161367,
        "Closing Price": 55.54,
        "Image": "Images/commercial_realestate.jpg"
    },
    "CVS": {
        "Name": "CVS",
        "Ethereum ETF Address": "0xd4008409A7dFEdc20Af7CdD22c9FD6EaFAe48D97",
        "Cumulative Returns": -0.161367,
        "Closing Price": 55.54,
        "Image": "Images/commercial_realestate.jpg"
    }
}

# Create a list of ETF names
etfs = list(etf_database.keys())

# Streamlit app
def main():
    st.title("ETF Analysis")
    
    # Display ETF details
    selected_etf = st.selectbox("Select an ETF", etfs)
    etf_details = etf_database[selected_etf]
    
    st.image(etf_details["Image"], width=200)
    st.write("Name:", etf_details["Name"])
    st.write("Ethereum ETF Address:", etf_details["Ethereum ETF Address"])
    st.write(f"Cumulative Returns: {etf_details['Cumulative Returns']:.6f}")
    st.write(f"Current Price Per Share: {etf_details['Closing Price']} eth")
    
    # Create buttons to show analysis
    if st.button("Show Financial Analysis"):
        st.write(f"Financial Analysis for {etf_details['Name']}")
        st.table(icf_aglo_evaluation_df)
        st.line_chart(icf_returns_df)
    
    # Streamlit application headings
    st.markdown("# RealEstateETFApp")
    st.markdown("## Invest In Real Estate ETFs")
    st.text(" \n")
    
    # Streamlit Sidebar Code - Start
    st.sidebar.markdown("## ETF Account Addresses & Ethernet Balance in Ether")
    
    # Call the 'generate_account' function and save it as the variable 'account'
    account = generate_account()
    
    # Write the client's Ethereuma ccount address to the sidebar
    st.sidebar.write(account.address)
    
    # Call the 'get_balance' function and pass it your account address
    # Write the returned ether balance to the sidebar
    balance = get_balance(w3, account.address)
    st.sidebar.write(balance)
    
    #Create a select box to chose a Real Estate ETF
    etf = st.sidebar.number_input("Select a Real Estate ETF", etfs)
    
    # Create a input field to record the number of shares requested
    shares = st.sidebar.number_input("Number of Shares")
    
    st.sidebar.markdown("## Real Estate ETF Name, Price per Share, & Ethereum Address")
    
    # Identify the Real Estate ETF
    etfname = etf_database[etf][0]
    
    # Write the RealEstateETF etf's name to the sidebar
    st.sidebar.write(etfname)
    
    # Identify the RealEstateETf etf's closing price
    closing_price = etf_database[etf][3]
    
    # Write the closing price to the sidebar
    st.sidebar.write(closing_price)
    
    # Identify the RealEstateETfs etf's Ethereum Address
    etfs_address = etf_database[etf][1]
    
    # Write the etf's Ethereum Address to the sidebar
    st.sidebar.write(etfs_address)
    
    # Write the total shares in Ether
    st.sidebar.markdown("## Total Shares in Ether")

if __name__ = "__main__":
    main()
