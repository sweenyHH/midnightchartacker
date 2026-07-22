from app.game_data.raid_catalog import is_featured_raid, get_featured_raids


def build_raid_progress_rows(character):

    raids = {}

    for definition in get_featured_raids():

        raids[
            definition.key
        ] = {
            "instance_key":
                definition.key,

            "instance_name":
                definition.english_name,

            "LFR": "-",
            "N": "-",
            "H": "-",
            "M": "-",
        }

    for lockout in character.lockouts:

        if (
            not lockout.instance_key
        ):
            continue

        if (
            not is_featured_raid(
                lockout.instance_key
            )
        ):
            continue

        row = raids[
            lockout.instance_key
        ]

        progress = (
            f"{lockout.progress_current}"
            f"/"
            f"{lockout.progress_total}"
        )

        difficulty = (
            lockout.difficulty.lower()
        )

        if difficulty == "lfr":
            row["LFR"] = progress

        elif difficulty == "normal":
            row["N"] = progress

        elif difficulty == "heroic":
            row["H"] = progress

        elif difficulty == "mythic":
            row["M"] = progress

    return list(
        raids.values()
    )