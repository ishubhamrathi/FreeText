from ai.providers.gemini_provider import (
    GeminiProvider
)

from ai.providers.languagetool_provider import (
    LanguageToolProvider
)

from ai.providers.local_provider import (
    LocalProvider
)

from ai.providers.openai_provider import (
    OpenAiProvider
)


class AiRouter:

    def __init__(self):

        self.providers = {

            "local":
            LocalProvider(),

            "languagetool":
            LanguageToolProvider(),

            "openai":
            OpenAiProvider(),

            "gemini":
            GeminiProvider()
        }

    def get_provider(
        self,
        provider
    ):

        return (
            self.providers[
                provider
            ]
        )