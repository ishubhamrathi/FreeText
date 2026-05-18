from dataclasses import dataclass


@dataclass
class HistoryItem:

    session_id: int

    started_at: str

    cleaned_text: str