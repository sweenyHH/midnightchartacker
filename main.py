
# Entry point of the application. Initializes the Qt application, starts the main window.


import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.ui.theme_manager import ThemeManager
from app.storage.settings_storage import load_setting


def main():

# Create the Qt application instance

    app = QApplication(sys.argv)


# Load saved theme

    theme = load_setting(
        "theme",
        "dark"
    )

    ThemeManager.load_theme(
        app,
        theme
    )


# Create and show main window

    window = MainWindow()
    window.show()

# Start application event loop

    sys.exit(app.exec())

if __name__ == "__main__":
    main()