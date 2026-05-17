class StreamingContext:

    def __init__(self):

        self.previous_text = ""

    def update(
        self,
        text
    ):

        self.previous_text = text[-200:]

    def get_context(
        self
    ):

        return self.previous_text