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

        if not text:
            return ""

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

    def reset(
        self
    ):

        self.output = ""