class ActionExtractor:

    def extract(
        self,
        text
    ):

        verbs = [

            "fix",

            "deploy",

            "create",

            "review",

            "implement",

            "update",

            "refactor",

            "test"
        ]

        actions = []

        lines = text.split(
            "\n"
        )

        for line in lines:

            lower = (
                line.lower()
            )

            for verb in verbs:

                if verb in lower:

                    actions.append(
                        line.strip()
                    )

                    break

        return actions