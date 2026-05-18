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
                    provider
                )
                VALUES(
                    ?,?,?,?,?,?,?,?
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
                    session.provider
                )
            )

            self.db.connection.commit()