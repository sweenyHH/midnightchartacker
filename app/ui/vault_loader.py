import os


def load_user_vault(character):

    vault = getattr(
        character,
        "vault",
        {"row1": [], "row2": [], "row3": []}
    )

    user_vault = {
        "row1": [],
        "row2": [],
        "row3": []
    }

    file_path = getattr(character, "source_file", None)

    if not file_path or not os.path.exists(file_path):
        return vault

    in_user_block = False
    in_vault = False

    with open(file_path, encoding="utf-8") as f:

        for line in f:
            stripped = line.strip()

            if stripped == "### USER_DATA_START ###":
                in_user_block = True
                continue

            if stripped == "### USER_DATA_END ###":
                break

            if in_user_block and stripped == "Vault:":
                in_vault = True
                continue

            if in_vault:

                if "=" in stripped:

                    key, value = stripped.split("=")

                    row_idx, col_idx = key.split("_")
                    row_name = f"row{int(row_idx) + 1}"

                    while len(user_vault[row_name]) <= int(col_idx):
                        user_vault[row_name].append(None)

                    user_vault[row_name][int(col_idx)] = value

                elif stripped.endswith(":"):
                    break

    if any(user_vault[r] for r in user_vault):
        return user_vault

    return vault