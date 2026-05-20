from path_setup import (
    add_app_to_path
)

add_app_to_path()

from ai.manager import (
    AiManager
)


manager = (
    AiManager()
)

manager.set_provider(
    "languagetool"
)

result = manager.cleanup(
    """
    hello i am building freetext
    """
)

print(
    result
)