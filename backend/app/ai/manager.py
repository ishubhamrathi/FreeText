from ai.router import (
    AiRouter
)

from settings.manager import (
    SettingsManager
)


class AiManager:

    def __init__(self):

        self.router = (
            AiRouter()
        )

        self.settings = (
            SettingsManager()
        )

    def cleanup(
        self,
        text,
        provider=None,
        language="auto"
    ):

        active = provider

        if active is None:

            active = (
                self.settings
                .get()
                .ai_provider
            )

        engine = (
            self.router
            .get_provider(
                active
            )
        )

        return engine.process(
            text=text,
            language=language
        )