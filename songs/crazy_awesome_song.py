from . import utilities
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
    