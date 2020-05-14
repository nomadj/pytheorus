#!/usr/local/bin/python3


class Measure:
    def __init__(self, voices):
        self.voices = voices


class Voice:
    def __init__(self, notes):
        self.notes = notes


class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration
