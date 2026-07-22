from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox,
)

from app.storage.warband_task_storage import (
    load_tasks,
    add_task,
    delete_task,
)
from app.localization.ui_strings import get_ui_string
from app.utils.logger import logger

class WarbandTaskDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("warbandTaskDialog")

        self.setWindowTitle(
            get_ui_string(
                "warband_tasks"
            )
        )
        self.resize(450, 400)

        layout = QVBoxLayout(self)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
        title = QLabel(
            get_ui_string(
                "warband_tasks"
            )
        )
        title.setObjectName("warbandTaskTitle")

        layout.addWidget(title)

# --------------------------------------------------
# TASK LIST
# --------------------------------------------------
        self.task_list = QListWidget()
        self.task_list.setObjectName("warbandTaskList")

        layout.addWidget(self.task_list)

# --------------------------------------------------
# INPUT ROW
# --------------------------------------------------
        input_layout = QHBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setObjectName("warbandTaskInput")
        self.task_input.setPlaceholderText(
            get_ui_string(
                "new_task_name"
            )
        )

        add_btn = QPushButton(get_ui_string("add"))
        add_btn.setObjectName("warbandTaskAddButton")
        add_btn.clicked.connect(self.add_task)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_btn)

        layout.addLayout(input_layout)

# --------------------------------------------------
# BUTTON ROW
# --------------------------------------------------
        button_layout = QHBoxLayout()

        delete_btn = QPushButton(get_ui_string("delete_selected"))
        delete_btn.setObjectName("warbandTaskDeleteButton")
        delete_btn.clicked.connect(self.delete_selected)

        close_btn = QPushButton(get_ui_string("close"))
        close_btn.setObjectName("warbandTaskCloseButton")
        close_btn.clicked.connect(self.accept)

        button_layout.addWidget(delete_btn)
        button_layout.addStretch()
        button_layout.addWidget(close_btn)

        layout.addLayout(button_layout)

# --------------------------------------------------
# INITIAL LOAD
# --------------------------------------------------
        self.reload_tasks()

# --------------------------------------------------
# LOAD
# --------------------------------------------------
    def reload_tasks(self):

        tasks = load_tasks()

        logger.info(
            f"Loaded {len(tasks)} warband tasks"
        )

        self.task_list.clear()

        for task in tasks:
            self.task_list.addItem(task)


# --------------------------------------------------
# ADD
# --------------------------------------------------
    def add_task(self):

        task_name = self.task_input.text().strip()

        if not task_name:

            logger.warning(
                "Attempted to create empty warband task"
            )

            return

        if not add_task(task_name):

            logger.warning(
                f"Duplicate warband task: "
                f"{task_name}"
            )

            QMessageBox.warning(
                self,
                get_ui_string(
                    "task_exists"
                ),
                get_ui_string(
                    "task_already_exists"
                ).format(
                    name=task_name
                ),
            )
            return

        logger.info(
            f"Warband task created: "
            f"{task_name}"
        )

        self.task_input.clear()
        self.reload_tasks()

# --------------------------------------------------
# DELETE
# --------------------------------------------------
    def delete_selected(self):

        item = self.task_list.currentItem()

        if not item:

            logger.warning(
                "Delete task requested with no selection"
            )

            return

        task_name = item.text()

        result = QMessageBox.question(
            self,
            get_ui_string(
                "delete_task"
            ),
            get_ui_string(
                "delete_task_confirmation"
            ).format(
                name=task_name
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if result != QMessageBox.Yes:

            logger.info(
                f"Task deletion cancelled: "
                f"{task_name}"
            )

            return

        logger.info(
            f"Warband task deleted: "
            f"{task_name}"
        )


        delete_task(task_name)
        self.reload_tasks()