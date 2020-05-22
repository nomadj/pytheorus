#!/usr/local/bin/python3

# PyaSynth 

import os
import numpy as np
import simpleaudio as sa
import object as o
import threading
from time import sleep

ch_sc = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
ch = ch_sc.copy()
ch_f = {'a': 440}
f = ch_f['a']
bpm = 80
T = (1/bpm)*60
n_val = {'q': bpm/T}
sample_rate = 44100

t = np.linspace(0, T, int(T * sample_rate), False)



#for e in tOld:
  #  if tOld.index(e) < len(tOld / 2):
    #    t[e] = 0

pitches = ['a', 'c#', 'e', 'c#']



voice1 = ['e', 'f', 'g', 'a', 'b', 'c', 'd']
voice2 = ['c', 'c', 'g', 'g']
voice3 = ['e', 'e', 'b', 'b']
voice4 = ['g', 'g', 'd', 'd']

i = 1

# Populate ch_f dictionary
for element in ch_sc:
    if element != 'a':
        ch_f[element] = f*2**(i/12)
        i += 1

# Voices


def voices(voice):
    v1 = []
    for note in voice:
        v1.append(ch_f[note])
    return v1

# Modulate to desired key


def mod(key):
    for element in ch_sc:
        if element != key:
            ch.remove(element)
            ch.append(element)
        else:
            break


mod('b')


def ff(index):
    freq = f*2**(index/12)
    return freq

# generate sine wave ]voice


def sine_gen(voice):
    sines = []
    for f in voice:
        sines.append(np.sin(f * t * 2 * np.pi))
    return sines


def play_sine(voice):
    audio = np.hstack((sine_gen(voices(voice))))
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()


def voice_one():
    play_sine(voice1)


def voice_two():
    play_sine(voice2)


def voice_three():
    #bpm /= 2
    play_sine(voice3)


def voice_four():
    #bpm /= 2
    play_sine(voice4)

# def threads(voices):
#     for voice in voices:
#         play_sine(voice)


def execute():
    _ = os.system("clear")
    thread_dict = {'vc1': voice_one, 'vc2': voice_two,
                   'vc3': voice_three, 'vc4': voice_four}
    for key, val in thread_dict.items():
        key = threading.Thread(target=val)
        key.start()


execute()

newNote = o.Note('c', '2')




# © 2020 Pytheorus at Silicon Lab Chicago
# Copyleft 2020
