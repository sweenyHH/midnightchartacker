import csv
from pathlib import Path

from app.game_data.pvp_bracket_catalog_definition import (
    PvpBracketCatalogDefinition,
)


_BRACKETS_BY_ID = {}
_BRACKETS_BY_KEY = {}
_BRACKETS_BY_NAME = {}

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

    _BRACKETS_BY_ID.clear()
    _BRACKETS_BY_KEY.clear()
    _BRACKETS_BY_NAME.clear()

    csv_path = (
        Path(__file__).parent
        / "pvp_brackets.csv"
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
                PvpBracketCatalogDefinition(
                    bracket_id=int(
                        row["id"]
                    ),

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

                    overview=_to_bool(
                        row["overview"]
                    ),
                )
            )

            if (
                definition.bracket_id
                in _BRACKETS_BY_ID
            ):
                raise ValueError(
                    f"Duplicate bracket id: "
                    f"{definition.bracket_id}"
                )

            if (
                definition.key
                in _BRACKETS_BY_KEY
            ):
                raise ValueError(
                    f"Duplicate bracket key: "
                    f"{definition.key}"
                )

            _BRACKETS_BY_ID[
                definition.bracket_id
            ] = definition

            _BRACKETS_BY_KEY[
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

                _BRACKETS_BY_NAME[
                    lookup_name
                ] = definition

    _LOADED = True


def get_pvp_bracket_by_key(
    key,
):
    _load_catalog()

    return _BRACKETS_BY_KEY.get(
        key
    )


def get_pvp_bracket_by_name(
    name,
):
    _load_catalog()

    if not name:
        return None

    return _BRACKETS_BY_NAME.get(
        name.casefold()
    )


def get_overview_pvp_brackets():

    _load_catalog()

    return [
        definition
        for definition
        in _BRACKETS_BY_ID.values()
        if definition.overview
    ]


def get_pvp_bracket_display_name(
    key,
    language,
):
    _load_catalog()

    definition = (
        _BRACKETS_BY_KEY.get(key)
    )

    if definition is None:
        return key

    if language == "de":
        return definition.german_name

    if language == "fr":
        return definition.french_name

    return definition.english_name