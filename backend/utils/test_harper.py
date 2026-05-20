from path_setup import (
    add_app_to_path
)

add_app_to_path()

from ai.fallback_manager import (
    FallbackManager
)


manager = (
    FallbackManager()
)

result = manager.cleanup(
    """
    hello i am buildng freetext
    """
)

print(
    result
)