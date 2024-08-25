from pydub import AudioSegment
import speech_recognition as sr
import os
import tempfile

def transcribe_audio(audio_file_path):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Convert MP3 to WAV
        audio = AudioSegment.from_mp3(audio_file_path)
        wav_file_path = os.path.join(temp_dir, os.path.basename(audio_file_path).replace(".mp3", ".wav"))
        audio.export(wav_file_path, format="wav")

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Split audio into chunks of 60 seconds each
        chunk_length_ms = 60000  # 60 seconds
        audio_chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

        transcription = ""

        for i, chunk in enumerate(audio_chunks):
            chunk_wav_path = os.path.join(temp_dir, f"chunk_{i}.wav")
            chunk.export(chunk_wav_path, format="wav")

            # Transcribe each chunk
            with sr.AudioFile(chunk_wav_path) as source:
                audio_data = recognizer.record(source)

            try:
                chunk_transcription = recognizer.recognize_google(audio_data)
                transcription += chunk_transcription + " "
                print(f"Transcribed chunk {i + 1}/{len(audio_chunks)}")
            except sr.UnknownValueError:
                print(f"Google Speech Recognition could not understand chunk {i + 1}")
            except sr.RequestError as e:
                print(f"Could not request results for chunk {i + 1}; {e}")
                break  # Exit if there's a network error

        return transcription

# Prompt the user for the audio file path
audio_file_path = input("Please enter the path to the audio file: ").strip()  # <-- Added .strip() here

print("Starting transcription process...")
transcription = transcribe_audio(audio_file_path)
print("Transcription: ", transcription)
print("Process completed.")
