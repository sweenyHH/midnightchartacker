from pathlib import Path
import sys


def resource_path(relative_path):

# Running from PyInstaller bundle
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path

# Running from source
    return (
        Path(__file__)
        .resolve()
        .parent
        .parent
        .parent
        / relative_path
    )