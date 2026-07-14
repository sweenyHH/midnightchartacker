from app.utils.app_paths import get_data_dir
from app.storage.warband_task_progress_storage import remove_task_from_all_characters

TASK_FILE = get_data_dir() / "warband_tasks.txt"

def load_tasks():
    
# Return all warband task names.

    if not TASK_FILE.exists():
        return []

    with open(TASK_FILE, encoding="utf-8") as f:
        tasks = [
            line.strip()
            for line in f
            if line.strip()
        ]

    return sorted(tasks)


def save_tasks(tasks):

# Save complete task list.


    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in sorted(tasks):
            f.write(f"{task}\n")


def add_task(task_name):

# Add a task if it does not already exist.

    task_name = task_name.strip()

    if not task_name:
        return False

    tasks = load_tasks()

    if task_name in tasks:
        return False

    tasks.append(task_name)

    save_tasks(tasks)

    return True


def delete_task(task_name):

# Remove a task and all associated progress.

    tasks = load_tasks()

    if task_name not in tasks:
        return False

    tasks.remove(task_name)

    save_tasks(tasks)

    remove_task_from_all_characters(
        task_name
    )

    return True