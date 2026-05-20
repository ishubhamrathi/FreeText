import time

from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class HarperProvider(
    AiProvider
):

    def __init__(self):

        self.available = False

        self.engine = None

        try:

            import harper

            self.engine = harper

            self.available = True

        except Exception:

            self.available = False

    def process(
        self,
        text,
        language="auto"
    ):

        start = time.time()

        corrected = text

        if self.available:

            try:

                corrected = (
                    self.engine.correct(
                        text
                    )
                )

            except Exception:

                corrected = text

        return CleanupResult(

            text=corrected,

            provider="harper",

            latency=round(
                time.time()
                - start,
                3
            ),

            language=language
        )