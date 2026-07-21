from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtCore import QTimer
import os

from app.utils.logger import logger

from app.storage.user_data_storage import (
    load_section,
    save_section,
)
from app.localization.ui_strings import get_ui_string



class NotesWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

# spacing
        self.layout.setSpacing(8)

        self.layout.addWidget(
            QLabel(
                f"<b>{get_ui_string('notes')}</b>"
            )
        )

        self.textbox = QTextEdit()

# disable rich text
        self.textbox.setAcceptRichText(False)

        self.textbox.setPlaceholderText(
            get_ui_string(
                "notes_placeholder"
            )
        )

        self.layout.addWidget(self.textbox)

        self.textbox.textChanged.connect(self._limit_length)
        
        self.save_timer = QTimer()
        self.save_timer.setSingleShot(True)
        self.save_timer.timeout.connect(self._save_notes)

        self.textbox.textChanged.connect(self._schedule_save)


        self.current_file = None

# --------------------------------------------------
# SET CHARACTER
# --------------------------------------------------
    def set_character(self, character):

        logger.info(
            f"Notes loaded for: "
            f"{character.name}"
        )

        self.current_file = character.source_file

        
        new_text = self._load_notes(self.current_file)

        if new_text != self.textbox.toPlainText():
            self.textbox.blockSignals(True)
            self.textbox.setPlainText(new_text)
            self.textbox.blockSignals(False)

# --------------------------------------------------
# LOAD NOTES (FROM USER BLOCK)
# --------------------------------------------------

    def _load_notes(self, file_path):

        lines = load_section(
            file_path,
            "Notes"
        )

        return "\n".join(lines).strip()


# --------------------------------------------------
# SAVE NOTES (MERGE SAFE)
# --------------------------------------------------

    def _schedule_save(self):

        self.save_timer.start(1000)

    def _save_notes(self):

        if not self.current_file:

            logger.warning(
                "Notes save skipped: "
                "no character loaded"
            )

            return

        text = self.textbox.toPlainText().strip()

        note_lines = []

        if text:
            note_lines = text.splitlines()

        try:

            save_section(
                self.current_file,
                "Notes",
                note_lines
            )

            logger.info(
                f"Notes saved: "
                f"{os.path.basename(self.current_file)}"
            )

        except Exception:

            logger.exception(
                "Failed to save notes"
            )

            raise

# --------------------------------------------------
# LIMIT LENGTH
# --------------------------------------------------
    def _limit_length(self):

        text = self.textbox.toPlainText()

        if len(text) > 512:
            self.textbox.blockSignals(True)
            self.textbox.setPlainText(text[:512])

            cursor = self.textbox.textCursor()
            cursor.setPosition(len(text[:512]))
            self.textbox.setTextCursor(cursor)

            self.textbox.blockSignals(False)