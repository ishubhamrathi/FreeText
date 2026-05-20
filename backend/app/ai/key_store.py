import json
from pathlib import Path


class KeyStore:

    def __init__(self):

        self.path = Path(
            "ai_keys.json"
        )

    def save(
        self,
        provider,
        key
    ):

        data = {}

        if self.path.exists():

            data = json.loads(
                self.path.read_text(
                    encoding="utf-8"
                )
            )

        data[
            provider
        ] = key

        self.path.write_text(
            json.dumps(
                data,
                indent=4
            ),
            encoding="utf-8"
        )

    def get(
        self,
        provider
    ):

        if not self.path.exists():

            return ""

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        return data.get(
            provider,
            ""
        )