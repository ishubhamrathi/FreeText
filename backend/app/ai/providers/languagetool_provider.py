import language_tool_python

from ai.providers.base import (
    CleanupProvider
)


class LanguageToolProvider(
    CleanupProvider
):

    def __init__(self):
        self.tool = (
            language_tool_python
            .LanguageTool("en-US")
        )

    def cleanup_text(
        self,
        text: str
    ) -> str:
        matches = self.tool.check(text)

        return self.tool.correct(
            text
        )