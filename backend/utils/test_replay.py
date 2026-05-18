from history.manager import (
    HistoryManager
)


manager = HistoryManager()

manager.open_history()

manager.replay_session(
    1
)

manager.copy_session(
    1
)