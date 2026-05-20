from ai.providers.harper_provider import (
    HarperProvider
)

from ai.providers.languagetool_provider import (
    LanguageToolProvider
)

from ai.providers.local_provider import (
    LocalProvider
)


class AiRouter:

    def __init__(self):

        self.providers = {

            "local":
            LocalProvider(),

            "languagetool":
            LanguageToolProvider(),

            "harper":
            HarperProvider()
        }

    def get_provider(
        self,
        provider
    ):

        if provider not in self.providers:

            raise ValueError(
                f"""
Unknown provider:
{provider}
"""
            )

        return (
            self.providers[
                provider
            ]
        )