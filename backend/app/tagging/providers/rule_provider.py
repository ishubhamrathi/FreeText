from tagging.providers.base import (
    TagProvider
)

from tagging.auto_tagger import (
    AutoTagger
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
        text
    ):

        return self.tagger.detect(
            text
        )