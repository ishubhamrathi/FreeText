class MeetingMode:

    def process(
        self,
        text
    ):

        lower = text.lower()

        tags = []

        if (
            "action item"
            in lower
        ):

            tags.append(
                "task"
            )

        if (
            "decision"
            in lower
        ):

            tags.append(
                "decision"
            )

        if (
            "follow up"
            in lower
        ):

            tags.append(
                "followup"
            )

        return tags