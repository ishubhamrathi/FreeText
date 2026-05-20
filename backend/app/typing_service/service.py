from pynput.keyboard import (
    Controller
)

from pynput.keyboard import (
    Key
)


class TypingService:

    def __init__(self):

        self.keyboard = (
            Controller()
        )

    def type_text(
        self,
        text
    ):

        if not text:

            return

        self.keyboard.type(
            text
        )

    def undo_last_word(
        self
    ):

        for _ in range(15):

            self.keyboard.press(
                Key.backspace
            )

            self.keyboard.release(
                Key.backspace
            )