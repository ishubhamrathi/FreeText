from datetime import datetime


class JournalMode:

    def process(
        self,
        text
    ):

        today = (
            datetime.now()
            .strftime(
                "%Y-%m-%d"
            )
        )

        return {

            "date":
            today,

            "entry":
            text.strip()
        }