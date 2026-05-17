from datetime import datetime
from pathlib import Path

from audio.state import RecordingState
from config.settings import (
    SAMPLE_RATE,
    CHANNELS,
    RECORDINGS_DIR,
    DEFAULT_RECORD_DURATION
)


class Recorder:

    def __init__(self):

        self.state = RecordingState.IDLE

        self.frames = []

        self.stream = None

    def generate_filename(self):

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )

        return (
            RECORDINGS_DIR
            / f"recording_{timestamp}.wav"
        )

    def callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        if self.state != RecordingState.RECORDING:
            return

        self.frames.append(
            indata.copy()
        )

    def start(self):

        if self.state == RecordingState.RECORDING:
            return

        RECORDINGS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        self.frames = []

        self.state = RecordingState.RECORDING

        import sounddevice as sd

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            callback=self.callback
        )

        self.stream.start()

        print("Recording started")

    def stop(self):

        if self.state != RecordingState.RECORDING:
            return None

        self.state = RecordingState.IDLE

        self.stream.stop()

        self.stream.close()

        output_file = (
            self.generate_filename()
        )

        import numpy as np
        from scipy.io.wavfile import write

        audio = np.concatenate(
            self.frames,
            axis=0
        )

        write(
            output_file,
            SAMPLE_RATE,
            audio
        )

        print(
            f"Saved: {output_file}"
        )

        return output_file


def record_audio():
    """Convenience function for synchronous recording used by the pipeline.

    Records for `DEFAULT_RECORD_DURATION` seconds and writes a WAV file.
    Returns the output file path.
    """
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = RECORDINGS_DIR / f"recording_{timestamp}.wav"

    print("Recording started...")

    import sounddevice as sd
    from scipy.io.wavfile import write

    audio = sd.rec(
        int(DEFAULT_RECORD_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    write(output_file, SAMPLE_RATE, audio)

    print(f"Recording saved to: {output_file}")

    return output_file