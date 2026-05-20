class TodoExtractor:

    def extract(
        self,
        text
    ):

        lower = text.lower()

        triggers = [

            "todo",

            "need to",

            "remember",

            "action item",

            "must",

            "should"
        ]

        todos = []

        sentences = (
            text.split(
                "."
            )
        )

        for sentence in sentences:

            s = (
                sentence
                .strip()
            )

            if not s:

                continue

            matched = any(
                trigger in s.lower()
                for trigger
                in triggers
            )

            if matched:

                todos.append(
                    s
                )

        return todos