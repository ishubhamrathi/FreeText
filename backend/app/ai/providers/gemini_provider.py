import time

from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class GeminiProvider(
    AiProvider
):

    def __init__(self):

        self.client = None

    def configure(
        self,
        api_key
    ):

        if api_key:

            import google.generativeai as genai

            genai.configure(
                api_key=api_key
            )

            self.client = (
                genai
            )

    def process(
        self,
        text,
        language="auto"
    ):

        start = time.time()

        if not self.client:

            return CleanupResult(
                text=text,
                provider="gemini",
                language=language
            )

        model = (
            self.client
            .GenerativeModel(
                "gemini-2.0-flash"
            )
        )

        result = model.generate_content(
            f"""
Fix grammar.

{text}
"""
        )

        cleaned = (
            result.text
        )

        return CleanupResult(

            text=cleaned,

            provider="gemini",

            latency=round(
                time.time()
                - start,
                3
            ),

            language=language
        )