from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

from PySide6.QtCore import Qt
from app.ui.detail.overview.overview_constants import OVERVIEW_TILE_WIDTH, OVERVIEW_TILE_HEIGHT


class PvpRatingWidget(QFrame):

    def __init__(
        self,
        bracket_name,
    ):
        super().__init__()

        self.bracket_name = (
            bracket_name
        )

        self.setObjectName(
            "overviewTile"
        )

        self.setProperty(
            "overviewType",
            "pvpRating"
        )

        self.setFrameShape(
            QFrame.Box
        )

        self.setMinimumWidth(
            OVERVIEW_TILE_WIDTH
        )

        self.setMinimumHeight(
            120
        )  

        layout = QVBoxLayout(self)

        self.title_label = QLabel()

        self.title_label.setObjectName(
            "overviewTileHeader"
        )

        self.set_title(
            bracket_name
        )

        self.rating_label = QLabel(
            "-"
        )

        self.rating_label.setObjectName(
            "overviewTileValue"
        )

        self.rating_label.setAlignment(
            Qt.AlignCenter
        )

        self.rating_label.setStyleSheet(
            """
            background: transparent;
            font-size: 24px;
            font-weight: bold;
            """
        )

        layout.addWidget(
            self.title_label
        )

        layout.addStretch()

        layout.addWidget(
            self.rating_label
        )

        layout.addStretch()

    def set_title(self, title):
        self.title_label.setText(
            title
        )


    def set_rating(self, rating):
        if rating is None:
            self.rating_label.setText(
                "-"
            )
        else:
            self.rating_label.setText(
                str(rating)
            )