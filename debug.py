from contract_methods import *
from utilities import *

def req_app():
    wallio = wallet()
    receipt = request_approval(wallio, "Bob")
    owner = get_owner()
    if receipt['status'] == 0:
        print("Something went wrong")
        get_error_message(receipt['transactionHash'])    
    else:
        print(f"Success! Waiting for approval from contract owner at {owner}")            
    



