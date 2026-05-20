from commands.hotword import (
    HotwordManager
)

from commands.models.command_result import (
    CommandResult
)

from commands.punctuation import (
    SmartPunctuation
)


class CommandProcessor:

    def __init__(self):

        self.hotword = (
            HotwordManager()
        )

        self.punctuation = (
            SmartPunctuation()
        )

    def process(
        self,
        text
    ):

        lower = text.lower().strip()

        if lower == "undo":

            return CommandResult(
                text="",
                handled=True,
                undo=True
            )

        if lower == "undo word":

            return CommandResult(
                text="",
                handled=True,
                undo=True
            )

        mode = (
            self.hotword.process(
                text
            )
        )

        processed = (
            self.punctuation.process(
                text
            )
        )

        return CommandResult(
            text=processed,
            mode=mode
        )