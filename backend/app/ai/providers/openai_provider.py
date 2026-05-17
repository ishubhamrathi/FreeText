from openai import OpenAI

from ai.providers.base import (
    CleanupProvider
)

from config.settings import (
    OPENAI_API_KEY
)


class OpenAIProvider(
    CleanupProvider
):

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def cleanup_text(
        self,
        text: str
    ) -> str:
        response = (
            self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content":
                        (
                            "Fix grammar and punctuation:\n\n"
                            + text
                        )
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message.content
            .strip()
        )