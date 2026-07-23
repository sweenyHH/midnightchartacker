from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QGridLayout, QCheckBox, QPushButton, QFrame
)
from PySide6.QtCore import Qt, QTimer
from app.ui.colors import STATUS_COLORS
from .weekly_duties_config import ROWS_CONFIG
from app.utils.logger import logger
from app.storage.weekly_duties_storage import (
    load_state,
    save_state,
)
from app.localization.ui_strings import get_ui_string

import os


class WeeklyDutiesWidget(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "overviewCard"
        )

        self.setFrameShape(
            QFrame.Box
        )

        self.layout = QVBoxLayout(self)
        self.title_label = QLabel(
            "<b>Weekly Duties</b>"
        )

        self.title_label.setObjectName(
            "overviewSectionTitle"
        )

        self.layout.addWidget(
            self.title_label
        )

        self.rows_config = ROWS_CONFIG

        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(12)
        self.grid.setVerticalSpacing(6)

        self.layout.addLayout(self.grid)
        self.layout.addStretch()

        self.clear_btn = QPushButton(
            get_ui_string(
                "clear_all"
            )
        )
        self.clear_btn.clicked.connect(self.clear_all)
        self.layout.addWidget(self.clear_btn)

        self.current_file = None
        self.checkboxes = []
        self.row_labels = []
        self._build_grid()

# Style checkboxes (green when checked)
#        self.setStyleSheet(f"""
#        QCheckBox::indicator {{
#            width: 14px;
#            height: 14px;
#        }}
#
#        QCheckBox::indicator:checked {{
#            background-color: {STATUS_COLORS['success']};
#            border: 1px solid {STATUS_COLORS['success']};
#        }}
#
#        QCheckBox::indicator:unchecked {{
#            border: 1px solid #888;
#            background: transparent;
#        }}
#        """)


    def _build_grid(self):

        max_boxes = max(
            count
            for _, count
            in self.rows_config
        )

        current_row = 0

        for row_index, (
            name,
            count,
        ) in enumerate(
            self.rows_config
        ):

            if name == "__SPACER__":

                spacer = QLabel("")

                spacer.setObjectName(
                    "weeklyDutiesSpacer"
                )

                spacer.setFixedHeight(12)

                self.grid.addWidget(
                    spacer,
                    current_row,
                    0,
                )

                current_row += 1

                continue

            label = QLabel(
                f"<b>{name}</b>"
            )

            label.setObjectName(
                "weeklyDutiesRowLabel"
            )

            label.setAlignment(
                Qt.AlignLeft
                | Qt.AlignVCenter
            )

            self.grid.addWidget(
                label,
                current_row,
                0,
            )

            self.row_labels.append(
                label
            )

            boxes = []

            for col in range(
                max_boxes
            ):

                if col < count:

                    cb = QCheckBox()

                    cb.setObjectName(
                        "weeklyDutiesCheckbox"
                    )

                    cb.stateChanged.connect(
                        self._save
                    )

                    cb.stateChanged.connect(
                        self._update_row_visuals
                    )

                    cb.setMaximumWidth(20)

                    self.grid.addWidget(
                        cb,
                        current_row,
                        col + 2,
                        alignment=Qt.AlignCenter
                    )

                    boxes.append(
                        cb
                    )

                else:

                    continue

            self.checkboxes.append(
                (
                    row_index,
                    boxes,
                )
            )

            current_row += 1

        #
        # Column layout
        #
        # 0 = duty label
        # 1 = spacer column
        # 2..n = checkbox columns
        #

        self.grid.setColumnStretch(
            0,
            0,
        )

        self.grid.setColumnMinimumWidth(
            1,
            16,
        )

        for col in range(
            2,
            max_boxes + 2,
        ):
            self.grid.setColumnStretch(
                col,
                0,
            )

        self.grid.setColumnStretch(
            max_boxes + 2,
            1,
        )          

# --------------------------------------------------
    def _save(self):

        if not self.current_file:

            logger.warning(
                "Weekly duties save skipped: "
                "no character loaded"
            )

            return
        

        try:

            save_state(
                self.current_file,
                self.checkboxes
            )

            logger.info(
                f"Weekly duties saved: "
                f"{self.current_file}"
            )

        except Exception:

            logger.exception(
                f"Failed to save weekly duties: "
                f"{os.path.basename(self.current_file)}"
            )

            raise

# --------------------------------------------------
    def _update_row_visuals(self):

        for (row_index, boxes), label in zip(self.checkboxes, self.row_labels):

# reset style
            label.setStyleSheet("")

            checked = sum(1 for cb in boxes if cb.isChecked())
            total = len(boxes)

            if checked == total:
                style = f"color: {STATUS_COLORS['success']}; font-weight: bold;"
            else:
                style = f"color: {STATUS_COLORS['error']};"

            label.setStyleSheet(style)

# --------------------------------------------------
    def set_character(self, character):

        logger.info(
            f"Weekly duties loaded for: "
            f"{character.name}"
        )

        self.current_file = character.source_file

        try:

            saved_state = load_state(
                self.current_file
            )

        except Exception:

            logger.exception(
                f"Failed to load weekly duties: "
                f"{self.current_file}"
            )

            raise

        for row_index, boxes in self.checkboxes:

            for col, cb in enumerate(boxes):

                key = f"{row_index}_{col}"

                cb.blockSignals(True)

                cb.setChecked(
                    bool(
                        saved_state.get(key)
                    )
                )

                cb.blockSignals(False)

        self._update_row_visuals()

# --------------------------------------------------

    def clear_all(self):

        logger.info(
            f"Weekly duties cleared: "
            f"{os.path.basename(self.current_file)}"
        )

        for _, boxes in self.checkboxes:
            for cb in boxes:
                cb.setChecked(False)

        self._save()