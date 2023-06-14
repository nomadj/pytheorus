import os
from wallet import *
import menu
from mint import *
from debug import *
import utilities
from contract_methods import *

# from web3_connect import web3_init

load_dotenv()

def main():
    print("Welcome to Pytheorus.")
    web3.default_account = wallet().address
    menu.main_menu()

def debug():
    try:
        file_path = 'images/tambora.png'
        file_type = check_file_type(file_path)
        print(f"The file {os.path.basename(file_path)} is of type {file_type}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
    # debug()
    # req_app()
    # a = get_pending_students()
    # print(a)
    # receipt = approve_or_deny_student(0, True)
    # get_students()
    
    
    
