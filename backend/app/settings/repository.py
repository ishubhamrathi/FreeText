import json

from pathlib import Path

from settings.models.app_settings import (
    AppSettings
)


class SettingsRepository:

    def __init__(self):

        self.path = Path(
            "settings.json"
        )

    def save(
        self,
        settings: AppSettings
    ):

        data = {

            "ai_provider":
            settings.ai_provider,

            "language":
            settings.language,

            "typing_mode":
            settings.typing_mode,

            "fallback_enabled":
            settings.fallback_enabled,

            "continuous_mode":
            settings.continuous_mode,

            "wake_phrase_enabled":
            settings.wake_phrase_enabled,

            "openai_key":
            settings.openai_key,

            "gemini_key":
            settings.gemini_key
        }

        self.path.write_text(
            json.dumps(
                data,
                indent=4
            ),
            encoding="utf-8"
        )

    def load(
        self
    ):

        if not self.path.exists():

            return AppSettings()

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        return AppSettings(
            **data
        )