from web3_connect import *
import requests
import json

def ipfs_add():
    metadata = {
        "name": "me",
        "image": "ipfs://image",
        "description": "desc",
        "attributes": [
            {
                "trait_type": "skill",
                "value": "music_composition"
            },
            {
                "trait_type": "skill",
                "value": "python_programming"
            },
            {
                "trait_type": "skill",
                "value": "music_theory"
            },
            {
                "trait_type": "skill",
                "value": "pytheorus"
            },
            {
                "trait_type": "title",
                "value": "student"
            }
        ]
    }

    json_string = json.dumps(metadata)
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "pin": "true",
        "recursive": "true",
        "content": json_string
    }

    infura_url = "https://ipfs.infura.io:5001/api/v0/add"
    # with open('objects.py', 'r') as f:
    #     files = {'file': ('objects.py', f)}
        # response = requests.post(
        #     'https://ipfs.infura.io:5001/api/v0/add',
        #     files=files,
        #     auth=('APIKEY','SECRET'))

    files = {'file': ("File Name", json_string)}
    response = requests.post(
        'https://ipfs.infura.io:5001/api/v0/add',
        files=files,
        auth=(os.getenv('IPFS_API_KEY'), os.getenv('IPFS_SECRET')))
    res_dict = dict(response.json())
    base_url = 'ipfs://'
    cid = res_dict['Hash']
    uri = base_url + cid
    
    return uri

def mint(wallet):
    uri = ipfs_add()
    address, key = wallet.address, wallet.key
    tx = contract.functions.mint(address, uri, uri.replace('ipfs://', ''), 'song_name', 'composer_name').build_transaction({
        'chainId': 5,
        'gas': 400000,
        'nonce': web3.eth.get_transaction_count(address)
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=key)
    raw_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = dict(web3.eth.wait_for_transaction_receipt(web3.to_hex(web3.keccak(signed_tx.rawTransaction))))

    return tx_receipt, raw_tx
