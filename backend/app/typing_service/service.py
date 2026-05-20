import pyperclip

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

        self.use_clipboard = False

    def enable_clipboard(
        self,
        enabled=True
    ):

        self.use_clipboard = enabled

    def type_text(
        self,
        text
    ):

        if not text:

            return

        if self.use_clipboard:

            self.paste_text(
                text
            )

        else:

            self.keyboard.type(
                text
            )

        self.session_text += text

    def paste_text(
        self,
        text
    ):

        previous = (
            pyperclip.paste()
        )

        pyperclip.copy(
            text
        )

        self.keyboard.press(
            Key.ctrl
        )

        self.keyboard.press(
            "v"
        )

        self.keyboard.release(
            "v"
        )

        self.keyboard.release(
            Key.ctrl
        )

        pyperclip.copy(
            previous
        )

    def rollback(
        self,
        count=None
    ):

        if not self.session_text:

            return

        remove = count

        if remove is None:

            remove = len(
                self.session_text
            )

        remove = min(
            remove,
            len(
                self.session_text
            )
        )

        for _ in range(
            remove
        ):

            self.keyboard.press(
                Key.backspace
            )

            self.keyboard.release(
                Key.backspace
            )

        self.session_text = (
            self.session_text[
                :-remove
            ]
        )

    def rollback_last_word(
        self
    ):

        words = (
            self.session_text
            .rstrip()
            .split()
        )

        if not words:

            return

        remove = (
            len(
                words[-1]
            )
            + 1
        )

        self.rollback(
            remove
        )

    def clear_session(
        self
    ):

        self.session_text = ""