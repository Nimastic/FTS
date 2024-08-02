from web3 import Web3

# Infura Sepolia Testnet URL with API key
infura_url = "https://sepolia.infura.io/v3/"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if not web3.is_connected():
    raise Exception("Failed to connect to Sepolia Testnet")

# Query balance
wallet_address = ""
balance = web3.eth.get_balance(wallet_address)

# Convert balance from Wei to Ether
ether_balance = web3.from_wei(balance, 'ether')
print(f"Balance of wallet {wallet_address}: {ether_balance} ETH")
