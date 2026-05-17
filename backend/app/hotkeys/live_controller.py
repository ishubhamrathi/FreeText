from streaming.service import (
    StreamService
)

from streaming.input import (
    StreamingInput
)

class LiveController:

    def __init__(self):

        self.streaming = (
            StreamService()
        )


        self.input = (
            StreamingInput(
                self.streaming
            )
        )

        self.active = False

    def start(self):

        self.input.start()

        self.streaming.start()

        if self.active:
            return

        print(
            "Streaming started"
        )

        self.active = True

        self.streaming.start()

    def stop(
        self
    ):

        if not self.active:
            return

        print(
            "Streaming stopped"
        )

        self.input.stop()

        self.streaming.stop()

        self.active = False