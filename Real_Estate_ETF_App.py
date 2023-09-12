import streamlit as st
import pandas as pd

# Load your CSV data
icf_returns_df = pd.read_csv("ICF_Cumulative_Df.csv")
icf_aglo_evaluation_df = pd.read_csv("Algo_Evaluation_Df.csv")

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

if __name__ == "__main__":
    main()
