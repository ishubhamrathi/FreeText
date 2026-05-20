class HotwordManager:

    def __init__(self):

        self.mode = "default"

    def process(
        self,
        text
    ):

        lower = text.lower()

        if "start coding mode" in lower:

            self.mode = "coding"

            return "coding"

        if "start meeting mode" in lower:

            self.mode = "meeting"

            return "meeting"

        if "reset mode" in lower:

            self.mode = "default"

            return "default"

        return self.mode