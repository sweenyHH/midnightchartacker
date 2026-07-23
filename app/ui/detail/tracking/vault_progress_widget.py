from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QGridLayout, QLineEdit, QPushButton, QFrame
)
from PySide6.QtCore import Qt, QTimer
import os

from app.utils.logger import logger

from app.storage.user_data_storage import (
    load_section,
    save_section,
)
from app.localization.ui_strings import (
    get_ui_string,
)




class VaultProgressWidget(QFrame):

    def __init__(self):
        super().__init__()

      
        self.setObjectName("vaultProgressWidget")
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.title_label = QLabel(f"<b>{get_ui_string('vault_progress')}</b>")
        self.title_label.setObjectName("overviewSectionTitle")
        self.layout.addWidget(self.title_label)
        self.layout.addSpacing(8)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)
        self.layout.addStretch()

        self.fields = {}  # (row, col) → QLineEdit

        row_labels = [
            get_ui_string("raid_slots"),
            get_ui_string("mplus_slots"),
            get_ui_string("delve_slots"),
        ]

        for row in range(3):
            label = QLabel(row_labels[row])

            label.setObjectName(
                "vaultProgressRowLabel"
            )
            self.grid.addWidget(label, row, 0)

            for col in range(3):
                field = QLineEdit()
                field.setObjectName("vaultProgressField")
                field.setMaximumWidth(60)
                field.setPlaceholderText("...")
                field.setAlignment(Qt.AlignCenter)
                field.setMaxLength(3)

                field.textChanged.connect(self._save)

                self.grid.addWidget(field, row, col + 1)
                self.fields[(row, col)] = field

        self.grid.setColumnStretch(0, 2)
        self.grid.setColumnStretch(4, 1)

# Clear button
        self.clear_btn = QPushButton(get_ui_string("clear_all"))
        self.clear_btn.setObjectName("vaultClearButton")
        self.clear_btn.clicked.connect(self.clear_all)
        self.layout.addWidget(self.clear_btn)

        self.current_file = None
        self.on_save_callback = None

# --------------------------------------------------
    def set_character(self, character):

        logger.info(
            f"Vault progress loaded for: "
            f"{character.name}"
        )

        self.current_file = character.source_file

        data = self._load()

        for (row, col), field in self.fields.items():
            key = f"{row}_{col}"
            field.blockSignals(True)
            field.setText(data.get(key, ""))
            field.blockSignals(False)

# --------------------------------------------------
    def clear_all(self):

        logger.info(
            f"Vault progress cleared: "
            f"{os.path.basename(self.current_file)}"
        )

        for field in self.fields.values():
            field.setText("")

        self._save()

# --------------------------------------------------
# LOAD (USER BLOCK)
# --------------------------------------------------
    def _load(self):

        result = {}

        try:

            lines = load_section(
                self.current_file,
                "Vault"
            )

        except Exception:

            logger.exception(
                f"Failed to load vault progress: "
                f"{self.current_file}"
            )

            raise

        for stripped in lines:

            if "=" not in stripped:
                continue

            k, v = stripped.split("=")
            result[k] = v

        return result
   

# --------------------------------------------------
# SAVE (MERGE SAFE)
# --------------------------------------------------
    def _save(self):

        if not self.current_file:

            logger.warning(
                "Vault progress save skipped: "
                "no character loaded"
            )

            return

        vault_lines = []

        for (row, col), field in self.fields.items():

            value = field.text().strip()

            if value:
                vault_lines.append(f"{row}_{col}={value}")

        try:

            save_section(
                self.current_file,
                "Vault",
                vault_lines
            )

            logger.info(
                f"Vault progress saved: "
                f"{os.path.basename(self.current_file)}"
            )

            if self.on_save_callback:
                self.on_save_callback()

        except Exception:

            logger.exception(
                f"Failed to save vault progress: "
                f"{self.current_file}"
            )

            raise


 