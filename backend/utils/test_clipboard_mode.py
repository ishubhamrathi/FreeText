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

input(
    "Focus target and press enter..."
)

manager.type(
    "Hello from FreeText clipboard mode"
)