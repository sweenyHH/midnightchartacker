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


