from ai.profiles.factory import (
    ProfileFactory
)

from ai.providers.factory import (
    CleanupProviderFactory
)


class CleanupService:

    def __init__(self):

        self.provider = (
            CleanupProviderFactory
            .create()
        )

        self.profile = (
            ProfileFactory.create()
        )

    def cleanup_text(
        self,
        text: str
    ):

        prompt = (
            self.profile.build_prompt(
                text
            )
        )

        return (
            self.provider.cleanup_text(
                prompt
            )
        )