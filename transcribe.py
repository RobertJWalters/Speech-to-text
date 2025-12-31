import warnings
import whisper
import os

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

whisper_model = whisper.load_model("base")

input_folder = "wav"
output_folder = "txt"

for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        wav_path = os.path.join(input_folder, filename)
        txt_path = os.path.join(output_folder, filename.replace(".wav", ".txt"))
        #Skip files that have already been transcribed
        if os.path.exists(txt_path):
            continue
        
        result = whisper_model.transcribe(wav_path, language="en")

        with open(txt_path, "w", encoding="utf-8") as output_file:
            output_file.write(result["text"])

        print(f"Transcribed: {filename}")