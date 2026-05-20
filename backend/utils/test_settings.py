from path_setup import (
    add_app_to_path
)

add_app_to_path()

from settings.manager import (
    SettingsManager
)


manager = (
    SettingsManager()
)

manager.update_provider(
    "languagetool"
)

manager.update_typing_mode(
    "clipboard"
)

print(
    manager.get()
)