from streaming.token import (
    TranscriptToken
)


class TokenStabilizer:

    def __init__(self):

        self.previous = []

    def update(
        self,
        current
    ):

        stable = []

        limit = min(
            len(self.previous),
            len(current)
        )

        for i in range(limit):

            old = self.previous[i]

            new = current[i]

            if (
                old.text
                == new.text
            ):

                stable.append(
                    new
                )

            else:

                break

        self.previous = current

        return stable