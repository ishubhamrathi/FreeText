from extraction.action_extractor import (
    ActionExtractor
)

from extraction.todo_extractor import (
    TodoExtractor
)

from modes.coding_mode import (
    CodingMode
)

from modes.meeting_mode import (
    MeetingMode
)


class ModeManager:

    def __init__(self):

        self.meeting = (
            MeetingMode()
        )

        self.coding = (
            CodingMode()
        )

        self.todos = (
            TodoExtractor()
        )

        self.actions = (
            ActionExtractor()
        )

    def process(
        self,
        mode,
        text
    ):

        result = {

            "tags": [],

            "todos": [],

            "actions": []
        }

        if mode == "meeting":

            result[
                "tags"
            ] = (
                self.meeting.process(
                    text
                )
            )

        if mode == "coding":

            result[
                "tags"
            ] = (
                self.coding.process(
                    text
                )
            )

        result[
            "todos"
        ] = (
            self.todos.extract(
                text
            )
        )

        result[
            "actions"
        ] = (
            self.actions.extract(
                text
            )
        )

        return result