from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from app.ui.detail.tracking.notes_widget import NotesWidget
from app.ui.detail.tracking.weekly_duties_widget import WeeklyDutiesWidget
from app.ui.detail.tracking.vault_progress_widget import VaultProgressWidget
from app.utils.logger import logger


class TrackingTab(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("trackingTab")

# MAIN LAYOUT (persistent)
        self.layout = QVBoxLayout(self)

# CREATE WIDGETS
        self.notes_widget = NotesWidget()
        self.duties_widget = WeeklyDutiesWidget()
        self.vault_widget = VaultProgressWidget()


# --------------------------------------------------
# PERMANENT LAYOUTS
# --------------------------------------------------

        self.main_row = QHBoxLayout()

        self.left_column_widget = QWidget()
        self.left_column_widget.setObjectName("trackingColumn")
        self.left_column = QVBoxLayout(self.left_column_widget)

        self.right_column_widget = QWidget()
        self.right_column_widget.setObjectName("trackingColumn")
        self.right_column = QVBoxLayout(self.right_column_widget)

        self.left_column.addWidget(
            self.notes_widget,
            5
        )

        self.left_column.addSpacing(
            12
        )

        self.left_column.addWidget(
            self.vault_widget,
            4
        )


        self.right_column.addWidget(
            self.duties_widget
        )

        self.main_row.addWidget(
            self.left_column_widget,
            2
        )


        self.main_row.addWidget(
            self.right_column_widget,
            3
        )

        self.layout.addLayout(
            self.main_row
        )


# --------------------------------------------------
    def set_character(self, character):

        logger.info(
            f"TrackingTab set_character: {character.name}"
        )

        self.notes_widget.set_character(
            character
        )

        self.vault_widget.set_character(
            character
        )

# REUSE DUTIES WIDGET
        self.duties_widget.set_character(character)

