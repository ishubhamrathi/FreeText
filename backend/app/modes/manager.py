from modes.meeting_mode import (
    MeetingMode
)


class ModeManager:

    def __init__(self):

        self.meeting = (
            MeetingMode()
        )

    def process(
        self,
        mode,
        text
    ):

        if mode == "meeting":

            return (
                self.meeting.process(
                    text
                )
            )

        return []