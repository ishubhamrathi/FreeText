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

        self.punctuation = (
            SmartPunctuation()
        )

        self.hotword = (
            HotwordManager()
        )

    def process(
        self,
        text
    ):

        lower = text.lower()

        if lower.strip() == "undo":

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
            handled=False,
            mode=mode
        )