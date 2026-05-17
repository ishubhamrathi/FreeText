from streaming.token import (
    TranscriptToken
)


class TokenStabilizer:

    def __init__(self):

        self.tokens = []

        self.commit_index = 0

    def update(
        self,
        incoming_tokens
    ):

        self.tokens = incoming_tokens

        stable = []

        for i in range(
            self.commit_index,
            len(self.tokens) - 2
        ):

            token = self.tokens[i]

            if not token.committed:

                token.committed = True

                stable.append(
                    token
                )

        self.commit_index += len(
            stable
        )

        return stable