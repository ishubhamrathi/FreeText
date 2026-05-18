import pyperclip

from storage.repository import (
    SessionRepository
)

class ReplayService:

    def __init__(self):

        self.repository = (
            SessionRepository()
        )

    def replay(
        self,
        session_id: int
    ):

        row = (
            self.repository.get_by_id(
                session_id
            )
        )

        if row is None:

            print(
                "Session not found"
            )

            return

        text = row[1]

        print(
            "\n=== REPLAY ==="
        )

        print(
            text
        )

        return text

    def copy(
        self,
        session_id: int
    ):

        text = self.replay(
            session_id
        )

        if text:

            pyperclip.copy(
                text
            )

            print(
                "Copied to clipboard"
            )