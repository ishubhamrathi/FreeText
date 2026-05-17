import traceback

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

        try:
            return provider.cleanup_text(
                text
            )
        except Exception:
            print("Cleanup provider failed, returning original text:")
            traceback.print_exc()
            return text

