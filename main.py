from record_audio import RecordAudio
from transcribe import TranscribeAudio

def run():
    ra = RecordAudio()
    recording = ra.record()
    ra.write_file(recording)

    ta = TranscribeAudio()
    ta.transcribe()

if __name__ == "__main__":
    run()