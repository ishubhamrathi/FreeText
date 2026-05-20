from dataclasses import dataclass


@dataclass
class CommandResult:

    text: str

    handled: bool = False

    undo: bool = False

    new_paragraph: bool = False

    capitalize: bool = True

    mode: str | None = None