import aubio
import numpy as num
import pyaudio
import wave
import cocos

CHUNK=1024
# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=CHUNK)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", CHUNK*2,
    CHUNK, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

while True:

    data = stream.read(CHUNK)
    samples = num.fromstring(data,
        dtype=aubio.float_type)
    pitch = pDetection(samples)[0]
    # Compute the energy (volume) of the
    # current frame.
    volume = num.sum(samples**2)/len(samples)
    # Format the volume output so that at most
    # it has six decimal numbers.
    volume = "{:.6f}".format(volume)

    print(pitch)
    print(volume)
