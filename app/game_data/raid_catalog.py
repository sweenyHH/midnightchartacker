import csv
from pathlib import Path

from app.game_data.raid_catalog_definition import (
    RaidCatalogDefinition,
)


_RAIDS_BY_KEY = {}
_RAIDS_BY_NAME = {}

_LOADED = False


def _to_bool(value):

    return (
        str(value)
        .strip()
        .upper()
        == "TRUE"
    )


def _load_catalog():

    global _LOADED

    if _LOADED:
        return

    _RAIDS_BY_KEY.clear()
    _RAIDS_BY_NAME.clear()

    csv_path = (
        Path(__file__).parent
        / "raids-and-dungeons.csv"
    )

    with open(
        csv_path,
        encoding="utf-8-sig",
        newline="",
    ) as file:

        reader = csv.DictReader(
            file,
            delimiter=";",
        )

        reader.fieldnames = [
            name.strip()
            for name in reader.fieldnames
        ]

        for row in reader:

            definition = (
                RaidCatalogDefinition(
                    raid_id=int(row["id"]),
                    key=row["key"],

                    english_name=row[
                        "english_name"
                    ],
                    german_name=row[
                        "german_name"
                    ],
                    french_name=row[
                        "french_name"
                    ],

                    content_type=row[
                        "content_type"
                    ],

                    featured=_to_bool(
                        row["featured"]
                    ),
                )
            )

            if (
                definition.key
                in _RAIDS_BY_KEY
            ):
                raise ValueError(
                    f"Duplicate raid key: "
                    f"{definition.key}"
                )

            _RAIDS_BY_KEY[
                definition.key
            ] = definition

            for name in (
                definition.english_name,
                definition.german_name,
                definition.french_name,
            ):

                lookup_name = (
                    name.casefold()
                )

                if (
                    lookup_name
                    not in _RAIDS_BY_NAME
                ):
                    _RAIDS_BY_NAME[
                        lookup_name
                    ] = definition

    _LOADED = True


def get_raid_by_key(
    key,
):
    _load_catalog()

    return _RAIDS_BY_KEY.get(
        key
    )


def get_raid_by_name(
    name,
):
    _load_catalog()

    if not name:
        return None

    return _RAIDS_BY_NAME.get(
        name.casefold()
    )


def is_featured_raid(
    key,
):
    _load_catalog()

    definition = (
        _RAIDS_BY_KEY.get(key)
    )

    if definition is None:
        return False

    return definition.featured


def get_raid_display_name(
    key,
    language,
):
    _load_catalog()

    definition = (
        _RAIDS_BY_KEY.get(key)
    )

    if definition is None:
        return key

    if language == "de":
        return definition.german_name

    if language == "fr":
        return definition.french_name

    return definition.english_name

def get_featured_raids():

    _load_catalog()

    return [
        definition
        for definition
        in _RAIDS_BY_KEY.values()
        if definition.featured
    ]