from tagging.providers.base import (
    TagProvider
)


class LocalAiTagProvider(
    TagProvider
):

    def generate(
        self,
        text,
        language="auto"
    ):

        return ""