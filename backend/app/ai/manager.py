from ai.config import (
    AiConfig
)

from ai.router import (
    AiRouter
)


class AiManager:

    def __init__(self):

        self.router = (
            AiRouter()
        )

        self.config = (
            AiConfig()
        )

    def set_provider(
        self,
        provider
    ):

        self.config.set_provider(
            provider
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
                self.config
                .get_provider()
            )

        engine = (
            self.router
            .get_provider(
                active
            )
        )

        return engine.process(
            text,
            language
        )