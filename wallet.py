from web3 import Web3

# Connect to a local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Generate a new HD wallet
mnemonic = w3.eth.account.create().mnemonic

# Derive the private key and address from the mnemonic
private_key = w3.eth.account.from_mnemonic(mnemonic).privateKey
address = w3.eth.account.from_mnemonic(mnemonic).address

# Sign a sample transaction
transaction = {
    'nonce': w3.eth.getTransactionCount(address),
    'to': '0x1234567890123456789012345678901234567890',  # Replace with the recipient's address
    'value': w3.toWei(1, 'ether'),  # Replace with the desired value
    'gas': 21000,
    'gasPrice': w3.eth.gas_price,
    'chainId': w3.eth.chain_id,
}
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

# Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print("Transaction sent. Hash:", tx_hash.hex())
