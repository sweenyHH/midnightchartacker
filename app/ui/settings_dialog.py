from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QRadioButton,
    QPushButton,
    QHBoxLayout,
    QApplication,
    QButtonGroup,
)

from PySide6.QtCore import Signal

from app.storage.settings_storage import (
    load_setting,
    save_setting,
)
from app.utils.logger import logger, LOG_DIR
from app.ui.theme_manager import ThemeManager
import os
import platform
import subprocess
from app.localization.ui_strings import get_ui_string

class SettingsDialog(QDialog):

    settings_saved = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("settingsDialog")

        self.setWindowTitle(
            get_ui_string("settings")
        )
        self.resize(350, 250)

        layout = QVBoxLayout(self)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

        self.title_label = QLabel(get_ui_string("application_settings"))
        self.title_label.setObjectName("settingsTitle")
        layout.addWidget(self.title_label)

# --------------------------------------------------
# THEME
# --------------------------------------------------

        self.theme_label = QLabel(
            f"<b>{get_ui_string('theme')}</b>"
        )

        self.theme_label.setObjectName(
            "settingsSectionTitle"
        )

        layout.addWidget(
            self.theme_label
        )


        self.dark_radio = QRadioButton(
            get_ui_string("dark")
        )

        self.light_radio = QRadioButton(
            get_ui_string("light")
        )

        self.wow_radio = QRadioButton(
            get_ui_string("wow")
        )

        self.modern_radio = QRadioButton(
            get_ui_string("modern")
        )

        self.cherry_blossom_radio = QRadioButton(
            get_ui_string("cherry_blossom")
        )

        self.daddy_gamer_radio = QRadioButton(
            get_ui_string("daddy_gamer")
        )

        self.theme_group = QButtonGroup(self)

        self.theme_group.addButton(
            self.dark_radio
        )
        self.dark_radio.setObjectName("settingsRadioButton")

        self.theme_group.addButton(
            self.light_radio
        )
        self.light_radio.setObjectName("settingsRadioButton")

        self.theme_group.addButton(
            self.wow_radio
        )
        self.wow_radio.setObjectName("settingsRadioButton")

        self.theme_group.addButton(
            self.modern_radio
        )

        self.theme_group.addButton(
            self.cherry_blossom_radio
        )

        self.cherry_blossom_radio.setObjectName(
            "settingsRadioButton"
        )

        self.theme_group.addButton(
            self.daddy_gamer_radio
        )

        self.daddy_gamer_radio.setObjectName(
            "settingsRadioButton"
        )


        self.modern_radio.setObjectName("settingsRadioButton")

        layout.addWidget(self.dark_radio)
        layout.addWidget(self.light_radio)
        layout.addWidget(self.wow_radio)
        layout.addWidget(self.modern_radio)
        layout.addWidget(
            self.cherry_blossom_radio
        )

        layout.addWidget(
            self.daddy_gamer_radio
        )


# --------------------------------------------------
# Number Format
# --------------------------------------------------

        self.number_format_label = QLabel(
            f"<b>{get_ui_string('number_format')}</b>"
        )

        self.number_format_label.setObjectName(
            "settingsSectionTitle"
        )

        layout.addWidget(
            self.number_format_label
        )

        self.german_numbers = QRadioButton(
            get_ui_string(
                "number_format_german"
            )
        )
        self.german_numbers.setObjectName("settingsRadioButton")
        
        self.english_numbers = QRadioButton(
            get_ui_string(
                "number_format_english"
            )
        )
        self.english_numbers.setObjectName("settingsRadioButton")

        self.number_format_group = QButtonGroup(self)

        self.number_format_group.addButton(
            self.german_numbers
        )

        self.number_format_group.addButton(
            self.english_numbers
        )

        layout.addWidget(
            self.german_numbers
        )

        layout.addWidget(
            self.english_numbers
        )

