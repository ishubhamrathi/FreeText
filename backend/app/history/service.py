from history.model import (
    HistoryItem
)

from storage.repository import (
    SessionRepository
)


class HistoryService:

    def __init__(self):

        self.repository = (
            SessionRepository()
        )

    def get_recent(
        self,
        limit: int = 20
    ):

        cursor = (
            self.repository
            .db
            .connection
            .cursor()
        )

        cursor.execute(
            """
            SELECT
                id,
                started_at,
                cleaned_text
            FROM sessions
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = cursor.fetchall()

        result = []

        for row in rows:

            result.append(
                HistoryItem(
                    session_id=row[0],
                    started_at=row[1],
                    cleaned_text=row[2]
                )
            )

        return result