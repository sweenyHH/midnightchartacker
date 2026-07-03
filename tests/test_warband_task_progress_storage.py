from app.storage.warband_task_progress_storage import (
    load_progress,
    get_task_state,
    set_task_state,
)


def test_get_unknown_task_returns_false(tmp_path):

    file_path = tmp_path / "character.txt"

    file_path.write_text(
        "Test Character\n",
        encoding="utf-8"
    )

    class Character:
        source_file = str(file_path)

    char = Character()

    assert get_task_state(
        char,
        "Farm Invincible"
    ) is False


def test_set_task_state_true(tmp_path):

    file_path = tmp_path / "character.txt"

    file_path.write_text(
        "Test Character\n",
        encoding="utf-8"
    )

    class Character:
        source_file = str(file_path)

    char = Character()

    set_task_state(
        char,
        "Farm Invincible",
        True
    )

    assert get_task_state(
        char,
        "Farm Invincible"
    ) is True


def test_load_progress_multiple_tasks(tmp_path):

    file_path = tmp_path / "character.txt"

    file_path.write_text(
        """### USER_DATA_START ###
WarbandTasks:
Task A=true
Task B=true
### USER_DATA_END ###
""",
        encoding="utf-8"
    )

    class Character:
        source_file = str(file_path)

    char = Character()

    progress = load_progress(char)

    assert progress["Task A"] is True
    assert progress["Task B"] is True


def test_set_task_state_preserves_other_sections(tmp_path):

    file_path = tmp_path / "character.txt"

    file_path.write_text(
        """Character Data

### USER_DATA_START ###
Notes:
Hello World

WeeklyDuties:
0_0=1
### USER_DATA_END ###
""",
        encoding="utf-8"
    )

    class Character:
        source_file = str(file_path)

    char = Character()

    set_task_state(
        char,
        "Farm Invincible",
        True
    )

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "Notes:" in content
    assert "Hello World" in content
    assert "WeeklyDuties:" in content
    assert "0_0=1" in content
    assert "Farm Invincible=true" in content


def test_unchecking_task_removes_it(tmp_path):

    file_path = tmp_path / "character.txt"

    file_path.write_text(
        "Character Data\n",
        encoding="utf-8"
    )

    class Character:
        source_file = str(file_path)

    char = Character()

    set_task_state(
        char,
        "Farm Invincible",
        True
    )

    assert get_task_state(
        char,
        "Farm Invincible"
    ) is True

    set_task_state(
        char,
        "Farm Invincible",
        False
    )

    assert get_task_state(
        char,
        "Farm Invincible"
    ) is False

    content = file_path.read_text(
        encoding="utf-8"
    )

    assert "Farm Invincible=true" not in content

