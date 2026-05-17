import keyboard

from config.settings import (
    PUSH_TO_TALK_KEY
)


class HotkeyService:

    def register(
        self,
        callback
    ):
        keyboard.add_hotkey(
            PUSH_TO_TALK_KEY,
            callback
        )

    def listen(self):

        print(
            f"Listening on "
            f"{PUSH_TO_TALK_KEY}"
        )

        keyboard.wait()