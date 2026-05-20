class LanguageRouter:

    def detect(
        self,
        language
    ):

        if language:

            return language

        return "auto"

    def normalize(
        self,
        language
    ):

        mapping = {

            "en":
            "english",

            "hi":
            "hindi",

            "ja":
            "japanese",

            "ko":
            "korean"
        }

        return mapping.get(
            language,
            language
        )