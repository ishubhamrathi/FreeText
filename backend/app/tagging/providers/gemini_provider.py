from tagging.providers.base import (
    TagProvider
)


class GeminiTagProvider(
    TagProvider
):

    def generate(
        self,
        text,
        language="auto"
    ):

        return ""