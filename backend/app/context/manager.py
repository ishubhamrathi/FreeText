from context.memory import (
    ContextMemory
)


class ContextManager:

    def __init__(self):

        self.memory = (
            ContextMemory()
        )

    def update(
        self,
        text,
        mode=None
    ):

        if mode:

            self.memory.set_mode(
                mode
            )

        self.memory.add_text(
            text
        )

    def get_mode(
        self
    ):

        return (
            self.memory
            .state
            .mode
        )

    def get_text(
        self
    ):

        return (
            self.memory
            .state
            .session_text
        )

    def reset(
        self
    ):

        self.memory.clear()