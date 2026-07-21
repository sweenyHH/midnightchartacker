from app.game_data.combat_rating_catalog import (
    get_combat_rating_by_key,
    get_combat_rating_by_name,
    get_combat_rating_display_name,
)


def test_lookup_by_key():

    definition = get_combat_rating_by_key(
        "critical_strike"
    )

    assert definition is not None
    assert definition.key == "critical_strike"


def test_lookup_english_name():

    definition = get_combat_rating_by_name(
        "Critical Strike"
    )

    assert definition is not None
    assert definition.key == "critical_strike"


def test_lookup_german_name():

    definition = get_combat_rating_by_name(
        "Kritischer Treffer"
    )

    assert definition is not None
    assert definition.key == "critical_strike"


def test_german_display_name():

    assert (
        get_combat_rating_display_name(
            "critical_strike",
            "de",
        )
        == "Kritischer Treffer"
    )