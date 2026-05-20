from path_setup import (
    add_app_to_path
)

add_app_to_path()

from modes.manager import (
    ModeManager
)


manager = (
    ModeManager()
)

result = manager.process(
    "coding",
    """
    Need to fix API bug

    Refactor spring service

    Deploy backend

    Remember to add tests
    """
)

print(
    result
)