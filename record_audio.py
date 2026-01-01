import keyboard
import numpy
import sounddevice
import soundfile
import time
from datetime import datetime

class RecordAudio:

    def __init__(self):
        # Recording settings
        self.SAMPLE_RATE = 44100
        self.CHANNELS = 1
        self.BLOCK_SIZE = 1024

    def record(self):
        print("Press SPACE to record")
        keyboard.wait('space')
        print("Recording...   Press SPACE to stop")
        # Debounce for 0.2 seconds
        time.sleep(0.2)

        # Start recording
        recording = []
        with sounddevice.InputStream(
            samplerate=self.SAMPLE_RATE,
            channels=self.CHANNELS,
            blocksize=self.BLOCK_SIZE
        ) as stream:
            stream.start()

            while True:
                data = stream.read(self.BLOCK_SIZE)[0]
                recording.append(data)
                if keyboard.is_pressed('space'):
                    break
            stream.stop()
            print("Recording stopped...")

        return numpy.concatenate(recording)

    def write_file(self, recording):
        output_filename = self.get_output_filename()
        soundfile.write(output_filename, recording, self.SAMPLE_RATE)
        print(f"Recording saved as {output_filename}")

    def get_output_filename(self):
        current_time = datetime.now()
        return current_time.strftime("wav/recording-%d-%m-%y-AT-%H-%M-%f.wav")
