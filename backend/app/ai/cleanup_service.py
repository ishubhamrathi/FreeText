from ai.providers.factory import (
    CleanupProviderFactory
)


class CleanupService:

    def __init__(self):
        self.provider = (
            CleanupProviderFactory
            .create()
        )

    def cleanup_text(
        self,
        text: str
    ) -> str:
        return self.provider.cleanup_text(
            text
        )