import json
import requests
from web3 import Web3

# Configuration
CONFIG_FILE = 'wallet-config.json'

# RPC Endpoints for different networks
RPC_ENDPOINTS = {
    'Ethereum': 'https://eth.publicnode.com',
    'BNB Smart Chain': 'https://bsc-dataseed1.binance.org',
    'Polygon': 'https://polygon-rpc.com'
}

class PortfolioTracker:
    def __init__(self, config_file):
        """Initialize the portfolio tracker with config file"""
        with open(config_file, 'r', encoding='utf-8-sig') as f:
            self.config = json.load(f)
        
        self.owner = self.config['owner']
        self.primary_wallet = self.config['primary_wallet']
        self.secondary_wallet = self.config['secondary_wallet']
        self.networks = self.config['networks']
        
        print(f"\n{'='*60}")
        print(f"Portfolio Tracker for: {self.owner}")
        print(f"{'='*60}\n")
    
    def get_wallet_balance(self, wallet_address, network):
        """Fetch wallet balance for a specific network"""
        try:
            rpc_url = RPC_ENDPOINTS.get(network)
            if not rpc_url:
                print(f"⚠️  Network {network} not supported")
                return None
            
            web3 = Web3(Web3.HTTPProvider(rpc_url))
            
            # Check connection
            if not web3.is_connected():
                print(f"❌ Failed to connect to {network}")
                return None
            
            # Get balance in Wei
            balance_wei = web3.eth.get_balance(wallet_address)
            
            # Convert to native token (ETH, BNB, MATIC)
            balance = web3.from_wei(balance_wei, 'ether')
            
            return float(balance)
        
        except Exception as e:
            print(f"❌ Error fetching balance from {network}: {str(e)}")
            return None
    
    def get_network_token_symbol(self, network):
        """Return the token symbol for each network"""
        symbols = {
            'Ethereum': 'ETH',
            'BNB Smart Chain': 'BNB',
            'Polygon': 'MATIC'
        }
        return symbols.get(network, 'UNKNOWN')
    
    def display_wallet_balances(self, wallet_address, wallet_name):
        """Display balances for a wallet across all networks"""
        print(f"\n📊 {wallet_name}: {wallet_address}")
        print(f"{'-'*60}")
        
        total_usd = 0
        balances = {}
        
        for network in self.networks:
            balance = self.get_wallet_balance(wallet_address, network)
            token_symbol = self.get_network_token_symbol(network)
            
            if balance is not None:
                balances[network] = balance
                print(f"✅ {network:20} | {balance:>12.6f} {token_symbol}")
            else:
                print(f"❌ {network:20} | Connection failed")
        
        return balances
    
    def run(self):
        """Run the portfolio tracker"""
        print(f"Available Networks: {', '.join(self.networks)}\n")
        
        # Fetch balances for primary wallet
        primary_balances = self.display_wallet_balances(
            self.primary_wallet, 
            "Primary Wallet"
        )
        
        # Fetch balances for secondary wallet
        secondary_balances = self.display_wallet_balances(
            self.secondary_wallet, 
            "Secondary Wallet"
        )
        
        print(f"\n{'='*60}")
        print("✨ Portfolio Summary Complete!")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    tracker = PortfolioTracker(CONFIG_FILE)
    tracker.run()