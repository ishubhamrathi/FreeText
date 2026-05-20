class SmartPunctuation:

    def __init__(self):

        self.mapping = {

            "comma": ",",

            "full stop": ".",

            "period": ".",

            "question mark": "?",

            "exclamation mark": "!",

            "new line": "\n",

            "next line": "\n",

            "colon": ":",

            "semicolon": ";"
        }

    def process(
        self,
        text: str
    ):

        result = text

        for key, value in self.mapping.items():

            result = result.replace(
                key,
                value
            )

        return result