import numpy as np
import simpleaudio as sa

def generate_sine_wave(frequency, duration, sample_rate=44100):


    t = np.linspace(0, duration, int(sample_rate * duration), False)

    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    wave = (wave * 32767).astype(np.int16)

    #play sound
    play_obj = sa.play_buffer(wave, 1, 2, sample_rate)
    play_obj.wait_done() #Wait for playback to finish

    return wave  #Still return the wave if we need it later