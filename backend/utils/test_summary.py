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
    "journal",
    """
    Today I worked on FreeText.

    Need to finish local AI support.

    Refactor streaming service.

    Review typing module tomorrow.
    """
)

print(
    result
)