from dataclasses import dataclass


@dataclass
class TranscriptionResult:
    text: str
    language: str
    processing_time: float
    