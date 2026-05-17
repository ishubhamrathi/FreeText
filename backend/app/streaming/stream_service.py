import threading
import time

from streaming.audio_buffer import (
    AudioBuffer
)

from streaming.overlap_resolver import (
    OverlapResolver
)


class StreamService:

    def __init__(
        self,
        pipeline
    ):

        self.pipeline = pipeline

        self.buffer = AudioBuffer()

        self.resolver = (
            OverlapResolver()
        )

        self.running = False

    def start(self):

        self.running = True

        threading.Thread(
            target=self.worker,
            daemon=True
        ).start()

    def stop(self):

        self.running = False

    def worker(self):

        while self.running:

            chunk = (
                self.buffer
                .get_chunk()
            )

            if len(chunk) == 0:

                time.sleep(1)

                continue

            result = (
                self.pipeline
                .execute_chunk(
                    chunk
                )
            )

            merged = (
                self.resolver
                .merge(
                    result.text
                )
            )

            if merged:

                print(
                    merged
                )

            time.sleep(3)