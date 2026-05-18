from dataclasses import dataclass
from datetime import datetime


@dataclass
class SessionRecord:

    started_at: datetime

    ended_at: datetime

    duration: float

    language: str

    raw_text: str

    cleaned_text: str

    latency: float

    provider: str