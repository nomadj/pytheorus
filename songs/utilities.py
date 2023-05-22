import pickle
import numpy as np
import simpleaudio as sa

def execute():
    new_val = input("Enter new value: ")
    save(new_val)

# def boots():
#     f = open("persistence.py", "rb")
#     try:
#         f.readline().decode("utf-8")
#         boot_data = {1: "red", 2: "blue"}
#         with open("persistence.py", "wb") as f:
#             pickle.dump(boot_data, f)
#             f.close()
#             execute()
#     except(Exception):
#         f.close()
#         execute()

def boots():
    try:
        execute()
    except(Exception):
        print("You're new here, let's try that again.")
        boot_data = [{1: "red", 2: "blue"}, {1: "orange", 2: "yellow"}]
        with open("persistence.py", "wb") as f:
            pickle.dump(boot_data, f)
            f.close()
            execute()
        
def load():
    with open("persistence.py", "rb") as f:
        f.seek(0)
        info = pickle.load(f)
        print(f"Updated info: {info}\n")
        f.close()

def save(val):
    with open("persistence.py", "rb+") as f:
        f.seek(0)
        info = pickle.load(f)
        print("Current info: ", info)
        info[0][1] = val
        f.seek(0)
        f.truncate()
        pickle.dump(info, f)
        f.close()
        load()

ch_f = {'a': 440}
f = ch_f['a']
bpm = 60
T = (1/bpm)*60
sample_rate = 44100

t = np.linspace(0, T, int(T * sample_rate), False)

i = 1

# Populate ch_f dictionary
ch_sc = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
for element in ch_sc:
    if element != 'a':
        ch_f[element] = f*2**(i/12)
        i += 1

# Voices
def freq_gen(voice):
    freqs = []
    for note in voice:
        freqs.append(ch_f[note])
    return freqs

# generate sine wave
def sine_gen(voice, tempo):
    sines = []
    for f in voice:
        sines.append(np.sin(f * tempo * 2 * np.pi))
    return sines

def play_sine(voice, tempo):
    audio = np.hstack((sine_gen(freq_gen(voice), tempo)))
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def tempo(bpm):
    T = (1/bpm)*60
    t = np.linspace(0, T, int(T * sample_rate), False)
    return t    
