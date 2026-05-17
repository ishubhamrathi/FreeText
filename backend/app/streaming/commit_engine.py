class CommitEngine:

    def commit(
        self,
        tokens
    ):

        return " ".join(
            token.text
            for token in tokens
        )