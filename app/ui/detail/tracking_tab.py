from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from app.ui.detail.notes_widget import NotesWidget
from app.weekly_duties.widget import WeeklyDutiesWidget
from app.ui.detail.vault_progress import VaultProgressWidget
from app.utils.logger import logger


class TrackingTab(QWidget):

    def __init__(self):
        super().__init__()

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

        self.left_column = QVBoxLayout()
        self.right_column = QVBoxLayout()

        self.left_column.addWidget(
            self.notes_widget
        )

        self.left_column.addWidget(
            self.vault_widget
        )

        self.right_column.addWidget(
            self.duties_widget
        )

        self.main_row.addLayout(
            self.left_column,
            2
        )

        self.main_row.addLayout(
            self.right_column,
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

