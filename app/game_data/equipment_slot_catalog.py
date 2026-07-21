import csv
from pathlib import Path

from app.game_data.equipment_slot_definition import (
    EquipmentSlotDefinition,
)


_SLOTS_BY_KEY = {}
_SLOTS_BY_NAME = {}

_LOADED = False


def _load_catalog():

    global _LOADED

    if _LOADED:
        return

    csv_path = (
        Path(__file__).parent
        / "equipment_slots.csv"
    )

    with open(
        csv_path,
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(
            file,
            delimiter=";"
        )

        reader.fieldnames = [
            name.strip()
            for name in reader.fieldnames
        ]

        for row in reader:

            definition = EquipmentSlotDefinition(
                key=row["key"],
                english_name=row["english_name"],
                german_name=row["german_name"],
                french_name=row["french_name"],
            )

            # ----------------------------------
            # KEY LOOKUP
            # ----------------------------------

            if (
                definition.key
                in _SLOTS_BY_KEY
            ):
                raise ValueError(
                    f"Duplicate slot key: "
                    f"{definition.key}"
                )

            _SLOTS_BY_KEY[
                definition.key
            ] = definition

            # ----------------------------------
            # NAME LOOKUPS
            # ----------------------------------

            for name in (
                definition.english_name,
                definition.german_name,
                definition.french_name,
            ):

                if not name:
                    continue

                _SLOTS_BY_NAME[
                    name.casefold()
                ] = definition

    _LOADED = True


def get_equipment_slot_by_key(
    key,
):

    _load_catalog()

    return _SLOTS_BY_KEY.get(
        key
    )


def get_equipment_slot_by_name(
    name,
):

    _load_catalog()

    if not name:
        return None

    return _SLOTS_BY_NAME.get(
        name.casefold()
    )


def get_equipment_slot_display_name(
    key,
    language,
):

    _load_catalog()

    definition = (
        _SLOTS_BY_KEY.get(key)
    )

    if definition is None:
        return key

    if language == "de":
        return definition.german_name

    if language == "fr":
        return definition.french_name

    return definition.english_name