from ai.profiles.base import (
    CleanupProfile
)


class CasualProfile(
    CleanupProfile
):

    def build_prompt(
        self,
        text: str
    ):
        return f"""
Fix grammar.

Keep casual tone.

{text}
"""