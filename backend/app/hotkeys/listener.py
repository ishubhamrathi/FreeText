from pynput import keyboard

from config.settings import (
    PUSH_TO_TALK_KEYS
)

from hotkeys.context import (
    HotkeyContext
)

from hotkeys.live_controller import (
    LiveController
)

class HoldToTalkListener:

    def __init__(self):

        self.context = (
            HotkeyContext()
        )

        self.controller = (
            LiveController()
        )

    def on_press(
        self,
        key
    ):

        key_name = str(key)

        self.context.press(
            key_name
        )

        if self.context.is_active(
            PUSH_TO_TALK_KEYS
        ):

            self.controller.start()

    def on_release(
        self,
        key
    ):

        key_name = str(key)

        self.context.release(
            key_name
        )
        was_active = (
            self.context.is_active(
                PUSH_TO_TALK_KEYS
            )
        )

        self.context.release(
            key_name
        )

        still_active = (
            self.context.is_active(
                PUSH_TO_TALK_KEYS
            )
        )

        if was_active and not still_active:

            self.controller.stop()

    def listen(
        self
    ):

        self.listener = (
            keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
            )
        )

        self.listener.start()

        return self.listener


    def stop(
        self
    ):

        if hasattr(
            self,
            "listener"
        ):

            self.listener.stop()