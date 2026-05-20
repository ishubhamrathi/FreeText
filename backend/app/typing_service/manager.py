from typing_service.mode import (
    TypingMode
)

from typing_service.service import (
    TypingService
)


class TypingManager:

    def __init__(self):

        self.service = (
            TypingService()
        )

        self.mode = (
            TypingMode.DIRECT
        )

    def set_mode(
        self,
        mode
    ):

        self.mode = mode

        self.service.enable_clipboard(
            mode
            ==
            TypingMode.CLIPBOARD
        )

    def type(
        self,
        text
    ):

        self.service.type_text(
            text
        )

    def undo_word(
        self
    ):

        self.service.rollback_last_word()