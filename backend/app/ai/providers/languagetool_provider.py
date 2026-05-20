import time

import language_tool_python

from ai.models.cleanup_result import (
    CleanupResult
)

from ai.providers.base import (
    AiProvider
)


class LanguageToolProvider(
    AiProvider
):

    def __init__(self):

        self.tools = {}

    def get_tool(
        self,
        language
    ):

        mapping = {

            "en":
            "en-US",

            "hi":
            "en-US"
        }

        key = mapping.get(
            language,
            "en-US"
        )

        if key not in self.tools:

            self.tools[key] = (
                language_tool_python
                .LanguageTool(
                    key
                )
            )

        return self.tools[
            key
        ]

    def process(
        self,
        text,
        language="en"
    ):

        start = time.time()

        tool = (
            self.get_tool(
                language
            )
        )

        corrected = (
            tool.correct(
                text
            )
        )

        return CleanupResult(

            text=corrected,

            provider=
            "languagetool",

            latency=round(
                time.time()
                - start,
                3
            ),

            language=language
        )