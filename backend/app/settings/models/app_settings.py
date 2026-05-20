from dataclasses import dataclass


@dataclass
class AppSettings:

    ai_provider: str = "local"

    language: str = "auto"

    typing_mode: str = "direct"

    fallback_enabled: bool = True

    continuous_mode: bool = False

    wake_phrase_enabled: bool = False

    openai_key: str = ""

    gemini_key: str = ""