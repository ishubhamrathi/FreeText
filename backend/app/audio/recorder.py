from datetime import datetime

import sounddevice as sd
from scipy.io.wavfile import write

from config.settings import (
    SAMPLE_RATE,
    CHANNELS,
    DEFAULT_RECORD_DURATION,
    RECORDINGS_DIR
)


def generate_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return RECORDINGS_DIR / f"recording_{timestamp}.wav"


def record_audio():
    RECORDINGS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = generate_filename()

    print("Recording started...")

    audio_data = sd.rec(
        int(DEFAULT_RECORD_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    write(output_file, SAMPLE_RATE, audio_data)

    print(f"Recording saved to: {output_file}")

    return output_file