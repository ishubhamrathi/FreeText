from pynput.keyboard import (
    Controller
)


class TypingService:

    def __init__(self):

        self.keyboard = (
            Controller()
        )

    def type_text(
        self,
        text: str
    ):

        if not text.strip():
            return

        self.keyboard.type(
            text + " "
        )