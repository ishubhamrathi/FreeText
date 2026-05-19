from pathlib import Path

from export.markdown_exporter import (
    MarkdownExporter
)

from export.txt_exporter import (
    TxtExporter
)

from history.replay_service import (
    ReplayService
)

class ExportManager:

    def __init__(self):

        self.replay = (
            ReplayService()
        )

        self.txt = (
            TxtExporter()
        )

        self.md = (
            MarkdownExporter()
        )

    def export_txt(
        self,
        session_id
    ):

        text = (
            self.replay.replay(
                session_id
            )
        )

        if not text:
            return

        path = (
            Path(
                f"session_{session_id}.txt"
            )
        )

        self.txt.export(
            text,
            path
        )

        print(
            f"Saved {path}"
        )

    def export_md(
        self,
        session_id
    ):

        text = (
            self.replay.replay(
                session_id
            )
        )

        if not text:
            return

        path = (
            Path(
                f"session_{session_id}.md"
            )
        )

        self.md.export(
            text,
            path
        )

        print(
            f"Saved {path}"
        )