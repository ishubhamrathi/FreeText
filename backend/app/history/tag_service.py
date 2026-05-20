from storage.repository import (
    SessionRepository
)


class TagService:

    def __init__(self):

        self.repository = (
            SessionRepository()
        )

    def update_tags(
        self,
        session_id,
        tags
    ):

        cursor = (
            self.repository
            .db
            .connection
            .cursor()
        )

        cursor.execute(
            """
            UPDATE sessions
            SET tags = ?
            WHERE id = ?
            """,
            (
                tags,
                session_id
            )
        )

        self.repository.db.connection.commit()