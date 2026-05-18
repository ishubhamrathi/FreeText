from debug_ui.overlay import (
    OverlayWindow
)

from debug_ui.state import (
    OverlayState
)


class DebugUiService:

    def __init__(self):

        self.overlay = (
            OverlayWindow()
        )

        self.state = (
            OverlayState()
        )

    def publish(
        self,
        **kwargs
    ):

        for key, value in kwargs.items():

            setattr(
                self.state,
                key,
                value
            )

        self.overlay.update(
            self.state
        )