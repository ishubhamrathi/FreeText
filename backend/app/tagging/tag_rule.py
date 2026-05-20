from dataclasses import dataclass


@dataclass
class TagRule:

    tag: str

    keywords: list[str]