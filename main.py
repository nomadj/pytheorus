import os
from wallet import *
import menu
from mint import *
from debug import *
import utilities
# from web3_connect import web3_init

load_dotenv()

def main():
    menu.main_menu()

def debug():
    try:
        file_path = 'images/tambora.png'
        file_type = check_file_type(file_path)
        print(f"The file {os.path.basename(file_path)} is of type {file_type}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    # main()
    # debug()
    req_app()
    
    
