from path_setup import add_app_to_path


add_app_to_path()

from history.manager import (
    HistoryManager
)


manager = HistoryManager()

manager.open_history()
