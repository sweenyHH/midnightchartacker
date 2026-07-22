from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QFrame,
)
from PySide6.QtCore import Qt

from app.localization.ui_strings import get_ui_string
from app.ui.detail.overview.raid_progress_helper import build_raid_progress_rows
from app.game_data.raid_catalog import get_raid_display_name
from app.services.display_language import get_display_language


class RaidProgressWidget(QFrame):


    def __init__(self):
        super().__init__()

        self.setObjectName(
            "overviewTile"
        )

        self.setProperty(
            "overviewType",
            "raidProgress"
        )

        self.setFrameShape(
            QFrame.Box
        )

        layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setObjectName("raidProgressTable")
        self.table.setColumnCount(5)
        self.table.verticalHeader().setVisible(False)

        self.table.setHorizontalHeaderLabels(
            [
                get_ui_string("instance"),
                get_ui_string("lfr"),
                get_ui_string("normal"),
                get_ui_string("heroic"),
                get_ui_string("mythic"),
            ]
        )

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch,
        )

        for column in (1, 2, 3, 4):

            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeToContents,
            )

        layout.addWidget(
            self.table
        )

    def set_character(self, character):

        #self.title_label.setText(get_ui_string("raid_progress"))
        rows = (build_raid_progress_rows(character))
        self.table.setRowCount(len(rows))
        language = (get_display_language())

        for row, raid in enumerate(rows):

            name_item = QTableWidgetItem(
                get_raid_display_name(
                    raid["instance_key"],
                    language,
                )
            )

            font = name_item.font()
            font.setBold(True)
            name_item.setFont(font)

            self.table.setItem(
                row,
                0,
                name_item,
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    raid["LFR"]
                ),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    raid["N"]
                ),
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    raid["H"]
                ),
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    raid["M"]
                ),
            )

            self.table.resizeRowsToContents()

            self.table.setVerticalScrollBarPolicy(
                Qt.ScrollBarAlwaysOff
            )

            header_height = (
                self.table.horizontalHeader().height()
            )

            rows_height = 0

            for row in range(
                self.table.rowCount()
            ):
                rows_height += (
                    self.table.rowHeight(row)
                )

            self.table.setFixedHeight(
                header_height
                + rows_height
                + 6
            )