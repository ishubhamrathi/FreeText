from config.settings import (
    CLEANUP_MODE
)


class CleanupRouter:

    def __init__(self):

        from ai.providers.languagetool_provider import (
            LanguageToolProvider
        )

        from ai.providers.ollama_provider import (
            OllamaProvider
        )

        self.language_tool = (
            LanguageToolProvider()
        )

        self.ollama = (
            OllamaProvider()
        )

        self.providers = {
            "languagetool":
                self.language_tool,

            "ollama":
                self.ollama
        }

    def get_provider(
        self,
        language: str
    ):

        if CLEANUP_MODE != "local":

            print(
                f"Forced provider: "
                f"{CLEANUP_MODE}"
            )

            return self.providers[
                CLEANUP_MODE
            ]

        print(
            "Using local routing"
        )

        if language == "en":

            print(
                "English → LanguageTool"
            )

            return self.language_tool

        print(
            "Multilingual → Ollama"
        )

        return self.ollama