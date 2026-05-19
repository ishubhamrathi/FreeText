from path_setup import add_app_to_path


add_app_to_path()

from export.manager import (
    ExportManager
)


manager = ExportManager()

manager.export_txt(
    1
)

manager.export_md(
    1
)