# --------------------------------------------------
# Display Language
# --------------------------------------------------

        self.display_language_label = QLabel(
            f"<b>{get_ui_string('display_language')}</b>"
        )

        self.display_language_label.setObjectName(
            "settingsSectionTitle"
        )

        layout.addWidget(
            self.display_language_label
        )

        self.language_en = QRadioButton(
            get_ui_string("english")
        )
        self.language_en.setObjectName("settingsRadioButton")

        self.language_de = QRadioButton(
            get_ui_string("german")
        )
        self.language_de.setObjectName("settingsRadioButton")

        self.language_fr = QRadioButton(
            get_ui_string("french")
        )
        self.language_fr.setObjectName("settingsRadioButton")

        self.language_group = QButtonGroup(self)

        self.language_group.addButton(self.language_en)
        self.language_group.addButton(self.language_de)
        self.language_group.addButton(self.language_fr)

        layout.addWidget(self.language_en)
        layout.addWidget(self.language_de)
        layout.addWidget(self.language_fr)


# --------------------------------------------------
# LOGS
# --------------------------------------------------

        logs_button = QPushButton(
            get_ui_string(
                "open_log_folder"
            )
        )
        logs_button.setObjectName("settingsUtilityButton")
        logs_button.clicked.connect(
            self._open_log_folder
        )

        layout.addWidget(logs_button)

# --------------------------------------------------
# LOAD CURRENT THEME SETTING
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

        elif current_theme == "cherry_blossom":
            self.cherry_blossom_radio.setChecked(True)

        elif current_theme == "daddy_gamer":
            self.daddy_gamer_radio.setChecked(True)

# --------------------------------------------------
# LOAD NUMBER FORMAT
# --------------------------------------------------

        current_number_format = load_setting(
            "number_format",
            "german"
        )

        if current_number_format == "english":

            self.english_numbers.setChecked(
                True
            )

        else:

            self.german_numbers.setChecked(
                True
            )

# --------------------------------------------------
# LOAD DISPLAY LANGUAGE
# --------------------------------------------------

        current_language = load_setting(
            "display_language",
            "en"
        )

        if current_language == "de":

            self.language_de.setChecked(True)

        elif current_language == "fr":

            self.language_fr.setChecked(True)

        else:

            self.language_en.setChecked(True)



# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

        button_row = QHBoxLayout()

        save_button = QPushButton(
            get_ui_string("save")
        )
        save_button.setObjectName("settingsSaveButton")

        cancel_button = QPushButton(
            get_ui_string("cancel")
        )
        cancel_button.setObjectName("settingsCancelButton")

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
# OPEN LOG FOLDER
# --------------------------------------------------

    def _open_log_folder(self):

        log_path = str(LOG_DIR.resolve())

        try:

            logger.info(
                "Log folder opened"
            )

            system = platform.system()

            # -----------------------------
            # Windows
            # -----------------------------
            if system == "Windows":

                os.startfile(log_path)

            # -----------------------------
            # macOS
            # -----------------------------
            elif system == "Darwin":

                subprocess.Popen(
                    ["open", log_path]
                )

            # -----------------------------
            # Linux / WSL
            # -----------------------------
            else:

                # Detect WSL
                with open(
                    "/proc/version",
                    "r",
                    encoding="utf-8"
                ) as f:

                    version_info = f.read().lower()

                # WSL
                if "microsoft" in version_info:

                    subprocess.Popen(
                        ["explorer.exe", "."],
                        cwd=log_path
                    )

                # Native Linux
                else:

                    subprocess.Popen(
                        ["xdg-open", log_path]
                    )

        except Exception:

            logger.exception(
                "Failed to open log folder"
            )


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

        elif self.modern_radio.isChecked():
            theme = "modern"

        elif self.cherry_blossom_radio.isChecked():
            theme = "cherry_blossom"

        else:
            theme = "daddy_gamer"

        save_setting(
            "theme",
            theme
        )

        ThemeManager.load_theme(
            QApplication.instance(),
            theme
        )


        if self.english_numbers.isChecked():

            save_setting(
                "number_format",
                "english"
            )

        else:

            save_setting(
                "number_format",
                "german"
            )


        if self.language_de.isChecked():

            save_setting(
                "display_language",
                "de"
            )

        elif self.language_fr.isChecked():

            save_setting(
                "display_language",
                "fr"
            )

        else:

            save_setting(
                "display_language",
                "en"
            )

        self.settings_saved.emit()

        self.accept()