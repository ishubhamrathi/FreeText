from ai.router import (
    AiRouter
)


class AiManager:

    def __init__(self):

        self.router = (
            AiRouter()
        )

    def cleanup(
        self,
        text,
        provider="local",
        language="auto"
    ):

        engine = (
            self.router
            .get_provider(
                provider
            )
        )

        return engine.process(
            text,
            language
        )