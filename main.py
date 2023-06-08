import os
# import threading
# import types
# from time import sleep
# import importlib
# from dotenv import load_dotenv
# from web3_connect import *
# import requests
# import json
from wallet import *
import menu
from mint import *

load_dotenv()

def main():
    menu.main_menu()

def debug():
    pass
    # event_filter = contract.events.Transfer.create_filter(fromBlock=0, toBlock='latest')
    # events = event_filter.get_all_entries()
    # print(events)
    # for e in events:
    #     print(e)

### SCRATCH ###

# def execute():
#     definitions = globals()
#     all_functions = [name for name, obj in definitions.items() if isinstance(obj, types.FunctionType)]
#     print(*all_functions)
# def execute():
#     definitions = globals()
#     for definition in definitions.items():
#         if callable(eval(definition[0])):
#             print(definition[0])

if __name__ == "__main__":
    main()
    # debug()
    
