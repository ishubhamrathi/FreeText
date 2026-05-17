class CommitEngine:

    def __init__(self):

        self.output = ""

    def commit(
        self,
        tokens
    ):

        text = " ".join(
            token.text
            for token in tokens
        ).strip()

        if text.startswith(
            self.output
        ):

            delta = text[
                len(
                    self.output
                ):
            ].strip()

            self.output = text

            return delta

        self.output = text

        return text