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

        self.session_text = ""

    def type_text(
        self,
        text
    ):

        if not text:

            return

        self.keyboard.type(
            text
        )

        self.session_text += text

    def rollback(
        self,
        count=None
    ):

        if not self.session_text:

            return

        rollback_count = count

        if rollback_count is None:

            rollback_count = len(
                self.session_text
            )

        rollback_count = min(
            rollback_count,
            len(
                self.session_text
            )
        )

        for _ in range(
            rollback_count
        ):

            self.keyboard.press(
                Key.backspace
            )

            self.keyboard.release(
                Key.backspace
            )

        self.session_text = (
            self.session_text[
                :-rollback_count
            ]
        )

    def rollback_last_word(
        self
    ):

        if not self.session_text:

            return

        words = (
            self.session_text
            .rstrip()
            .split()
        )

        if not words:

            return

        last = words[-1]

        remove_count = (
            len(last)
            + 1
        )

        self.rollback(
            remove_count
        )

    def clear_session(
        self
    ):

        self.session_text = ""