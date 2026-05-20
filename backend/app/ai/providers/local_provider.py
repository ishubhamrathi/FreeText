import time

from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class LocalProvider(
    AiProvider
):

    def process(
        self,
        text,
        language="auto"
    ):

        start = time.time()

        cleaned = (
            text
            .strip()
            .replace(
                " i ",
                " I "
            )
        )

        return CleanupResult(

            text=cleaned,

            provider="local",

            latency=round(
                time.time()
                - start,
                3
            ),

            language=language
        )