from web3_connect import *
import utilities

def request_approval(wallet, name):
    address, key = wallet.address, wallet.key
    tx = contract.functions.requestApproval(name).build_transaction({
        'chainId': 5,
        'gas': 200000,
        'nonce': web3.eth.get_transaction_count(address)
    })
    gas = web3.eth.estimate_gas(tx)
    print("Gas Estimate:", gas)
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=key)
    raw_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = dict(web3.eth.wait_for_transaction_receipt(web3.to_hex(web3.keccak(signed_tx.rawTransaction))))

    return tx_receipt

def get_owner():
    owner = contract.functions.owner().call()

    return owner

def get_pending_students():
    wallet = utilities.wallet()
    pending_students = contract.functions.getPendingStudents().call({
        'from': wallet.address
    })

    return pending_students

def approve_or_deny_student(index, decision):
    wallet = utilities.wallet()
    tx = contract.functions.approveOrDenyStudent(index, decision).build_transaction({
        'from': wallet.address,
        'chainId': 5,
        'gas': 200000,
        'nonce': web3.eth.get_transaction_count(wallet.address)
    })

    gas = web3.eth.estimate_gas(tx)
    print("Gas Estimate:", gas)
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=wallet.key)
    raw_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = dict(web3.eth.wait_for_transaction_receipt(web3.to_hex(web3.keccak(signed_tx.rawTransaction))))
    if tx_receipt['status'] != 0:
        print("Success! The student has been accepted.")
    else:
        print("Transaction failed with status 0.")

    return tx_receipt
    
