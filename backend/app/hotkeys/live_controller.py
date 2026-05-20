from streaming.service import (
    StreamService
)

from streaming.input import (
    StreamingInput
)

from commands.command_processor import (
    CommandProcessor
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

        self.commands = (
            CommandProcessor()
        )

    def start(self):

        if self.active:
            return

        self.streaming.reset()

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

        self.streaming.flush()

        self.input.stop()

        self.active = False

    def process_text(
        self,
        text
    ):

        result = (
            self.commands.process(
                text
            )
        )

        if result.undo:

            self.typing.rollback_last_word()

            return

        self.typing.type_text(
            result.text
        )