from dataclasses import dataclass


@dataclass
class TranscriptToken:

    text: str

    start: float

    end: float

    committed: bool = False