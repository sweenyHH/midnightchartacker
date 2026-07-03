from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QRadioButton,
    QPushButton,
    QHBoxLayout,
    QApplication,
)

from app.storage.settings_storage import (
    load_setting,
    save_setting,
)

from app.ui.theme_manager import ThemeManager


class SettingsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        self.resize(350, 250)

        layout = QVBoxLayout(self)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

        title = QLabel("Application Settings")
        title.setObjectName("settingsTitle")

        layout.addWidget(title)

# --------------------------------------------------
# THEME
# --------------------------------------------------

        layout.addWidget(QLabel("<b>Theme</b>"))

        self.dark_radio = QRadioButton("Dark")
        self.light_radio = QRadioButton("Light")
        self.wow_radio = QRadioButton("WoW")
        self.modern_radio = QRadioButton("Modern")

        layout.addWidget(self.dark_radio)
        layout.addWidget(self.light_radio)
        layout.addWidget(self.wow_radio)
        layout.addWidget(self.modern_radio)

# --------------------------------------------------
# LOAD CURRENT SETTING
# --------------------------------------------------

        current_theme = load_setting(
            "theme",
            "dark"
        )

        if current_theme == "dark":
            self.dark_radio.setChecked(True)

        elif current_theme == "light":
            self.light_radio.setChecked(True)

        elif current_theme == "wow":
            self.wow_radio.setChecked(True)

        elif current_theme == "modern":
            self.modern_radio.setChecked(True)

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

        button_row = QHBoxLayout()

        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")

        save_button.clicked.connect(
            self._save_settings
        )

        cancel_button.clicked.connect(
            self.reject
        )

        button_row.addStretch()
        button_row.addWidget(save_button)
        button_row.addWidget(cancel_button)

        layout.addStretch()
        layout.addLayout(button_row)

# --------------------------------------------------
# SAVE
# --------------------------------------------------

    def _save_settings(self):

        if self.dark_radio.isChecked():
            theme = "dark"

        elif self.light_radio.isChecked():
            theme = "light"

        elif self.wow_radio.isChecked():
            theme = "wow"

        else:
            theme = "modern"

        save_setting(
            "theme",
            theme
        )

        ThemeManager.load_theme(
            QApplication.instance(),
            theme
        )

        self.accept()