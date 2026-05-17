from dataclasses import dataclass


@dataclass
class SegmentResult:

    text: str

    start: float

    end: float


@dataclass
class TranscriptionResult:

    text: str

    language: str

    processing_time: float

    segments: list[SegmentResult]