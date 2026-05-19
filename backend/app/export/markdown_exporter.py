from export.exporter import (
    Exporter
)

class MarkdownExporter(
    Exporter
):

    def export(
        self,
        session,
        output_path
    ):

        content = f"""
# FreeText Session

{session}
"""

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                content
            )