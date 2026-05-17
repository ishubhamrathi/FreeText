from collections import deque

import numpy as np

from config.settings import (
    SAMPLE_RATE,
    LIVE_CHUNK_SECONDS
)


class AudioBuffer:

    def __init__(self):

        self.max_samples = (
            SAMPLE_RATE
            * LIVE_CHUNK_SECONDS
        )

        self.buffer = deque(
            maxlen=self.max_samples
        )

    def append(
        self,
        audio
    ):

        self.buffer.extend(
            audio.flatten()
        )

    def get_chunk(self):

        return np.array(
            self.buffer
        )