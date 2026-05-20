from tagging.providers.gemini_provider import (
    GeminiTagProvider
)

from tagging.providers.local_ai_provider import (
    LocalAiTagProvider
)

from tagging.providers.openai_provider import (
    OpenAiTagProvider
)

from tagging.providers.rule_provider import (
    RuleTagProvider
)


class TagProviderRouter:

    def __init__(self):

        self.providers = {

            "rule":
            RuleTagProvider(),

            "local":
            LocalAiTagProvider(),

            "openai":
            OpenAiTagProvider(),

            "gemini":
            GeminiTagProvider()
        }

    def get_provider(
        self,
        provider
    ):

        if provider not in self.providers:

            raise ValueError(
                f"""
Unknown tag provider:
{provider}
"""
            )

        return self.providers[
            provider
        ]