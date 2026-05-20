from path_setup import add_app_to_path

add_app_to_path()

from tagging.manager import (
    TagManager
)


manager = TagManager()

print(
    manager.generate(
        """
        Need to fix API bug
        in Spring service
        and deploy later
        """,
        provider="rule"
    )
)