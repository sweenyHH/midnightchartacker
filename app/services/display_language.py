from app.storage.settings_storage import (
    load_setting,
)


def get_display_language():

    return load_setting(
        "display_language",
        "en",
    )