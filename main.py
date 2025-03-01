from synthesis import generate_sine_wave

wave = generate_sine_wave(440, 1) #440 Hz for 1 second
print(wave[:10]) #print first 10 samples to check if it works