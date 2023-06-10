from web3 import Web3
from dotenv import load_dotenv
import os
import json
import getpass
from mnemonic import Mnemonic
from utils import crypt

load_dotenv()

os.system('clear')
# Connect to node
web3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_NODE_GOERLI')))
public_key = ""
# Get contract abi
abi_path = 'artifacts/contracts/Pytheorus.sol/Pytheorus.json'
abi = ""
with open(abi_path) as f:
    data = json.load(f)
    abi = data["abi"]
    f.close()
    
# Create contract object    
contract = web3.eth.contract(address=web3.to_checksum_address(os.getenv('CONTRACT_ADDRESS')), abi=abi)

def get_transfer_events():    
    event_filter = contract.events.Transfer.create_filter(fromBlock=0, toBlock='latest')
    events = event_filter.get_all_entries()

    return events




