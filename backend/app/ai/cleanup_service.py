from ai.router import CleanupRouter


class CleanupService:

    def __init__(self):

        self.router = CleanupRouter()

    def cleanup_text(
        self,
        text: str,
        language: str
    ) -> str:

        provider = self.router.get_provider(
            language
        )

        return provider.cleanup_text(
            text
        )