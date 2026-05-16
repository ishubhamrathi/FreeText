from audio.recorder import record_audio

def main():
    print("FreeText started")
    input("Press Enter to start recording...")
    audio_file = record_audio()
    print(f"Audio recorded and saved to: {audio_file}")


if __name__ == "__main__":
    main()