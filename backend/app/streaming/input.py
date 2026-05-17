import sounddevice as sd

from config.settings import (
    CHANNELS,
    SAMPLE_RATE
)


class StreamingInput:

    def __init__(
        self,
        service
    ):

        self.service = service

        self.stream = None

    def callback(
        self,
        indata,
        frames,
        time_info,
        status
    ):

        self.service.append_audio(
            indata
        )

    def start(
        self
    ):

        if self.stream is not None:
            return

        self.stream = (
            sd.InputStream(
                samplerate=SAMPLE_RATE,
                channels=CHANNELS,
                callback=self.callback
            )
        )

        self.stream.start()

        print(
            "Audio stream started"
        )
    
    def stop(
        self
    ):

        if self.stream is None:
            return

        try:

            self.stream.stop()

            self.stream.close()

        finally:

            self.stream = None