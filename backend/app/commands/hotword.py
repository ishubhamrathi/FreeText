class HotwordManager:

    def __init__(self):

        self.mode = "default"

    def process(
        self,
        text
    ):

        lower = text.lower()

        modes = {

            "start coding mode":
            "coding",

            "start meeting mode":
            "meeting",

            "start youtube mode":
            "youtube",

            "start journal mode":
            "journal",

            "reset mode":
            "default"
        }

        for phrase, mode in modes.items():

            if phrase in lower:

                self.mode = mode

                return mode

        return self.mode