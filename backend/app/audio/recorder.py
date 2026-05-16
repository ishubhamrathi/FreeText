from datetime import datetime
from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
DURATION = 5

RECORDINGS_DIR = Path("data/recordings")


def generate_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return RECORDINGS_DIR / f"recording_{timestamp}.wav"


def record_audio():
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)

    output_file = generate_filename()

    print("Recording started...")

    audio_data = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(output_file, SAMPLE_RATE, audio_data)

    print(f"Recording saved to: {output_file}")

    return output_file