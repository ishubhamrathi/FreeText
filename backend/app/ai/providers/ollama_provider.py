import ollama

from ai.providers.base import (
    CleanupProvider
)

from config.settings import (
    OLLAMA_MODEL
)


class OllamaProvider(
    CleanupProvider
):

    def cleanup_text(
        self,
        text: str
    ) -> str:
        prompt = f"""
Fix grammar and punctuation.
Keep original meaning.

{text}
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        return (
            response["message"]["content"]
            .strip()
        )