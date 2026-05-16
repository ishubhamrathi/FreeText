from audio.recorder import record_audio

from transcription.transcriber import (
    transcribe_audio
)


def main():
    input("Press Enter to start recording...")

    audio_file = record_audio()

    print("\nTranscribing audio...\n")

    result = transcribe_audio(audio_file)

    print("=" * 50)

    print(f"Detected Language : {result.language}")

    print(
        f"Processing Time  : "
        f"{result.processing_time}s"
    )

    print("\nTranscript:\n")

    print(result.text)

    print("=" * 50)


if __name__ == "__main__":
    main()