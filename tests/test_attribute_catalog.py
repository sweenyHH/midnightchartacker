from app.game_data.attribute_catalog import (
    get_attribute_by_key,
    get_attribute_by_name,
    get_attribute_display_name,
)


def test_lookup_by_key():

    definition = get_attribute_by_key(
        "strength"
    )

    assert definition is not None
    assert definition.key == "strength"


def test_lookup_english_name():

    definition = get_attribute_by_name(
        "Strength"
    )

    assert definition is not None
    assert definition.key == "strength"


def test_lookup_german_name():

    definition = get_attribute_by_name(
        "Stärke"
    )

    assert definition is not None
    assert definition.key == "strength"


def test_english_display_name():

    assert (
        get_attribute_display_name(
            "strength",
            "en",
        )
        == "Strength"
    )


def test_german_display_name():

    assert (
        get_attribute_display_name(
            "strength",
            "de",
        )
        == "Stärke"
    )