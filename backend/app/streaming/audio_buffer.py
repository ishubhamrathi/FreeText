from collections import deque

import numpy as np
import threading

from config.settings import (
    LIVE_CHUNK_SECONDS,
    SAMPLE_RATE
)


class AudioBuffer:

    def __init__(self):

        self.max_samples = (
            SAMPLE_RATE
            * LIVE_CHUNK_SECONDS
        )

        self.lock = threading.Lock()

        self.buffer = deque(
            maxlen=self.max_samples
        )

    def append(
        self,
        audio
    ):

        flattened = (
            audio.flatten()
        )

        with self.lock:

            self.buffer.extend(
                flattened
            )

        # print(
        #     f"Buffer size: "
        #     f"{len(self.buffer)}"
        # )

    def ready(
        self
    ):

        ready = (
            len(self.buffer)
            >= self.max_samples
        )

        if ready:

            print(
                "Chunk ready"
            )

        return ready

    def get_chunk(
        self
    ):

        with self.lock:

            return np.array(
                list(
                    self.buffer
                ),
                dtype=np.float32
            )