#import pyasynth_exp as pya
import os
import threading
import types
from time import sleep
import importlib
from dotenv import load_dotenv
import web3_connect as w3

load_dotenv()

def clear():
    os.system('clear')

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
        execute()
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
    #os.system(f'nano songs/new_song_{i}.py')
    os.system(f'nano {song_path}')
    execute()

def edit_song():
    clear()
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}    
    print("Which song would you like to edit? Hit enter to go back.\n")
    for index, song in songs.items():
        print(f"{index}. {song}")        
    song_name = input("\n--> ")
    if song_name == "":
        execute()
        return
    while song_name not in songs.keys():
        song_name = input("That song does not exist. Type the number of the song\n--> ")
        if song_name == "":
            execute()
            return
    os.system(f'nano songs/{songs[song_name]}.py')
    execute()

def play_song():
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}

    clear()
    print("Which song would you like to play?\n")
    for index, song in songs.items():
        print(f"{index}. {song}")
    prompt = input("\n--> ")
    while prompt not in songs.keys():
        prompt = input("Try again. Type the number of the song to be played --> ")
    songs_package = 'songs'
    song = importlib.import_module("." + songs[prompt], package=songs_package)
    voices = song.voices
    for voice in voices:
        thread = threading.Thread(target=voice)
        thread.start()
    song.start_event.set()
    for voice in voices:
        thread.join()
    execute()

def delete_song():
    clear()
    songs = [song.removesuffix('.py') for song in os.listdir('songs') if song.removesuffix('.py') not in ['utilities', '__pycache__']]
    songs = {str(i): song for i, song in enumerate(songs, start=1)}    
    print("Which song would you like to delete? Hit enter to go back.\n")
    for index, song in songs.items():
        print(f"{index}. {song}")        
    song_name = input("\n--> ")
    if song_name == "":
        execute()
        return
    while song_name not in songs.keys():
        song_name = input("That song does not exist. Enter the number of the song.\n--> ")
        if song_name == "":
            execute()
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

def exit_program():
    clear()
    print("Goodbye!")
    sleep(2)
    clear()

def execute():
    menu_options = ["1. Create a new song", "2. Edit an existing song", "3. Play a song", "4. Delete a song", "5. Exit"]
    menu_actions = {"1": create_song, "2": edit_song, "3": play_song, "4": delete_song, "5": exit_program}    
    clear()
    print("Hello. Welcome to PyaSynth. Choose from the options below.\n")
    for option in menu_options:
        print(option)
    prompt = input("\n--> ")
    while prompt not in menu_actions.keys():
        prompt = input("Invalid response. Type the number of an action\n--> ")
    menu_actions[prompt]()

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
    execute()
    
