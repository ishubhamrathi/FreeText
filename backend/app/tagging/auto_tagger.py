from tagging.tag_rule import (
    TagRule
)


class AutoTagger:

    def __init__(self):

        self.rules = [

            TagRule(
                "meeting",
                [
                    "meeting",
                    "agenda",
                    "discussion",
                    "client"
                ]
            ),

            TagRule(
                "coding",
                [
                    "bug",
                    "code",
                    "api",
                    "deploy",
                    "spring",
                    "python"
                ]
            ),

            TagRule(
                "idea",
                [
                    "idea",
                    "startup",
                    "thought"
                ]
            ),

            TagRule(
                "task",
                [
                    "todo",
                    "task",
                    "remember"
                ]
            ),

            TagRule(
                "youtube",
                [
                    "video",
                    "youtube",
                    "content"
                ]
            )
        ]

    def detect(
        self,
        text: str
    ):

        text = text.lower()

        tags = []

        for rule in self.rules:

            matched = any(
                keyword in text
                for keyword
                in rule.keywords
            )

            if matched:

                tags.append(
                    rule.tag
                )

        return ",".join(
            sorted(
                set(tags)
            )
        )