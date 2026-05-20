from tagging.providers.base import (
    TagProvider
)


class OpenAiTagProvider(
    TagProvider
):

    def generate(
        self,
        text,
        language="auto"
    ):

        return ""