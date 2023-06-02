import fluidsynth

# Create a FluidSynth synthesizer object
fs = fluidsynth.Synth()

# Load the SoundFont file (piano sound)
sfid = fs.sfload("path/to/piano_soundfont.sf2")

# Set the SoundFont for the synthesizer
fs.program_select(0, sfid, 0, 0)

# Set the output audio driver (optional)
# fs.start(driver="pulseaudio")

# Define the C major scale frequencies
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

# Set the duration of each note in seconds
duration = 1.0

# Play the C major scale
for frequency in frequencies:
    # Create a MIDI note event with the specified frequency
    note = int(round(69 + 12 * math.log2(frequency / 440.0)))

    # Start the note
    fs.noteon(0, note, 127)

    # Sleep for the duration of the note
    time.sleep(duration)

    # Stop the note
    fs.noteoff(0, note)

# Cleanup and close the synthesizer
fs.delete()
