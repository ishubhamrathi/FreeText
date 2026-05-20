import time

from path_setup import (
    add_app_to_path
)

add_app_to_path()

from typing_service.manager import (
    TypingManager
)

from typing_service.mode import (
    TypingMode
)


manager = TypingManager()

manager.set_mode(
    TypingMode.CLIPBOARD
)

print(
    "Click target window"
)

print(
    "Typing in 5 seconds..."
)

time.sleep(
    5
)

manager.type(
    "Hello from FreeText clipboard mode"
)

print(
    "Done"
)