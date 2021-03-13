#!/usr/local/bin/python3

# PyaSynth 

import os
import numpy as np
import simpleaudio as sa
import objects as o
import threading
from time import sleep as rest
import theory as th

ch_f = {'a': 440}
f = ch_f['a']
bpm = 60
T = (1/bpm)*60
sample_rate = 44100

t = np.linspace(0, T, int(T * sample_rate), False)

i = 1

# Populate ch_f dictionary
for element in th.ch_sc:
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
def sine_gen(voice):
    sines = []
    for f in voice:
        sines.append(np.sin(f * t * 2 * np.pi))
    return sines

def voice_one():
    play_sine(th.voice1)
    # rest(T)
    # voices = th.voices()
    # for i in range(0, 4):
    #     play_sine(next(voices))
    f_maj_sc = th.maj_sc('f')
    play_sine(f_maj_sc)

def voice_two():
    play_sine(th.voice2)

def voice_three():
    play_sine(th.voice3)

def voice_four():
    play_sine(th.voice4)

def play_sine(voice):
    audio = np.hstack((sine_gen(freq_gen(voice))))
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def execute():
    _ = os.system("clear")
    thread_dict = {'vc1': voice_one, 'vc2': voice_two,
                   'vc3': voice_three, 'vc4': voice_four}
    for key, val in thread_dict.items():
        key = threading.Thread(target=val)
        key.start()

execute()

# © 2020 Pytheorus at Silicon Lab Chicago
# Copyleft 2020
