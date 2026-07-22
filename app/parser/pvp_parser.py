import re

from app.model.pvp_bracket import (
    PvPBracket,
)


RATING_RE = re.compile(
    r"^(.*?)"
    r"\s*-\s*Rating:\s*(\d+)"
)


SEASON_BEST_RE = re.compile(
    r"Season Best:\s*(\d+)"
)


WEEKLY_BEST_RE = re.compile(
    r"Weekly Best:\s*(\d+)"
)


SEASON_RE = re.compile(
    r"Season:\s*(\d+)/(\d+)"
)


WEEKLY_RE = re.compile(
    r"Weekly:\s*(\d+)/(\d+)"
)


SEASON_ROUNDS_RE = re.compile(
    r"Season Rounds:\s*(\d+)/(\d+)"
)


WEEKLY_ROUNDS_RE = re.compile(
    r"Weekly Rounds:\s*(\d+)/(\d+)"
)


def parse_pvp_bracket(
    line,
):
    match = RATING_RE.search(
        line
    )

    if not match:
        return None

    bracket = PvPBracket(
        match.group(1).strip()
    )

    bracket.rating = int(
        match.group(2)
    )

    season_best = (
        SEASON_BEST_RE.search(
            line
        )
    )

    if season_best:
        bracket.season_best = int(
            season_best.group(1)
        )

    weekly_best = (
        WEEKLY_BEST_RE.search(
            line
        )
    )

    if weekly_best:
        bracket.weekly_best = int(
            weekly_best.group(1)
        )

    season = SEASON_RE.search(
        line
    )

    if season:
        bracket.season_wins = int(
            season.group(1)
        )

        bracket.season_games = int(
            season.group(2)
        )

    weekly = WEEKLY_RE.search(
        line
    )

    if weekly:
        bracket.weekly_wins = int(
            weekly.group(1)
        )

        bracket.weekly_games = int(
            weekly.group(2)
        )

    season_rounds = (
        SEASON_ROUNDS_RE.search(
            line
        )
    )

    if season_rounds:
        bracket.season_round_wins = int(
            season_rounds.group(1)
        )

        bracket.season_round_games = int(
            season_rounds.group(2)
        )

    weekly_rounds = (
        WEEKLY_ROUNDS_RE.search(
            line
        )
    )

    if weekly_rounds:
        bracket.weekly_round_wins = int(
            weekly_rounds.group(1)
        )

        bracket.weekly_round_games = int(
            weekly_rounds.group(2)
        )

    return bracket