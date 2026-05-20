from ai.manager import (
    AiManager
)


class FallbackManager:

    def __init__(self):

        self.ai = (
            AiManager()
        )

        self.chain = [

            "harper",

            "languagetool",

            "local"
        ]

    def cleanup(
        self,
        text,
        language="auto"
    ):

        for provider in self.chain:

            try:

                result = (
                    self.ai.cleanup(
                        text=text,

                        provider=provider,

                        language=language
                    )
                )

                if result.text:

                    return result

            except Exception:

                continue

        return self.ai.cleanup(
            text=text,

            provider="local",

            language=language
        )