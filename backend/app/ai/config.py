class AiConfig:

    def __init__(self):

        self.provider = (
            "local"
        )

        self.language = (
            "auto"
        )

        self.api_key = ""

    def set_provider(
        self,
        provider
    ):

        self.provider = provider

    def get_provider(
        self
    ):

        return self.provider