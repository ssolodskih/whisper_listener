import os
from tempfile import NamedTemporaryFile

import openai
import speech_recognition as sr
from pydub import AudioSegment
from speech_recognition import AudioData

# Initialize the recognizer
r = sr.Recognizer()

# Assuming you've set your OpenAI API key in your environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to compress audio data to MP3 and return an in-memory file
def compress_to_mp3_and_save(ad: AudioData) -> str:
    # Convert the audio data from speech_recognition AudioData to pydub AudioSegment
    audio_segment = AudioSegment(
        data=ad.get_wav_data(),
        sample_width=ad.sample_width,
        frame_rate=ad.sample_rate,
        channels=1
    )
    with NamedTemporaryFile(delete=False, suffix='.mp3') as temp_mp3:
        audio_segment.export(temp_mp3.name, format="mp3")
        return temp_mp3.name


# Function to transcribe compressed audio file to text using OpenAI's API
def transcribe_audio(file_path: str):
    response = None
    with open(file_path, 'rb') as audio_file:
        response = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",
        )
    os.remove(file_path)  # Remove the temporary MP3 file
    return response.dict() if response else None


def recognize() -> str:
    # Capture audio from the default microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Please start speaking...")
        # os.system('play --volume=0.1 -nq synth 0.2 sine 300')  # Play a sound to indicate recording has started

        try:
            # Listen for the first phrase and extract it into audio data
            audio_data = r.listen(source)
            print("Processing and transcribing...")

            # Compress to MP3 and save locally
            mp3_file_path = compress_to_mp3_and_save(audio_data)

            # Transcribe the saved MP3 file
            transcription = transcribe_audio(mp3_file_path)
            print("Transcription: ", transcription)
            return transcription['text'] if 'text' in transcription else ''
        except Exception as e:
            print(f"An error occurred: {e}")
            return ''
