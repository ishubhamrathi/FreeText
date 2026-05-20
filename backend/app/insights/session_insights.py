class SessionInsights:

    def analyze(
        self,
        text,
        todos,
        actions
    ):

        words = (
            text.split()
        )

        return {

            "word_count":
            len(words),

            "todo_count":
            len(todos),

            "action_count":
            len(actions),

            "character_count":
            len(text),

            "estimated_minutes":
            round(
                len(words)
                / 130,
                2
            )
        }