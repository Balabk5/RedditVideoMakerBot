from typing import Tuple

from rich.console import Console

from TTS_list.aws_polly import AWSPolly
from TTS_list.elevenlabs import elevenlabs
from TTS_list.engine_wrapper import TTSEngine
from TTS_list.GTTS import GTTS
from TTS_list.pyttsx import pyttsx
from TTS_list.streamlabs_polly import StreamlabsPolly
from TTS_list.TikTok import TikTok
from utils import settings
from utils.console import print_step, print_table
from TTS_list.Coqui import coquiTTS
console = Console()

TTSProviders = {
    "GoogleTranslate": GTTS,
    "AWSPolly": AWSPolly,
    "StreamlabsPolly": StreamlabsPolly,
    "TikTok": TikTok,
    "pyttsx": pyttsx,
    "ElevenLabs": elevenlabs,
    "Coqui": coquiTTS
}


def save_text_to_mp3(reddit_obj) -> Tuple[int, int]:
    """Saves text to MP3 files.

    Args:
        reddit_obj (): Reddit object received from reddit API in reddit/subreddit.py

    Returns:
        tuple[int,int]: (total length of the audio, the number of comments audio was generated for)
    """

    voice = settings.config["settings"]["tts"]["voice_choice"]
    if str(voice).casefold() in map(lambda _: _.casefold(), TTSProviders):
        text_to_mp3 = TTSEngine(get_case_insensitive_key_value(TTSProviders, voice), reddit_obj)
    else:
        while True:
            print_step("Please choose one of the following TTS providers: ")
            print_table(TTSProviders)
            choice = input("\n")
            if choice.casefold() in map(lambda _: _.casefold(), TTSProviders):
                break
            print("Unknown Choice")
        text_to_mp3 = TTSEngine(get_case_insensitive_key_value(TTSProviders, choice), reddit_obj)
    return text_to_mp3.run()


def get_case_insensitive_key_value(input_dict, key):
    return next(
        (value for dict_key, value in input_dict.items() if dict_key.lower() == key.lower()),
        None,
    )
