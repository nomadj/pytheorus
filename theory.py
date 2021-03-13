#!/usr/local/bin/python3

from time import sleep

bpm = 60
T = (1/bpm)*60

ch_sc = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
ch = ch_sc.copy()

def mod(k):
    for element in ch_sc:
        if element != k:
            ch.remove(element)
            ch.append(element)
        else:
            break

# def ff(index):
#     freq = f*2**(index/12)
#     return freq

voice1 = ['e', 'f#', 'g', 'a', 'b', 'c', 'd#']
voice2 = ['e', 'e', 'b', 'b', 'c', 'f#', 'b']
voice3 = ['b', 'b', 'g', 'g', 'f#', 'a', 'f#']
voice4 = ['g', 'g', 'd', 'd', 'a', 'e', 'a']

all_voices = [voice1, voice2, voice3, voice4]

def voices():
    for voice in all_voices:
        yield voice
        sleep(T)

def maj_sc(k):
    mod(k)
    maj_sc_f = [0, 2, 4, 5, 7, 9, 11]
    scale = []
    for i in maj_sc_f:
        scale.append(ch[i])

    return scale
    
