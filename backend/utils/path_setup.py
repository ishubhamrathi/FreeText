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


def add_app_to_path():

    app_path = str(APP_DIR)

    if app_path not in sys.path:

        sys.path.insert(
            0,
            app_path
        )
