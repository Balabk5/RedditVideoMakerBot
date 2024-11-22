from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

class coquiTTS:
    def __init__(self):
        self.max_chars = 2500

    def run(self, text, filepath, random_voice: bool = False):
        output_audio_path = r"D:\BK dev\Open Source\RedditVideoMakerBot\assets\temp\1gs924u\mp3\output.wav"

        tts.tts_to_file(
        text= text,
        file_path=output_audio_path,
        speaker_wav=r"D:\BK dev\Open Source\RedditVideoMakerBot\assets\temp\1gs924u\mp3\sample-voice-2.wav",
        language="en"
    )
        print('audio saved')
        
        