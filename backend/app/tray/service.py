import threading

from PIL import Image
from PIL import ImageDraw

import pystray


class TrayService:

    def __init__(
        self,
        shutdown_callback
    ):

        self.shutdown_callback = (
            shutdown_callback
        )

        self.icon = None

    def create_icon(
        self
    ):

        image = Image.new(
            "RGB",
            (64, 64),
            "white"
        )

        draw = ImageDraw.Draw(
            image
        )

        draw.rectangle(
            (
                16,
                16,
                48,
                48
            ),
            fill="black"
        )

        return image

    def on_exit(
        self,
        icon,
        item
    ):

        icon.stop()

        self.shutdown_callback()

    def run(
        self
    ):

        menu = pystray.Menu(

            pystray.MenuItem(
                "Exit",
                self.on_exit
            )
        )

        self.icon = pystray.Icon(
            "FreeText",
            self.create_icon(),
            "FreeText",
            menu
        )

        threading.Thread(
            target=self.icon.run,
            daemon=True
        ).start()

    def stop(
        self
    ):

        if self.icon:

            self.icon.stop()