from TTS.api import TTS
import os
from datetime import datetime
import hashlib



tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

class coquiTTS:
    def __init__(self):
        self.max_chars = 2500

    def run(self, text, filepath, random_voice: bool = False):
        # Check if the file already exists
        if os.path.exists(filepath):
            print(f"File already exists: {filepath}")
            return

        # Generate the audio file and save it directly to the given filepath
        tts.tts_to_file(
            text=text,
            file_path=filepath,
            speaker_wav = r"D:\BK dev\Open Source\RedditVideoMakerBot\assets\coqui_sample_voices\sample-voice-2.wav",
            language="en"
        )
        print(f'Audio saved at {filepath}')


            
        