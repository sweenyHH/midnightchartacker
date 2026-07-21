
from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QMenu,
    QCheckBox,
    QWidget,
    QHBoxLayout,
)

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor

from app.ui.colors import CLASS_COLORS

from .character_table_helpers import (
    NumericItem,
    format_vault_values,
    get_attr,
    get_character_currency_by_key,
    adjust_class_color,
    shorten_task_name,
)

from app.storage.vault_storage import load_user_vault
from app.storage.warband_task_storage import load_tasks

from app.storage.warband_task_progress_storage import (
    get_task_state,
    set_task_state,
)
from app.localization.ui_strings import get_ui_string

from app.utils.logger import logger

class CharacterTable(QTableWidget):

    character_delete_requested = Signal(object)

    def __init__(self):
        super().__init__()
        
        self.setObjectName("characterTable")
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(
        self._show_context_menu
        )

    def load_characters(self, characters):

        logger.info(
            f"Loading character table with "
            f"{len(characters)} characters"
        )

        tasks = load_tasks()

        task_headers = [
            shorten_task_name(task)
            for task in tasks
        ]

        headers = [
            get_ui_string("character"),
            get_ui_string("class"),
            get_ui_string("item_level"),
            get_ui_string("level"),
            get_ui_string("specialization"),
            get_ui_string("coffer_keys"),
            get_ui_string("radiant_spark_dust"),
            get_ui_string("raid"),
            get_ui_string("mythic_plus"),
            get_ui_string("delves"),
        ]

        headers.extend(task_headers)


        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        
        for task_index, task_name in enumerate(tasks):

            column = 10 + task_index

            header_item = self.horizontalHeaderItem(column)

            if header_item:
                header_item.setToolTip(task_name)

        self.setSortingEnabled(False)
        self.clearContents()
        self.setRowCount(len(characters))

        self.verticalHeader().setDefaultSectionSize(34)

        for row, char in enumerate(characters):

            logger.info(
                f"Character table row loaded: "
                f"{char.name}"
            )
       
# -------------------------------
# Name
# -------------------------------
            name_item = QTableWidgetItem(char.name)
            name_item.setData(Qt.UserRole, char)

            if char.faction == "Alliance":
                name_item.setForeground(QColor("#4aa3ff"))
            elif char.faction == "Horde":
                name_item.setForeground(QColor("#ff4a4a"))

            font = name_item.font()
            font.setBold(True)
            name_item.setFont(font)

            self.setItem(row, 0, name_item)

# -------------------------------
# Class
# -------------------------------
            class_name = get_attr(char, "character_class")

            class_item = QTableWidgetItem(class_name)

            if class_name in CLASS_COLORS:
                adjusted = adjust_class_color(CLASS_COLORS[class_name])
                class_item.setForeground(QColor(adjusted))

            self.setItem(row, 1, class_item)

# -------------------------------
# Item Level
# -------------------------------
            ilvl_raw = getattr(char, "avg_item_level", None)

            try:
                ilvl_value = int(ilvl_raw)
            except (TypeError, ValueError):
                ilvl_value = 0

            ilvl_item = NumericItem(
                str(ilvl_raw) if ilvl_raw is not None else "-",
                ilvl_value
            )

            self.setItem(row, 2, ilvl_item)

# -------------------------------
# Level / Specialization
# -------------------------------
            self.setItem(
                row,
                3,
                QTableWidgetItem(get_attr(char, "level"))
            )

            self.setItem(
                row,
                4,
                QTableWidgetItem(get_attr(char, "specialization"))
            )

# -------------------------------
# Vault
# -------------------------------
            vault = load_user_vault(char)

            def has_value(values):
                return any(v for v in values if str(v).strip())

            raid_values = vault.get("row1", [])
            mplus_values = vault.get("row2", [])
            delve_values = vault.get("row3", [])

            raid_sort = 1 if has_value(raid_values) else 0
            mplus_sort = 1 if has_value(mplus_values) else 0
            delve_sort = 1 if has_value(delve_values) else 0

            raid_item = NumericItem(
                format_vault_values(raid_values),
                raid_sort
            )

            mplus_item = NumericItem(
                format_vault_values(mplus_values),
                mplus_sort
            )

            delve_item = NumericItem(
                format_vault_values(delve_values),
                delve_sort
            )

            self.setItem(row, 7, raid_item)
            self.setItem(row, 8, mplus_item)
            self.setItem(row, 9, delve_item)

# -------------------------------
# Warband Tasks
# -------------------------------

            task_start_col = 10

            for task_index, task_name in enumerate(tasks):

                checkbox = QCheckBox()
                checkbox.setObjectName("taskCheckbox")

                initial_state = get_task_state(
                    char,
                    task_name
                )

                checkbox.setChecked(initial_state)

                def on_state_changed(
                    state,
                    character=char,
                    task=task_name
                ):
                    checked = state != 0

                    set_task_state(
                        character,
                        task,
                        checked
                    )

                checkbox.stateChanged.connect(
                    on_state_changed
                )

                container = QWidget()
                container.setObjectName("taskCheckboxContainer")
                container.setStyleSheet("background: transparent;")

                layout = QHBoxLayout(container)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setAlignment(Qt.AlignCenter)

                layout.addWidget(checkbox)

                self.setCellWidget(
                    row,
                    task_start_col + task_index,
                    container
                )

# -------------------------------
# Coffer Keys
# -------------------------------

            coffer = get_character_currency_by_key(
                char,
                "restored_coffer_key"
            )

            coffer_value = coffer.quantity if coffer else 0

            coffer_item = NumericItem(
                str(coffer_value),
                coffer_value
            )

            self.setItem(row, 5, coffer_item)

# -------------------------------
# Spark Dust
# -------------------------------

            spark = get_character_currency_by_key(
                char,
                "radiant_spark_dust"
            )

            if spark:
                value = (
                    f"{spark.quantity}/{spark.max_total}"
                    if spark.max_total
                    else str(spark.quantity)
                )
                sort_value = spark.quantity
            else:
                value = "-"
                sort_value = 0

            spark_item = NumericItem(
                value,
                sort_value
            )

            self.setItem(row, 6, spark_item)

        self.resizeColumnsToContents()
        self.setSortingEnabled(True)

# Sort by Item Level descending

        self.sortItems(2, Qt.DescendingOrder)

# --------------------------------------------------
# CONTEXT MENU
# --------------------------------------------------

    def _show_context_menu(self, position):

        item = self.itemAt(position)

        if not item:
            return

        char_item = self.item(item.row(), 0)

        if not char_item:
            return

        character = char_item.data(Qt.UserRole)

        if not character:
            return

        menu = QMenu(self)

        delete_action = menu.addAction(
            get_ui_string(
                "delete_character_menu"
            ).format(
                name=character.name
            )
        )

        action = menu.exec(
            self.viewport().mapToGlobal(position)
        )

        if action == delete_action:

            logger.info(
                f"Delete requested for "
                f"{character.name}"
            )

            self.character_delete_requested.emit(character)