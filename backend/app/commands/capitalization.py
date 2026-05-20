class SmartCapitalization:

    def process(
        self,
        text: str
    ):

        text = text.strip()

        if not text:

            return text

        text = (
            text[0]
            .upper()
            +
            text[1:]
        )

        replacements = {

            " i ": " I ",

            " i'm ": " I'm ",

            " i'll ": " I'll ",

            " i've ": " I've "
        }

        lower = (
            " "
            + text
            + " "
        )

        for key, value in replacements.items():

            lower = lower.replace(
                key,
                value
            )

        return lower.strip()