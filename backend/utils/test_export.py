import sys

from pathlib import Path


ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent.parent
)

APP_DIR = (
    ROOT_DIR
    / "app"
)

sys.path.append(
    str(APP_DIR)
)

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