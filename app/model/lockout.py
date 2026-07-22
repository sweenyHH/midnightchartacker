class BossLockout:

    def __init__(
        self,
        boss_name: str,
        status: str,
    ):
        self.boss_name = boss_name
        self.status = status


class InstanceLockout:

    def __init__(
        self,
        instance_name: str,
    ):
        self.instance_name = instance_name
        self.instance_key = None

        self.difficulty = None
        self.size = None
        self.content_type = None

        self.locked = False
        self.extended = False

        self.reset = None

        self.progress_current = 0
        self.progress_total = 0

        self.lockout_id = None

        self.bosses = []

    def add_boss(
        self,
        boss,
    ):
        self.bosses.append(
            boss
        )