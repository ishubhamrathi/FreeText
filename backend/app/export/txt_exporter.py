from export.exporter import (
    Exporter
)

class TxtExporter(
    Exporter
):

    def export(
        self,
        session,
        output_path
    ):

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                session
            )