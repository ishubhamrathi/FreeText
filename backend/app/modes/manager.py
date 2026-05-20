from extraction.action_extractor import (
    ActionExtractor
)

from extraction.summary_extractor import (
    SummaryExtractor
)

from extraction.todo_extractor import (
    TodoExtractor
)

from insights.session_insights import (
    SessionInsights
)

from modes.coding_mode import (
    CodingMode
)

from modes.journal_mode import (
    JournalMode
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

        self.journal = (
            JournalMode()
        )

        self.todos = (
            TodoExtractor()
        )

        self.actions = (
            ActionExtractor()
        )

        self.summary = (
            SummaryExtractor()
        )

        self.insights = (
            SessionInsights()
        )

    def process(
        self,
        mode,
        text
    ):

        result = {

            "tags": [],

            "todos": [],

            "actions": [],

            "summary": "",

            "journal": None,

            "insights": {}
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

        if mode == "journal":

            result[
                "journal"
            ] = (
                self.journal.process(
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

        result[
            "summary"
        ] = (
            self.summary.extract(
                text
            )
        )

        result[
            "insights"
        ] = (
            self.insights.analyze(
                text,
                result["todos"],
                result["actions"]
            )
        )

        return result