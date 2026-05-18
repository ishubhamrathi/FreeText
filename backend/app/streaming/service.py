import tempfile
import threading
import time
import tempfile
import uuid
from pathlib import Path

from scipy.io.wavfile import write

from config.settings import (
    LIVE_PROCESS_INTERVAL,
    SAMPLE_RATE
)

from streaming.audio_buffer import (
    AudioBuffer
)

from streaming.commit_engine import (
    CommitEngine
)

from streaming.stabilizer import (
    TokenStabilizer
)

from streaming.whisper_stream import (
    WhisperStream
)

from typing_service.service import (
    TypingService
)



class StreamService:


    def __init__(self):

        self.buffer = AudioBuffer()

        self.stream = (
            WhisperStream()
        )

        self.stabilizer = (
            TokenStabilizer()
        )

        self.committer = (
            CommitEngine()
        )

        self.typing_service = (
            TypingService()
        )

        self.running = False

    def append_audio(
        self,
        audio
    ):

        self.buffer.append(
            audio
        )

    def start(self):

        if self.running:
            return

        self.running = True

        self.worker_thread = (
            threading.Thread(
                target=self.worker,
                daemon=True
            )
        )

        self.worker_thread.start()

    def stop(self):

        print(
            "Stopping worker..."
        )

        self.running = False

        if hasattr(
            self,
            "worker_thread"
        ):

            self.worker_thread.join(
                timeout=2
            )

        print(
            "Worker stopped"
        )

    def worker(self):

        while self.running:

            try:

                if not self.buffer.ready():

                    time.sleep(1)

                    continue

                chunk = (
                    self.buffer
                    .get_chunk()
                )

                chunk = chunk.reshape(
                    -1,
                    1
                )

                chunk_id = uuid.uuid4()

                tmp_path = (
                    Path(
                        tempfile.gettempdir()
                    )
                    / f"freetext_{chunk_id}.wav"
                )

                write(
                    str(tmp_path),
                    SAMPLE_RATE,
                    chunk
                )

                print(
                    f"Saved temp: "
                    f"{tmp_path}"
                )

                tokens = (
                    self.stream.transcribe(
                        str(tmp_path)
                    )
                )

                stable = (
                    self.stabilizer.update(
                        tokens
                    )
                )

                committed = (
                    self.committer.commit(
                        sorted(
                            tokens,
                            key=lambda x: x.start
                        )
                    )
                )

                if committed:

                    print(
                        f"LIVE: "
                        f"{committed}"
                    )

                    self.typing_service.type_text(
                        committed + " "
                    )

                try:

                    tmp_path.unlink(
                        missing_ok=True
                    )

                except Exception:

                    pass

                time.sleep(
                    LIVE_PROCESS_INTERVAL
                )

            except Exception as ex:

                print(
                    f"Streaming error: "
                    f"{ex}"
                )

    def flush(
        self
    ):

        tokens = (
            self.stabilizer.flush()
        )

        committed = (
            self.committer.commit(
                sorted(
                    tokens,
                    key=lambda x: x.start
                )
            )
        )

        if committed:

            print(
                f"FINAL: "
                f"{committed}"
            )

            self.typing_service.type_text(
                committed + " "
            )

        self.committer.reset()

    def reset(
        self
    ):

        self.stabilizer.previous = []

        self.committer.reset()