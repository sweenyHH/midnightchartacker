
# Entry point of the application. Initializes the Qt application, starts the main window.


import sys
import platform
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.ui.theme_manager import ThemeManager
from app.storage.settings_storage import load_setting
from app.utils.logger import logger
from app.app_info import (
    APP_NAME,
    APP_VERSION,
)
from PySide6.QtGui import QIcon
from app.utils.resource_path import resource_path


# --------------------------------------------------
# GLOBAL EXCEPTION HANDLER
# --------------------------------------------------

def log_uncaught_exception(exc_type, exc_value, exc_traceback):

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(
            exc_type,
            exc_value,
            exc_traceback
        )
        return

    logger.critical(
        "Unhandled exception",
        exc_info=(
            exc_type,
            exc_value,
            exc_traceback,
        ),
    )

    sys.__excepthook__(
        exc_type,
        exc_value,
        exc_traceback
    )



def main():

# registration of exception handler

    sys.excepthook = log_uncaught_exception    

# Create the Qt application instance

    app = QApplication(sys.argv)

    app.setWindowIcon(
        QIcon(
            str(
                resource_path(
                    "assets/icon.ico"
                )
            )
        )
    )

    

# start logging new session
    
    logger.info(
        "========================================"
    )
    logger.info(
        "New application session started"
    )

    logger.info(
        f"Application: {APP_NAME}"
    )

    logger.info(
        f"Version: {APP_VERSION}"
    )

    logger.info(
        f"Python: {platform.python_version()}"
    )

    logger.info(
        f"OS: {platform.platform()}"
    )

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