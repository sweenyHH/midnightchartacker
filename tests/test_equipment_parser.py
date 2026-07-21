from app.parser.equipment_parser import (
    parse_equipment,
)


def test_head_slot_is_canonical():

    lines = [
        "Equipment:",
        "== Head ==",
        "[Test Helm] iLvl: 700",
    ]

    equipment = parse_equipment(
        lines
    )

    assert (
        equipment[0].slot
        == "head"
    )