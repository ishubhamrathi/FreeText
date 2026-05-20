from tagging.auto_tagger import (
    AutoTagger
)


class TagManager:

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