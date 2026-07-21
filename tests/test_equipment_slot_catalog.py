from app.game_data.equipment_slot_catalog import (
    get_equipment_slot_by_key,
    get_equipment_slot_by_name,
    get_equipment_slot_display_name,
)


def test_lookup_by_key():

    definition = get_equipment_slot_by_key(
        "head"
    )

    assert definition is not None
    assert definition.key == "head"


def test_lookup_english_name():

    definition = get_equipment_slot_by_name(
        "Head"
    )

    assert definition is not None
    assert definition.key == "head"


def test_lookup_german_name():

    definition = get_equipment_slot_by_name(
        "Kopf"
    )

    assert definition is not None
    assert definition.key == "head"


def test_english_display_name():

    assert (
        get_equipment_slot_display_name(
            "head",
            "en",
        )
        == "Head"
    )


def test_german_display_name():

    assert (
        get_equipment_slot_display_name(
            "head",
            "de",
        )
        == "Kopf"
    )