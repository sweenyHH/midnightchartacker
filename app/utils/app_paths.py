from pathlib import Path
import os
import platform
from app.app_info import APP_STORAGE_NAME

# moves folders with user input / char.txt files out of the application folders


def get_app_data_dir():

    if platform.system() == "Windows":

        base = Path(
            os.environ["APPDATA"]
        )

    else:

        base = (
            Path.home()
            / ".local"
            / "share"
        )

    path = base / APP_STORAGE_NAME

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