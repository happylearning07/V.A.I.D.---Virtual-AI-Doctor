import os
import elevenlabs
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from gtts import gTTS

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# Setup Text to Speech-TTS-model with gTTS 
def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"
    audioobj=gTTS(
        text=input_text,
        lang = language,
        slow= False
    )
    audioobj.save(output_filepath)
    return output_filepath # Return path for Gradio

# Setup Text to Speech-TTS-model with ElevenLabs
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="9BWtsMINqrJLrRacOk9x", #Aria
        output_format="mp3_22050_32",
        model_id="eleven_multilingual_v2" # Changed to Multilingual model for better language support
    )
    save(audio, output_filepath)
    return output_filepath # Return path for Gradio