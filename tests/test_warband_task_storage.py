import app.storage.warband_task_storage as storage


def test_load_tasks_empty_file(tmp_path, monkeypatch):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    assert storage.load_tasks() == []


def test_add_task(tmp_path, monkeypatch):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    result = storage.add_task(
        "Farm Invincible"
    )

    assert result is True

    assert storage.load_tasks() == [
        "Farm Invincible"
    ]


def test_duplicate_task_rejected(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    assert storage.add_task(
        "Farm Invincible"
    ) is True

    assert storage.add_task(
        "Farm Invincible"
    ) is False

    assert storage.load_tasks() == [
        "Farm Invincible"
    ]


def test_delete_task_removes_definition(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    storage.add_task(
        "Farm Invincible"
    )

    assert (
        "Farm Invincible"
        in storage.load_tasks()
    )

    assert storage.delete_task(
        "Farm Invincible"
    ) is True

    assert (
        "Farm Invincible"
        not in storage.load_tasks()
    )


def test_delete_unknown_task_returns_false(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    assert storage.delete_task(
        "Unknown Task"
    ) is False


def test_multiple_tasks_are_sorted(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    storage.add_task("Zulu")
    storage.add_task("Bravo")
    storage.add_task("Alpha")

    assert storage.load_tasks() == [
        "Alpha",
        "Bravo",
        "Zulu",
    ]


def test_blank_task_rejected(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    assert storage.add_task("") is False

    assert storage.add_task("   ") is False

    assert storage.load_tasks() == []


def test_task_name_is_trimmed(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    storage.add_task(
        "   Farm Invincible   "
    )

    assert storage.load_tasks() == [
        "Farm Invincible"
    ]


def test_save_and_reload_tasks(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    storage.save_tasks([
        "Task B",
        "Task A",
    ])

    assert storage.load_tasks() == [
        "Task A",
        "Task B",
    ]


def test_delete_last_task_leaves_empty_list(
    tmp_path,
    monkeypatch
):

    task_file = tmp_path / "warband_tasks.txt"

    monkeypatch.setattr(
        storage,
        "TASK_FILE",
        task_file
    )

    storage.add_task("Farm Invincible")

    storage.delete_task(
        "Farm Invincible"
    )

    assert storage.load_tasks() == []