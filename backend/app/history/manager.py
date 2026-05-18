from history.viewer import (
    HistoryViewer
)

from history.replay_service import (
    ReplayService
)

from history.viewer import (
    HistoryViewer
)

class HistoryManager:

    def __init__(self):

        self.viewer = (
            HistoryViewer()
        )

        self.replay = (
            ReplayService()
        )

    def open_history(
        self
    ):

        self.viewer.show_recent()

    def replay_session(
        self,
        session_id
    ):

        self.replay.replay(
            session_id
        )

    def copy_session(
        self,
        session_id
    ):

        self.replay.copy(
            session_id
        )