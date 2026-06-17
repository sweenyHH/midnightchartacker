
# Main application window. Handles navigation between overview and detail view.

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem
)
from app.services.data_service import DataService
from app.ui.detail_view import DetailView
from app.utils.watcher import FolderWatcher

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Midnight Character Tracker")

# Set fixed window size (width, height)

        self.setFixedSize(1800, 900)

# Sets DataService for data from the data_service.py

        self.data_service = DataService()

# Main layout container
        self.container = QWidget()
        self.layout = QVBoxLayout()

# Folder selection button
        self.select_button = QPushButton("Select Data Folder")
        self.select_button.clicked.connect(self.select_folder)

# Character overview table

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Character",
            "Class:",
            "Average Item Level:",
            "Level",
            "Specialization:"
             ])
        self.table.cellClicked.connect(self.open_character)

# Enable sorting 

        self.table.setSortingEnabled(True)

# Detail view 

        self.detail_view = DetailView()
        self.detail_view.hide()

# Back button for navigation

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.show_list)
        self.back_button.hide()

# Layout structure

        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.detail_view)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.watcher = None

    def select_folder(self):
  
# Opens a dialog for selecting the data folder.
  
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder:
            self.data_service.set_folder(folder)
            self.reload_list()
            self.start_watcher(folder)

    def reload_list(self):
  
# Reloads the overview table of characters.
  
        characters = self.data_service.get_characters()

        self.table.setRowCount(len(characters))

        for row, char in enumerate(characters):

# Column 1: Character name

            name_item = QTableWidgetItem(char.name)
            self.table.setItem(row, 0, name_item)

# Helper function to safely access values

            def get_value(key):
                return char.location.get(key, "-")

# Column 2: Class

            class_item = QTableWidgetItem(get_value("Class"))
            self.table.setItem(row, 1, class_item)

# Column 3: Average Item Level

            ilvl_item = QTableWidgetItem(get_value("Average Item Level"))
            self.table.setItem(row, 2, ilvl_item)

# Column 4: Level

            level_item = QTableWidgetItem(get_value("Level"))
            self.table.setItem(row, 3, level_item)

# Column 5: Specialization

            spec_item = QTableWidgetItem(get_value("Specialization"))
            self.table.setItem(row, 4, spec_item)


# Resize columns automatically (better layout)

        self.table.resizeColumnsToContents()

    def open_character(self, row, column):

# Opens detail view for selected character based on clicked row.

        character = self.data_service.get_characters()[row]

        self.detail_view.set_character(character)

        self.table.hide()
        self.back_button.show()
        self.detail_view.show()

    def show_list(self):
  
# Returns to the overview table.
  
        self.detail_view.hide()
        self.back_button.hide()
        self.table.show()

    def start_watcher(self, folder):
 
# Starts file system watcher for auto-updates.
 
        if self.watcher:
            self.watcher.stop()

        self.watcher = FolderWatcher(folder, self.on_files_changed)
        self.watcher.start()

    def on_files_changed(self):
 
# Called when files change -> reload data.
  
        self.data_service.load_data()
        self.reload_list()