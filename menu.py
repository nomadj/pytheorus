from web3_connect import *
import os
import threading
import types
from time import sleep
import importlib
from mint import mint

def clear():
    os.system('clear')

def main_menu():
    clear()
    menu_options = ["1. Create a new song", "2. Edit an existing song", "3. Play a song", "4. Delete a song", "5. Mint an NFT", "6. Exit"]
    menu_actions = {"1": create_song, "2": edit_song, "3": play_song, "4": delete_song, "5": mint_song, "6": exit_program}    
    connection = web3.is_connected()
    contract_name = contract.functions.name().call()
    if connection:
        print(f"Hello. Welcome to PyaSynth. You are connected to the {contract_name} contract.\nChoose from the options below.\n")
    else:
        print("Hello. Welcome to PyaSynth. You are not connected to an Ethereum node.\nChoose from the options below.\n")
    for option in menu_options:
        print(option)
    prompt = input("\n--> ")
    while prompt not in menu_actions.keys():
        prompt = input("Invalid response. Type the number of an action\n--> ")
    menu_actions[prompt]()

def create_song():
    clear()
    special_chars = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]
    special_chars.remove('_')
    special_chars.append(' ')
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    i = len(songs) + 1
    song_name = input("What is the name of your song? Hit enter to go back.\n--> ")
    while song_name in songs or any(character in song_name for character in special_chars):
        if song_name in songs:
            song_name = input("Song exists. Try again.\n--> ")
        elif any(character in song_name for character in special_chars):
            song_name = input("Alphanumeric and underscore only. No spaces. Try again.\n--> ")
    if song_name == "":
        main_menu()
        return
    song_path = "songs/" + song_name.strip() + ".py"
    code = """from . import utilities
import threading
    
start_event = threading.Event()
    
def voice_one():
    start_event.wait()
    melody = ['c', 'd', 'e', 'f', 'g']
    utilities.play_sine(melody, utilities.tempo(60))

def voice_two():
    start_event.wait()
    melody = ['e', 'f', 'g', 'a', 'b']
    utilities.play_sine(melody, utilities.tempo(60))

voices = [voice_one, voice_two]
    """
    with open(song_path, 'w') as f:
        f.write(code)
        f.close()

    os.system(f'nano {song_path}')
    main_menu()

def edit_song():
    clear()
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}    
    print("Which song would you like to edit? Hit enter to go back.\n")
    for index, song in songs.items():
        print(f"{index}. {song}")        
    song_name = input("\n--> ")
    if song_name == "":
        main_menu()
        return
    while song_name not in songs.keys():
        song_name = input("That song does not exist. Type the number of the song\n--> ")
        if song_name == "":
            main_menu()
            return
    os.system(f'nano songs/{songs[song_name]}.py')
    main_menu()

def play_song():
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}

    clear()
    print("Which song would you like to play? Hit enter to go back.\n")
    for index, song in songs.items():
        print(f"{index}. {song}")
    prompt = input("\n--> ")
    if prompt == '':
        main_menu()
        return
    while prompt not in songs.keys():
        prompt = input("Try again. Type the number of the song to be played --> ")
        if prompt == '':
            main_menu()
            return
    songs_package = 'songs'
    song = importlib.import_module("." + songs[prompt], package=songs_package)
    voices = song.voices
    for voice in voices:
        thread = threading.Thread(target=voice)
        thread.start()
    song.start_event.set()
    for voice in voices:
        thread.join()
    main_menu()

def delete_song():
    clear()
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}    
    print("Which song would you like to delete? Hit enter to go back.\n")
    for index, song in songs.items():
        print(f"{index}. {song}")        
    song_name = input("\n--> ")
    if song_name == "":
        main_menu()
        return
    while song_name not in songs.keys():
        song_name = input("That song does not exist. Enter the number of the song.\n--> ")
        if song_name == "":
            main_menu()
            return
    safeguard = input(f"Are you sure you want to delete {songs[song_name]}? Type yes to delete.\n--> ")
    if safeguard.lower() == 'yes':
        os.system(f'rm songs/{songs[song_name]}.py')
        clear()
        print(songs[song_name] + " deleted.")
        sleep(2)
        delete_song()
    else:
        delete_song()

def mint_song():
    os.system('clear')
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
        print('Welcome back!\n')
        songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
        songs = {str(i): song for i, song in enumerate(songs, start=1)}
        print("Which song would you like to mint? Hit enter to go back.\n")
        for index, song in songs.items():
            print(f"{index}. {song}")        
        song_name = input("\n--> ")
        if song_name == "":
            main_menu()
            return
        while song_name not in songs.keys():
            song_name = input("That song does not exist. Enter the number of the song.\n--> ")
            if song_name == "":
                main_menu()
                return
        safeguard = input(f"Are you sure you want to mint {songs[song_name]}? Input 'yes' to mint.\n--> ")
        if safeguard.lower() == 'yes':
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
            public_key = wallet.address
            balance = web3.from_wei(web3.eth.get_balance(public_key), 'ether')
            os.system('clear')
            clear()
            print("Wallet address:", public_key)
            print("Balance:", balance)
            print("\nMinting", songs[song_name])
            receipt = mint(wallet)
            tx_hash = web3.to_hex(receipt[0]['transactionHash'])
            block = receipt[0]['blockNumber']
            print(f"\nSuccess! {songs[song_name]} has been minted \nBlock: {block}\nTransaction hash: {tx_hash}\n")
            prompt = input("Would you like to mint another? Input 'yes' or 'no'\n--> ")
            while prompt not in ['yes', 'no']:
                prompt = input("Try again. Type 'yes' or 'no' then hit enter\n--> ")
            mint_song() if prompt == 'yes' else main_menu()
        else:
            mint_song()

def exit_program():
    clear()
    print("Goodbye!")
    sleep(2)
    clear()    
