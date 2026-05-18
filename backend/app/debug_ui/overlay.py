import queue
import tkinter as tk

from debug_ui.state import (
    OverlayState
)


class OverlayWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "FreeText Debug"
        )

        self.label = tk.Label(
            self.root,
            justify="left",
            anchor="w"
        )

        self.label.pack()

        self.queue = queue.Queue()

        self.root.after(
            100,
            self.process_queue
        )

    def update(
        self,
        state: OverlayState
    ):

        self.queue.put(
            state
        )

    def process_queue(
        self
    ):

        while not self.queue.empty():

            state = (
                self.queue.get()
            )

            text = f"""
Status: {state.status}

Committed:
{state.committed}

Pending:
{state.pending}

Language:
{state.language}

Latency:
{state.latency}

Chunk:
{state.chunk_number}
"""

            self.label.config(
                text=text
            )

        self.root.after(
            100,
            self.process_queue
        )

    def run(
        self
    ):

        self.root.mainloop()