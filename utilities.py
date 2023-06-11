import os
from web3_connect import *
import mimetypes

def wallet():
    wallet = None
    decrypted_text = None
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
        mint_song()
    else:
        authenticated = False
        password = getpass.getpass(prompt='Enter your wallet password --> ')
        while not authenticated:
            try:
                with open('settings.json', 'r') as f:
                    settings = json.load(f)
                salt_bytes = bytes.fromhex(settings['salt'])            
                decrypted_text = crypt.decrypt_string(password, settings['mnemonic'].encode(), salt_bytes)
                authenticated = True
            except Exception:
                password = getpass.getpass(prompt='Nope, try again -> ')
                
            web3.eth.account.enable_unaudited_hdwallet_features()
            wallet = web3.eth.account.from_mnemonic(decrypted_text)

            return wallet

def check_file_type(file_path):
    file_type = mimetypes.guess_type(file_path)[0]

    if file_type not in ["image/png", "image/jpeg", "model/gltf-binary"]:
        raise ValueError("Invalid file type. The file must be in PNG, JPG, or GLB format.")
    return file_type

def get_error_message(tx_hash):
    try:
        trace = web3.provider.make_request("debug_traceTransaction", [tx_hash, {'disableStorage': True, 'disableMemory': True, 'disableStack': True}])
        if trace:
            error_msg = trace['result']['error']
            print(f"The transaction failed with the error: {error_msg}")
        else:
            print("No error message was obtained.")
    except Exception as e:
        print(f"Error occurred while getting the message: {e.args[0]['message']}")
