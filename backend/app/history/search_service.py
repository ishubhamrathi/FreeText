from history.model import (
    HistoryItem
)

from storage.repository import (
    SessionRepository
)


class SearchService:

    def __init__(self):

        self.repository = (
            SessionRepository()
        )

    def search(
        self,
        query: str
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
            WHERE cleaned_text
            LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{query}%",
            )
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