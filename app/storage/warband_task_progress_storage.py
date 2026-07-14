from pathlib import Path
from app.utils.app_paths import get_import_dir
from app.utils.logger import logger

from app.storage.user_data_storage import (
    load_section,
    save_section,
)

SECTION_NAME = "WarbandTasks"


def load_progress(character):

    result = {}

    lines = load_section(
        character.source_file,
        SECTION_NAME
    )

    for line in lines:

        if "=" not in line:
            continue

        task_name, value = line.split("=", 1)

        result[task_name] = (
            value.strip().lower() == "true"
        )

    return result


def save_progress(character, progress):

    lines = []

    for task_name in sorted(progress):

        if progress[task_name] == True:

            lines.append(
                f"{task_name}=true"
            )

    save_section(
        character.source_file,
        SECTION_NAME,
        lines
    )

def get_task_state(character, task_name):

    progress = load_progress(character)

    return progress.get(task_name, False)

  
def set_task_state(
    character,
    task_name,
    completed,
):

    progress = load_progress(character)
    progress[task_name] = completed
    save_progress(
        character,
        progress,
    )

def remove_task_from_all_characters(task_name):
    """
    Removes a deleted warband task from all
    character progress files.
    """

    affected_characters = 0

    for file_path in get_import_dir().glob("*.txt"):

        class CharacterRef:

            def __init__(self, source_file):
                self.source_file = source_file

        character = CharacterRef(
            str(file_path)
        )

        progress = load_progress(character)

        if task_name not in progress:
            continue

        del progress[task_name]

        save_progress(
            character,
            progress,
        )

        affected_characters += 1

    logger.info(
        f"Removed task '{task_name}' "
        f"from {affected_characters} "
        f"character files"
    )

    return affected_characters
