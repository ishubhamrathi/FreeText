from pynput import keyboard

from audio.recorder import Recorder
from hotkeys.context import HotkeyContext
from config.settings import (
    PUSH_TO_TALK_KEYS
)
from services.pipeline_service import (
    PipelineService
)


class HoldToTalkListener:

    def __init__(self):

        self.context = HotkeyContext()

        self.recorder = Recorder()

        self.pipeline = PipelineService()

    def on_press(
        self,
        key
    ):

        key_name = str(key)

        self.context.press(
            key_name
        )

        if (
            self.context.is_active(
                PUSH_TO_TALK_KEYS
            )
            and self.recorder.state.value
            == "idle"
        ):

            self.recorder.start()

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

        if was_active and not still_active:

            audio = self.recorder.stop()

            if audio:

                result = (
                    self.pipeline.execute_from_audio(
                        audio
                    )
                )

                print(
                    result.text
                )

    def listen(self):

        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:

            listener.join()