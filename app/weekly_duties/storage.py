import os


def load_state(file_path):
    result = {}

    if not file_path or not os.path.exists(file_path):
        return result

    in_user_block = False
    in_section = False

    with open(file_path, encoding="utf-8") as f:
        for line in f:

            stripped = line.strip()

            if stripped == "### USER_DATA_START ###":
                in_user_block = True
                continue

            if stripped == "### USER_DATA_END ###":
                break

            if in_user_block and stripped == "WeeklyDuties:":
                in_section = True
                continue

            if in_section:
                if "=" in stripped:
                    k, v = stripped.split("=")
                    result[k] = (v == "1")
                elif stripped.endswith(":"):
                    break

    return result


def save_state(file_path, checkboxes):

    if not file_path or not os.path.exists(file_path):
        return

    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    in_user_block = False
    notes_lines = []
    new_lines = []

    for line in lines:

        stripped = line.strip()

        if stripped == "### USER_DATA_START ###":
            in_user_block = True
            continue

        if stripped == "### USER_DATA_END ###":
            in_user_block = False
            continue

        if in_user_block:
            if stripped.startswith("Notes:") or notes_lines:
                notes_lines.append(line)
                continue

            if stripped.startswith("WeeklyDuties:") or "=" in stripped:
                continue

        else:
            new_lines.append(line)

    duty_lines = []

    for row_index, boxes in checkboxes:
        for i, cb in enumerate(boxes):
            if cb.isChecked():
                duty_lines.append(f"{row_index}_{i}=1\n")

    user_block = []

    if notes_lines or duty_lines:
        user_block.append("### USER_DATA_START ###\n")

        if notes_lines:
            user_block.extend(notes_lines)

        if duty_lines:
            user_block.append("WeeklyDuties:\n")
            user_block.extend(duty_lines)

        user_block.append("### USER_DATA_END ###\n")

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

        if user_block:
            f.write("\n")
            f.writelines(user_block)