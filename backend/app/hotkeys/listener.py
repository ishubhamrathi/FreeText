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

        self.streaming = False

    def on_press(
        self,
        key
    ):

        key_name = str(key)

        self.context.press(
            key_name
        )

        active = (
            self.context.is_active(
                PUSH_TO_TALK_KEYS
            )
        )

        if (
            active
            and not self.streaming
        ):

            print(
                "Hold detected"
            )

            self.streaming = True

            self.controller.start()

    def on_release(
        self,
        key
    ):

        key_name = str(key)

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

        if (
            was_active
            and not still_active
            and self.streaming
        ):

            print(
                "Released"
            )

            self.streaming = False

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

    def stop(
        self
    ):

        if hasattr(
            self,
            "listener"
        ):

            self.listener.stop()