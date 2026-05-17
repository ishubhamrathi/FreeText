from ai.providers.languagetool_provider import (
    LanguageToolProvider
)

from ai.providers.ollama_provider import (
    OllamaProvider
)

from ai.providers.openai_provider import (
    OpenAIProvider
)

from config.settings import (
    CLEANUP_PROVIDER
)


class CleanupProviderFactory:

    @staticmethod
    def create():
        if CLEANUP_PROVIDER == "languagetool":
            return LanguageToolProvider()

        if CLEANUP_PROVIDER == "ollama":
            return OllamaProvider()

        if CLEANUP_PROVIDER == "openai":
            return OpenAIProvider()

        raise ValueError(
            "Invalid cleanup provider"
        )