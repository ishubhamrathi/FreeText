from context.models.context_state import (
    ContextState
)


class ContextMemory:

    def __init__(self):

        self.state = (
            ContextState(
                tags=[]
            )
        )

    def set_mode(
        self,
        mode
    ):

        self.state.mode = mode

    def add_text(
        self,
        text
    ):

        self.state.last_text = text

        self.state.session_text += (
            text + " "
        )

    def add_tag(
        self,
        tag
    ):

        if tag not in self.state.tags:

            self.state.tags.append(
                tag
            )

    def clear(
        self
    ):

        self.state = (
            ContextState(
                tags=[]
            )
        )