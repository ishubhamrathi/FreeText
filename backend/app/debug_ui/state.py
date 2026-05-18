from dataclasses import dataclass


@dataclass
class OverlayState:

    status: str = "IDLE"

    committed: str = ""

    pending: str = ""

    language: str = ""

    latency: float = 0.0

    chunk_number: int = 0