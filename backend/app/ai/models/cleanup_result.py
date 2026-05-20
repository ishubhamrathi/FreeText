from dataclasses import dataclass


@dataclass
class CleanupResult:

    text: str

    provider: str

    latency: float = 0.0

    language: str = "auto"