from pathlib import Path
import os

# moves folders with user input / char.txt files out of the application folders

APP_NAME = "Midnight Character Tracker"


def get_app_data_dir():

    base = Path(
        os.environ["APPDATA"]
    )

    path = base / APP_NAME

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return path


def get_import_dir():

    path = get_app_data_dir() / "import"

    path.mkdir(
        exist_ok=True
    )

    return path


def get_data_dir():

    path = get_app_data_dir() / "data"

    path.mkdir(
        exist_ok=True
    )

    return path


def get_log_dir():

    path = get_app_data_dir() / "logs"

    path.mkdir(
        exist_ok=True
    )

    return path