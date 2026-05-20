from dataclasses import dataclass


@dataclass
class ContextState:

    mode: str = "default"

    language: str = "auto"

    last_text: str = ""

    session_text: str = ""

    tags: list[str] | None = None