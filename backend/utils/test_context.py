from path_setup import (
    add_app_to_path
)

add_app_to_path()

from context.manager import (
    ContextManager
)


context = (
    ContextManager()
)

context.update(
    "create youtube idea",
    mode="youtube"
)

context.update(
    "add thumbnail concept"
)

print(
    context.get_mode()
)

print(
    context.get_text()
)