import json
from web3 import Web3

# Load the wallet configuration
with open('wallet-config.json') as f:
    wallet_config = json.load(f)

# Initialize Web3 for each network
eth_web3 = Web3(Web3.HTTPProvider(wallet_config['eth_node_url']))
bnb_web3 = Web3(Web3.HTTPProvider(wallet_config['bnb_node_url']))
polygon_web3 = Web3(Web3.HTTPProvider(wallet_config['polygon_node_url']))

# Retrieve and display balances
for network, web3 in zip(['ETH', 'BNB', 'Polygon'], [eth_web3, bnb_web3, polygon_web3]):
    for wallet in wallet_config['wallets']:
        balance = web3.eth.get_balance(wallet)
        print(f'Balance in {network} for wallet {wallet}: {web3.fromWei(balance, "ether")}')
