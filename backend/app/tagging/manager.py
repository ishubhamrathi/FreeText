from tagging.provider_router import (
    TagProviderRouter
)


class TagManager:

    def __init__(self):

        self.router = (
            TagProviderRouter()
        )

    def generate(
        self,
        text,
        provider="rule",
        language="auto"
    ):

        tagger = (
            self.router
            .get_provider(
                provider
            )
        )

        return tagger.generate(
            text=text,
            language=language
        )