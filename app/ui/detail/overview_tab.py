from PySide6.QtWidgets import (
QWidget,
QVBoxLayout,
QHBoxLayout,
QLabel,
QFrame,
QGridLayout,
)

from PySide6.QtCore import Qt

from app.ui.colors import CLASS_COLORS
from app.ui.character_table_helpers import (
    adjust_class_color,
)
from app.ui.blizzard_color_codes import get_mplus_color
from app.game_data.currency_catalog import get_currency_display_name

from app.services.display_language import get_display_language


class OverviewTab(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(12)
        self.character_card = QFrame()
        self.character_card.setFrameShape(QFrame.Box)

        self.character_layout = QVBoxLayout(self.character_card)

        self.name_label = QLabel()
        self.info_label = QLabel()
        self.ilvl_label = QLabel()

        self.mythic_card = QFrame()

        self.mythic_card.setFrameShape(QFrame.Box)

        self.mythic_layout = QVBoxLayout(self.mythic_card)
        self.stats_row = QHBoxLayout()

        self.mythic_title = QLabel("<h3>Mythic+</h3>")
        self.mythic_score_label = QLabel()
        self.mythic_layout.addWidget(self.mythic_title)
        self.mythic_layout.addWidget(self.mythic_score_label)

        self.pvp_card = QFrame()
        self.pvp_card.setFrameShape(QFrame.Box)
        self.pvp_layout = QVBoxLayout(self.pvp_card)
        self.pvp_title = QLabel("<h3>PvP</h3>")
        self.honor_level_label = QLabel()
        self.honor_progress_label = QLabel()
        self.pvp_layout.addWidget(self.pvp_title)
        self.pvp_layout.addWidget(self.honor_level_label)
        self.pvp_layout.addWidget(self.honor_progress_label)

        self.resources_card = QFrame()
        self.resources_card.setFrameShape(QFrame.Box)
        self.resources_layout = QVBoxLayout(self.resources_card)

        self.resources_grid = QGridLayout()

        self.resources_title = QLabel("<h3>Character Resources</h3>")

        self.mythic_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.pvp_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.resources_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.coffer_name_label = QLabel()
        self.coffer_value_label = QLabel()

        self.undercoin_name_label = QLabel()
        self.undercoin_value_label = QLabel()

        self.spark_name_label = QLabel()
        self.spark_value_label = QLabel()

        self.resources_layout.addWidget(
            self.resources_title
        )

        self.resources_grid.addWidget(
            self.coffer_name_label,
            0,
            0
        )

        self.resources_grid.addWidget(
            self.coffer_value_label,
            0,
            1
        )

        self.resources_grid.addWidget(
            self.undercoin_name_label,
            1,
            0
        )

        self.resources_grid.addWidget(
            self.undercoin_value_label,
            1,
            1
        )

        self.resources_grid.addWidget(
            self.spark_name_label,
            2,
            0
        )

        self.resources_grid.addWidget(
            self.spark_value_label,
            2,
            1
        )

        self.resources_grid.setColumnStretch(
            0,
            3
        )

        self.resources_grid.setColumnStretch(
            1,
            1
        )

        self.resources_layout.addLayout(
            self.resources_grid
        )

        self.character_layout.addWidget(self.name_label)
        self.character_layout.addWidget(self.info_label)
        self.character_layout.addWidget(self.ilvl_label)

        self.main_layout.addWidget(self.character_card)

        self.main_layout.addLayout(self.stats_row)
        self.stats_row.addWidget(self.mythic_card)

        self.stats_row.addWidget(self.pvp_card)

        self.main_layout.addWidget(self.resources_card)

        self.main_layout.addStretch()

    def set_character(self, character):

        class_name = getattr(
            character,
            "character_class",
            "-"
        )

        self.name_label.setText(f"<h2>{character.name}</h2>")

        self.info_label.setText(
            f"<b>Level {getattr(character, 'level', '-')}</b> "
            f"<b>{getattr(character, 'race', '-')}</b> "
            f"<b>{class_name}</b> "
            f"<b>({getattr(character, 'specialization', '-')})</b>"
        )

        if class_name in CLASS_COLORS:

            adjusted = adjust_class_color(CLASS_COLORS[class_name])

            self.info_label.setStyleSheet(f"color: {adjusted};")

        else:

            self.info_label.setStyleSheet("")

        self.ilvl_label.setText(
            f"<b>Item Level:</b> "
            f"{getattr(character, 'avg_item_level', '-')}"
        )

        score = getattr(
            character,
            "mythic_score",
            None,
        )

        self.mythic_score_label.setText(f"Score: {score}")
        self.mythic_score_label.setStyleSheet(f"color: {get_mplus_color(score)};")
        self.honor_level_label.setText(
            f"Honor Level: "
            f"{getattr(character, 'honor_level', '-')}"
        )

        if (character.honor_progress is not None and character.honor_progress_max is not None):

            self.honor_progress_label.setText(
                f"Honor Progress: "
                f"{character.honor_progress}"
                f"/"
                f"{character.honor_progress_max}"
            )

        else:

            self.honor_progress_label.setText("Honor Progress: -")

        def find_currency(currency_key):

            return next(
                (
                    c
                    for c in character.currencies
                    if c.currency_key == currency_key
                ),
                None,
            )

        language = get_display_language()

        coffer = find_currency("restored_coffer_key")

        self.coffer_name_label.setText(
            get_currency_display_name(
                "restored_coffer_key",
                language,
            )
        )

        self.coffer_value_label.setText(
            str(coffer.quantity if coffer else 0)
        )

        undercoin = find_currency("undercoin")

        self.undercoin_name_label.setText(
            get_currency_display_name(
                "undercoin",
                language,
            )
        )

        self.undercoin_value_label.setText(
            str(undercoin.quantity if undercoin else 0)
        )

        spark = find_currency("radiant_spark_dust")

        self.spark_name_label.setText(
            get_currency_display_name(
                "radiant_spark_dust",
                language,
            )
        )

        self.spark_value_label.setText(
            str(spark.quantity if spark else 0)
        )

