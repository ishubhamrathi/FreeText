import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
DURATION = 5


def record_audio(output_file="output.wav"):
    print("Recording started...")

    audio_data = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(output_file, SAMPLE_RATE, audio_data)

    print(f"Recording saved to {output_file}")