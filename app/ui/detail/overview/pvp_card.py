from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from app.localization.ui_strings import get_ui_string
from app.ui.detail.overview.pvp_rating_widget import PvpRatingWidget
from app.ui.detail.overview.pvp_helper import build_pvp_overview
from app.game_data.pvp_bracket_catalog import get_overview_pvp_brackets, get_pvp_bracket_display_name

from app.services.display_language import get_display_language


class PvpCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "overviewCard"
        )

        self.setFrameShape(
            QFrame.Box
        )

        layout = QVBoxLayout(self)

        self.pvp_title = QLabel()

        self.pvp_title.setObjectName(
            "overviewSectionTitle"
        )

        layout.addSpacing(8)

        self.honor_level_label = QLabel()
        self.honor_level_label.setObjectName(
            "overviewDataLabel"
        )

        self.honor_progress_label = QLabel()
        self.honor_progress_label.setObjectName(
            "overviewDataLabel"
        )

        layout.addWidget(
            self.pvp_title
        )

        layout.addWidget(
            self.honor_level_label
        )

        layout.addWidget(
            self.honor_progress_label
        )

        layout.addSpacing(
            8
        )

        self.rating_row = (
            QHBoxLayout()
        )

        layout.addLayout(
            self.rating_row
        )

        self.pvp_widgets = {}

        for definition in (get_overview_pvp_brackets()):

            widget = (
                PvpRatingWidget(
                    definition.key
                )
            )

            self.pvp_widgets[
                definition.key
            ] = widget

            self.rating_row.addWidget(
                widget
            )

    def set_character(
        self,
        character,
    ):

        self.pvp_title.setText(
            f"<h3>{get_ui_string('pvp')}</h3>"
        )

        self.honor_level_label.setText(
            f"{get_ui_string('honor_level')}: "
            f"{getattr(character, 'honor_level', '-')}"
        )

        if (
            character.honor_progress
            is not None
            and character.honor_progress_max
            is not None
        ):

            self.honor_progress_label.setText(
                f"{get_ui_string('honor_progress')}: "
                f"{character.honor_progress}"
                f"/"
                f"{character.honor_progress_max}"
            )

        else:

            self.honor_progress_label.setText(
                f"{get_ui_string('honor_progress')}: -"
            )

        language = (get_display_language())

        for key, widget in (self.pvp_widgets.items()):

            widget.set_title(
                get_pvp_bracket_display_name(
                    key,
                    language,
                )
            )



        rows = build_pvp_overview(
            character
        )

        for row in rows:

            widget = (
                self.pvp_widgets.get(
                    row["key"]
                )
            )

            if widget:

                widget.set_rating(
                    row["rating"]
                )
  