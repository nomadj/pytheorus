from web3 import Web3
from dotenv import load_dotenv
import os
import json
import getpass
from cryptography.fernet import Fernet
from mnemonic import Mnemonic
import binascii
from utils import crypt
import base64

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

# Check if launch file exists
launch_file = 'launch.py'
if os.path.isfile(launch_file):
    
    # Generate a new HD wallet
    account = web3.eth.account.create()
    mnemonic = Mnemonic("english").to_mnemonic(account._private_key)

    # Ask the user to enter a password for encryption
    password = getpass.getpass(prompt='Enter a password for encryption: ')

    ciphertext, salt = crypt.encrypt_string(password, mnemonic)
    with open("mnemonic.txt", "w") as f:
        json.dump(ciphertext.decode(), f)

    with open("salt.txt", "w") as f:
        json.dump(salt.hex(), f)
    os.system('rm launch.py')
    print("Wallet created.")

else:
    authenticated = False

    print("Welcome back!\n")
    password = getpass.getpass(prompt='Enter a password to retrieve your mnemonic: ')
    with open("salt.txt", "r") as f:
        salt = json.load(f)
        salt_bytes = bytes.fromhex(salt)

    while not authenticated:
        try:
            with open("mnemonic.txt", "r") as f:
                encrypted_text = json.load(f).encode()
            decrypted_text = crypt.decrypt_string(password, encrypted_text, salt_bytes)
            authenticated = True
            web3.eth.account.enable_unaudited_hdwallet_features()
            wallet = web3.eth.account.from_mnemonic(decrypted_text)
            public_key = wallet.address
        except Exception:
            password = getpass.getpass(prompt='Nope, try again -> ')
    
        




