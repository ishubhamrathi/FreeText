from audio.recorder import record_audio
from transcription.transcriber import transcribe_audio

def main():
    print("FreeText started")
    input("Press Enter to start recording...")
    audio_file = record_audio()
    print(f"Audio recorded and saved to: {audio_file}")
    transcript = transcribe_audio(audio_file)
    print("Transcription:")
    print(transcript)

if __name__ == "__main__":
    main()