from history.viewer import (
    HistoryViewer
)


class HistoryManager:

    def __init__(self):

        self.viewer = (
            HistoryViewer()
        )

    def open_history(self):

        self.viewer.show_recent()