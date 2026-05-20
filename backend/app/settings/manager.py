from settings.models.app_settings import (
    AppSettings
)

from settings.repository import (
    SettingsRepository
)


class SettingsManager:

    def __init__(self):

        self.repository = (
            SettingsRepository()
        )

        self.settings = (
            self.repository.load()
        )

    def get(
        self
    ):

        return self.settings

    def update_provider(
        self,
        provider
    ):

        self.settings.ai_provider = (
            provider
        )

        self.save()

    def update_openai_key(
        self,
        key
    ):

        self.settings.openai_key = key

        self.save()

    def update_gemini_key(
        self,
        key
    ):

        self.settings.gemini_key = key

        self.save()

    def update_typing_mode(
        self,
        mode
    ):

        self.settings.typing_mode = mode

        self.save()

    def save(
        self
    ):

        self.repository.save(
            self.settings
        )