from app.model.character import Character
from app.parser.section_parser import (
    handle_section,
)

def test_combat_rating_is_stored_as_canonical_key():

    character = Character(
        "Test"
    )

    handle_section(
        "Critical Strike: 1000 rating / 10%",
        "combat_ratings",
        character,
    )

    assert (
        "critical_strike"
        in character.combat_ratings
    )


def test_attribute_is_stored_as_canonical_key():

    character = Character(
        "Test"
    )

    handle_section(
        "Strength: 12345",
        "attributes",
        character,
    )

    assert (
        "strength"
        in character.attributes
    )

    assert (
        character.attributes[
            "strength"
        ]
        == "12345"
    )