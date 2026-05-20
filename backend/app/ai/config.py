class AiConfig:

    def __init__(self):

        self.provider = (
            "local"
        )

        self.language = (
            "auto"
        )

        self.api_key = ""

        self.use_fallback = True

    def set_provider(
        self,
        provider
    ):

        self.provider = provider

    def get_provider(
        self
    ):

        return self.provider

    def enable_fallback(
        self,
        enabled
    ):

        self.use_fallback = enabled