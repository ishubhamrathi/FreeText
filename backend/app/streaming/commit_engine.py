from streaming.token import (
    TranscriptToken
)


class CommitEngine:

    def __init__(self):

        self.committed_until = 0.0

    def commit(
        self,
        tokens: list[
            TranscriptToken
        ]
    ):

        output = []

        for token in tokens:

            if (
                token.end
                <= self.committed_until
            ):

                continue

            output.append(
                token.text
            )

            self.committed_until = (
                token.end
            )

        return (
            " ".join(
                output
            ).strip()
        )

    def reset(
        self
    ):

        self.committed_until = 0.0