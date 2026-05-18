from datetime import datetime

from storage.models.session import (
    SessionRecord
)

from storage.repository import (
    SessionRepository
)

class SessionService:

    def __init__(self):

        self.repository = (
            SessionRepository()
        )

        self.started_at = None

        self.raw_parts = []

        self.cleaned_parts = []

        self.language = "unknown"

        self.latency = 0.0

    def start_session(
        self
    ):

        self.started_at = (
            datetime.now()
        )

        self.raw_parts = []

        self.cleaned_parts = []

    def add_text(
        self,
        raw_text,
        cleaned_text
    ):

        self.raw_parts.append(
            raw_text
        )

        self.cleaned_parts.append(
            cleaned_text
        )

    def finish(
        self
    ):

        ended_at = (
            datetime.now()
        )

        duration = (
            ended_at
            - self.started_at
        ).total_seconds()

        record = SessionRecord(
            started_at=self.started_at,

            ended_at=ended_at,

            duration=duration,

            language=self.language,

            raw_text=" ".join(
                self.raw_parts
            ),

            cleaned_text=" ".join(
                self.cleaned_parts
            ),

            latency=self.latency,

            provider="local"
        )

        self.repository.save(
            record
        )

        print(
            "[SESSION SAVED]"
        )