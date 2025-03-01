import numpy as np
import simpleaudio as sa

def generate_sine_wave(frequency, duration, sample_rate=44100):


    t = np.linspace(0, duration, int(sample_rate * duration), False)

    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    wave = (wave * 32767).astype(np.int16)

    return wave 