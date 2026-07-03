import app.storage.settings_storage as storage


def test_load_unknown_setting_returns_default(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    result = storage.load_setting(
        "theme",
        "dark"
    )

    assert result == "dark"


def test_save_setting(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    storage.save_setting(
        "theme",
        "wow"
    )

    assert (
        storage.load_setting("theme")
        == "wow"
    )


def test_overwrite_existing_setting(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    storage.save_setting(
        "theme",
        "dark"
    )

    storage.save_setting(
        "theme",
        "modern"
    )

    assert (
        storage.load_setting("theme")
        == "modern"
    )


def test_multiple_settings(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    storage.save_setting(
        "theme",
        "wow"
    )

    storage.save_setting(
        "default_tab",
        "overview"
    )

    assert (
        storage.load_setting("theme")
        == "wow"
    )

    assert (
        storage.load_setting("default_tab")
        == "overview"
    )


def test_missing_file_returns_default(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "does_not_exist.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    assert (
        storage.load_setting(
            "theme",
            "dark"
        )
        == "dark"
    )


def test_setting_persists_after_reload(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    storage.save_setting(
        "theme",
        "light"
    )

    result = storage.load_setting(
        "theme"
    )

    assert result == "light"


def test_unknown_setting_without_default_returns_none(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    assert (
        storage.load_setting(
            "does_not_exist"
        )
        is None
    )


def test_saving_second_setting_does_not_overwrite_first(
    tmp_path,
    monkeypatch,
):

    settings_file = tmp_path / "settings.txt"

    monkeypatch.setattr(
        storage,
        "SETTINGS_FILE",
        settings_file
    )

    storage.save_setting(
        "theme",
        "modern"
    )

    storage.save_setting(
        "window_mode",
        "maximized"
    )

    assert (
        storage.load_setting("theme")
        == "modern"
    )

    assert (
        storage.load_setting("window_mode")
        == "maximized"
    )