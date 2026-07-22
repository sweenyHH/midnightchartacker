import re

from app.model.lockout import (
    InstanceLockout,
    BossLockout,
)
from app.game_data.raid_catalog import get_raid_by_name



INSTANCE_RE = re.compile(
    r"^(.*?) "
    r"\((.*?),\s*(\d+),\s*(Raid|Dungeon)\)"
    r"\s*-\s*Locked:\s*(yes|no)"
    r"\s*-\s*Extended:\s*(yes|no)"
    r"\s*-\s*Reset:\s*(.*?)"
    r"\s*-\s*Progress:\s*(\d+)/(\d+)"
    r"\s*-\s*Lockout ID:\s*(\d+)"
)


BOSS_RE = re.compile(
    r"^\s*-\s*(.*?):\s*(.*?)$"
)


def parse_instance_lockout(
    line,
):
    match = INSTANCE_RE.match(
        line.strip()
    )

    if not match:
        return None

    lockout = InstanceLockout(
        match.group(1).strip()
    )

    definition = get_raid_by_name(
        lockout.instance_name
    )

    if definition:
        lockout.instance_key = (
            definition.key
        )

    lockout.difficulty = (
        match.group(2).strip()
    )

    lockout.size = int(
        match.group(3)
    )

    lockout.content_type = (
        match.group(4).lower()
    )

    lockout.locked = (
        match.group(5).lower()
        == "yes"
    )

    lockout.extended = (
        match.group(6).lower()
        == "yes"
    )

    lockout.reset = (
        match.group(7).strip()
    )

    lockout.progress_current = int(
        match.group(8)
    )

    lockout.progress_total = int(
        match.group(9)
    )

    lockout.lockout_id = int(
        match.group(10)
    )

    return lockout


def parse_boss_lockout(
    line,
):
    match = BOSS_RE.match(
        line
    )

    if not match:
        return None

    return BossLockout(
        boss_name=match.group(1).strip(),
        status=match.group(2).strip(),
    )