from ai.profiles.base import (
    CleanupProfile
)


class ProfessionalProfile(
    CleanupProfile
):

    def build_prompt(
        self,
        text: str
    ):
        return f"""
Rewrite professionally.

Fix:
- grammar
- punctuation
- tone

Keep meaning same.

{text}
"""