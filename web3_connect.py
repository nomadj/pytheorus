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

def web3_init():
    os.system('clear')
    wallet = None
    # web3_init.wallet = None
    # Check if launch file exists
    launch_file = 'launch.py'
    if os.path.isfile(launch_file):
        # Get user's handle and set up a new wallet
        name = input("Hello new user. This is Pyasynth, the original interface for the Pytheorus Composer's Registry.\nPlease enter the screen name you would like to use for publishing -> ")
        account = web3.eth.account.create()
        mnemonic = Mnemonic("english").to_mnemonic(account._private_key)

        # Encrypt the mnemonic and persist to a json file
        password = getpass.getpass(prompt='Enter a password for your wallet -> ')

        ciphertext, salt = crypt.encrypt_string(password, mnemonic)
        settings = {'mnemonic': ciphertext.decode(), 'salt': salt.hex()}
        data = json.dumps(settings)
        with open('settings.json', 'w') as f:
            f.write(data)
        os.system('rm launch.py')
        print("Wallet created.")

    else:
        authenticated = False

        print('Welcome back!\n')
        password = getpass.getpass(prompt='Enter a password to retrieve your wallet -> ')

        while not authenticated:
            try:
                with open('settings.json', 'r') as f:
                    settings = json.load(f)
                salt_bytes = bytes.fromhex(settings['salt'])            
                decrypted_text = crypt.decrypt_string(password, settings['mnemonic'].encode(), salt_bytes)
                authenticated = True
                web3.eth.account.enable_unaudited_hdwallet_features()
                wallet = web3.eth.account.from_mnemonic(decrypted_text)
                public_key = wallet.address
                print(public_key)
            except Exception:
                password = getpass.getpass(prompt='Nope, try again -> ')

def get_transfer_events():    
    event_filter = contract.events.Transfer.create_filter(fromBlock=0, toBlock='latest')
    events = event_filter.get_all_entries()

    return events




