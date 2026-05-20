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

print(
    manager.process(
        "meeting",
        """
        Action item:
        fix api issue

        Decision:
        use local model

        Follow up:
        review tomorrow
        """
    )
)