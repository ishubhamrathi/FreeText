from commands.capitalization import (
    SmartCapitalization
)

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

        self.capitalization = (
            SmartCapitalization()
        )

    def process(
        self,
        text
    ):

        lower = (
            text
            .lower()
            .strip()
        )

        if lower == "undo":

            return CommandResult(
                text="",
                handled=True,
                undo=True
            )

        if lower == "new paragraph":

            return CommandResult(
                text="\n\n",
                handled=True,
                new_paragraph=True
            )

        mode = (
            self.hotword.process(
                text
            )
        )

        text = (
            self.punctuation.process(
                text
            )
        )

        text = (
            self.capitalization.process(
                text
            )
        )

        return CommandResult(
            text=text,
            mode=mode
        )