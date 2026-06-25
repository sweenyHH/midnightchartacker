from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QHBoxLayout, QGridLayout
)
from PySide6.QtCore import Qt


class TopPanel(QWidget):

    def __init__(self, select_cb, paste_cb, back_cb):
        super().__init__()

        main_layout = QVBoxLayout(self)

# --------------------------------------------------
# ROW 1 — BUTTONS (HORIZONTAL)
# --------------------------------------------------

        button_row = QHBoxLayout()

        self.select_btn = QPushButton("Select Data Folder")
        self.select_btn.clicked.connect(select_cb)

        self.paste_btn = QPushButton("Paste Character Data")
        self.paste_btn.clicked.connect(paste_cb)

        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(back_cb)
        self.back_btn.hide()

        button_row.addWidget(self.select_btn)
        button_row.addWidget(self.paste_btn)
        button_row.addWidget(self.back_btn)
        button_row.addStretch()

        main_layout.addLayout(button_row)

# --------------------------------------------------
# ROW 2 — REPUTATION GRID
# --------------------------------------------------

        self.rep_container = QWidget()
        self.rep_layout = QVBoxLayout(self.rep_container)

        main_layout.addWidget(self.rep_container)

# --------------------------------------------------
# UPDATE METHOD
# --------------------------------------------------

    def update_reputation(self, reputation_list):

        # Clear previous content
        while self.rep_layout.count():
            item = self.rep_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if not reputation_list:
            self.rep_layout.addWidget(QLabel("No reputation data available"))
            return

        # Split data
        renown = [r for r in reputation_list if r.rep_type == "renown"]
        normal = [r for r in reputation_list if r.rep_type != "renown"]

        renown.sort(key=lambda r: r.name)
        normal.sort(key=lambda r: r.name)

        # Helper: chunk list into groups of 3
        def chunk(lst, size=3):
            return [lst[i:i + size] for i in range(0, len(lst), size)]

        renown_chunks = chunk(renown)
        normal_chunks = chunk(normal)

        # --------------------------------------------------
        # MAIN ROW (RENOWN | STANDARD)
        # --------------------------------------------------

        main_row = QHBoxLayout()

        # --------------------------------------------------
        # RENOWN BLOCK
        # --------------------------------------------------

        renown_widget = QWidget()
        renown_layout = QVBoxLayout(renown_widget)

        renown_title = QLabel("Renown:")
        renown_title.setAlignment(Qt.AlignLeft)
        renown_layout.addWidget(renown_title)

        renown_grid = QGridLayout()

        def add_group_to_grid(rep_group, col_offset):
            for row, rep in enumerate(rep_group):
                name = QLabel(rep.name)
                value = QLabel(str(rep.level))

                renown_grid.addWidget(name, row, col_offset)
                renown_grid.addWidget(value, row, col_offset + 1)

        # max 2 groups (left + right)
        for i, group in enumerate(renown_chunks[:2]):
            add_group_to_grid(group, col_offset=i * 2)

        renown_layout.addLayout(renown_grid)

        # --------------------------------------------------
        # STANDARD BLOCK
        # --------------------------------------------------

        normal_widget = QWidget()
        normal_layout = QVBoxLayout(normal_widget)

        normal_title = QLabel("Standard:")
        normal_title.setAlignment(Qt.AlignLeft)
        normal_layout.addWidget(normal_title)

        normal_grid = QGridLayout()

        def add_standard_group(rep_group, col_offset):
            for row, rep in enumerate(rep_group):

                name = QLabel(rep.name)

                if rep.current and rep.maximum:
                    value = QLabel(f"{rep.level} ({rep.current}/{rep.maximum})")
                else:
                    value = QLabel(str(rep.level))

                normal_grid.addWidget(name, row, col_offset)
                normal_grid.addWidget(value, row, col_offset + 1)

        for i, group in enumerate(normal_chunks[:2]):
            add_standard_group(group, col_offset=i * 2)

        normal_layout.addLayout(normal_grid)

        # --------------------------------------------------
        # ADD BOTH BLOCKS SIDE BY SIDE
        # --------------------------------------------------

        main_row.addWidget(renown_widget)
        main_row.addWidget(normal_widget)
        main_row.setStretch(0, 1)
        main_row.setStretch(1, 1)

        self.rep_layout.addLayout(main_row)
