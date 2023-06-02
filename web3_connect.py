from web3 import Web3
from dotenv import load_dotenv
import os
import json

load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_NODE_GOERLI')))
abi_path = 'artifacts/contracts/Pytheorus.sol/Pytheorus.json'
abi = ""
with open(abi_path) as f:
    data = json.load(f)
    abi = data["abi"]
    f.close()
contract = web3.eth.contract(address=web3.to_checksum_address(os.getenv('CONTRACT_ADDRESS')), abi=abi)


