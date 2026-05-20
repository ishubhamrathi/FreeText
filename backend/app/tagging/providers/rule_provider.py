from tagging.auto_tagger import (
    AutoTagger
)

from tagging.providers.base import (
    TagProvider
)


class RuleTagProvider(
    TagProvider
):

    def __init__(self):

        self.tagger = (
            AutoTagger()
        )

    def generate(
        self,
        text,
        language="auto"
    ):

        return self.tagger.detect(
            text
        )