class OverlapResolver:

    def __init__(self):

        self.last_output = ""

    def merge(
        self,
        text
    ):

        if text.startswith(
            self.last_output
        ):

            return ""

        self.last_output = text

        return text