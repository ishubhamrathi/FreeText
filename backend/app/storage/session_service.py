from datetime import datetime

from storage.models.session import (
    SessionRecord
)

from storage.repository import (
    SessionRepository
)

from tagging.manager import (
    TagManager
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
        
        self.tag_manager = (
            TagManager()
        )

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

        cleaned = " ".join(
            self.cleaned_parts
        )

        tags = (
            self.tag_manager.generate(
                cleaned
            )
        )

        record = SessionRecord(

            started_at=self.started_at,

            ended_at=ended_at,

            duration=duration,

            language=self.language,

            raw_text=" ".join(
                self.raw_parts
            ),

            cleaned_text=cleaned,

            latency=self.latency,

            provider="local",

            tags=tags
        )

        self.repository.save(
            record
        )

        print(
            "[SESSION SAVED]"
        )