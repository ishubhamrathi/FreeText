from storage.database import (
    Database
)

from storage.models.session import (
    SessionRecord
)


class SessionRepository:

    def __init__(self):

        self.db = Database()

    def save(
        self,
        session: SessionRecord
    ):

        with self.db.lock:

            cursor = (
                self.db.connection.cursor()
            )

            cursor.execute(
                """
                INSERT INTO sessions(

                    started_at,

                    ended_at,

                    duration,

                    language,

                    raw_text,

                    cleaned_text,

                    latency,

                    provider,

                    tags
                )
                VALUES(
                    ?,?,?,?,?,?,?,?,?
                )
                """,
                (
                    session.started_at,

                    session.ended_at,

                    session.duration,

                    session.language,

                    session.raw_text,

                    session.cleaned_text,

                    session.latency,

                    session.provider,

                    session.tags
                )
            )

            self.db.connection.commit()

    def get_by_id(
        self,
        session_id: int
    ):

        with self.db.lock:

            cursor = (
                self.db.connection.cursor()
            )

            cursor.execute(
                """
                SELECT
                    id,
                    cleaned_text
                FROM sessions
                WHERE id = ?
                """,
                (
                    session_id,
                )
            )

            return cursor.fetchone()