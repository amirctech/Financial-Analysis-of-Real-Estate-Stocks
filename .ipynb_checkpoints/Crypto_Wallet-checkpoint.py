# Imports

import os
import requests
from dotenv import load_dotenv

load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy



# Wallet functionality

def generate_account():
    # Fetch mnemonic from environment variable
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derivce_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account



def get_balance(w3, address):
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)
    
    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")
    
    # Return the value in ether
    return ether




def send_transaction(w3, account, to, wage):
    # Set gas price strategy
    w3. eth.setGasPriceStrategy(medium_gas_price_strategy)
    
    # Convert eth amount to Wei
    value = w3.toWei(wage, "ether")
    
    # Calcualte gas estimate
    gasEstiamte = w3.eth.estiamteGas(
        {"to": to, "from": account.address, "value": value}
    )
    