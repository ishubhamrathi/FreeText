from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class HarperProvider(
    AiProvider
):

    def process(
        self,
        text,
        language="auto"
    ):

        return CleanupResult(
            text=text,
            provider="harper",
            language=language
        )