from app.game_data.pvp_bracket_catalog import (
    get_overview_pvp_brackets,
    get_pvp_bracket_by_name,
)


def build_pvp_overview(
    character,
):

    rows = {}

    for definition in (
        get_overview_pvp_brackets()
    ):

        rows[
            definition.key
        ] = {
            "key": definition.key,
            "rating": None,
        }

    for bracket in (
        character.pvp_brackets
    ):

        definition = (
            get_pvp_bracket_by_name(
                bracket.bracket
            )
        )

        if not definition:
            continue

        if definition.key not in rows:
            continue

        rows[
            definition.key
        ]["rating"] = (
            bracket.rating
        )

    return list(
        rows.values()
    )
