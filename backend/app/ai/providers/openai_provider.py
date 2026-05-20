import time

from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class OpenAiProvider(
    AiProvider
):

    def __init__(self):

        self.client = None

        self.api_key = ""

    def configure(
        self,
        api_key
    ):

        self.api_key = api_key

        if api_key:

            from openai import OpenAI

            self.client = (
                OpenAI(
                    api_key=api_key
                )
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
                provider="openai",
                language=language
            )

        response = (
            self.client.chat.completions.create(
                model="gpt-4.1-mini",

                messages=[
                    {
                        "role":
                        "system",

                        "content":
                        """
Fix grammar.
Keep original meaning.
Return only cleaned text.
"""
                    },

                    {
                        "role":
                        "user",

                        "content":
                        text
                    }
                ]
            )
        )

        cleaned = (
            response
            .choices[0]
            .message.content
        )

        return CleanupResult(

            text=cleaned,

            provider="openai",

            latency=round(
                time.time()
                - start,
                3
            ),

            language=language
        )