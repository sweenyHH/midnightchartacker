from app.storage.settings_storage import (
    save_setting,
)

from app.services.display_language import (
    get_display_language,
)


def test_default_display_language():

    save_setting(
        "display_language",
        "en",
    )

    assert (
        get_display_language()
        == "en"
    )


def test_saved_display_language():

    save_setting(
        "display_language",
        "de",
    )

    assert (
        get_display_language()
        == "de"
    )
