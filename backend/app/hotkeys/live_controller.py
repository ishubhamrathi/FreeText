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

        if self.active:
            return

        print(
            "Streaming started"
        )

        self.input.start()

        self.streaming.start()

        self.active = True


    def stop(self):

        if not self.active:
            return

        print(
            "Streaming stopped"
        )

        self.streaming.stop()

        self.input.stop()

        self.active = False