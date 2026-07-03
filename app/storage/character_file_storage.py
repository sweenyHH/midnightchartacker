from pathlib import Path


def delete_character_file(character):

    file_path = getattr(
        character,
        "source_file",
        None
    )

    if not file_path:
        return False

    path = Path(file_path)

    if not path.exists():
        return False

    path.unlink()

    return True