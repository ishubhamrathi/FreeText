from tagging.providers.rule_provider import (
    RuleTagProvider
)


class TagProviderRouter:

    def __init__(self):

        self.rule = (
            RuleTagProvider()
        )

    def get_provider(
        self,
        provider="rule"
    ):

        if provider == "rule":

            return self.rule

        raise ValueError(
            f"Unknown provider: {provider}"
        )