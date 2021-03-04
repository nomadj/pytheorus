#!/usr/local/bin/python3

ch_sc = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
ch = ch_sc.copy()

def mod(key):
    for element in ch_sc:
        if element != key:
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


