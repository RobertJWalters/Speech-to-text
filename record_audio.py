import keyboard
import numpy
import sounddevice
import soundfile
import time
from datetime import datetime

# Recording settings
sample_rate = 44100
channels = 1
block_size = 1024
current_time = datetime.now()
output_filename = current_time.strftime("wav/recording-%d-%m-%y-AT-%H-%M-%f.wav")

print("Press SPACE to record")
keyboard.wait('space')

print("Recording...   Press SPACE to stop")
time.sleep(0.2)

# Start recording
recording = []
with sounddevice.InputStream(
    samplerate=sample_rate,
    channels=channels,
    blocksize=block_size
) as stream:
    stream.start()

    while True:
        data = stream.read(block_size)[0]
        recording.append(data)
        if keyboard.is_pressed('space'):
            break

    stream.stop()
    print("Recording stopped...")

recording_array = numpy.concatenate(recording)

soundfile.write(output_filename, recording_array, sample_rate)
print(f"Recording saved as {output_filename}")



