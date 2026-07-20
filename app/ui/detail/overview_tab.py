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
from app.game_data.currency_catalog import get_overview_currencies, get_currency_display_name
from app.game_data.item_currency_catalog import get_overview_item_currencies, get_item_currency_display_name

from app.services.display_language import get_display_language
from app.ui.detail.utils import format_gold
from app.utils.number_formatter import format_number
from app.storage.vault_storage import load_user_vault


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

        self.mplus_tile = QFrame()
        self.mplus_tile.setFrameShape(
            QFrame.Box
        )

        self.mplus_layout = QVBoxLayout(
            self.mplus_tile
        )

        self.mplus_tile_title = QLabel(
            "Mythic+"
        )

        self.mythic_score_label = QLabel()

        self.mythic_score_label.setStyleSheet(
            """
            font-size: 28px;
            font-weight: bold;
            """
        )

        self.mplus_layout.addWidget(
            self.mplus_tile_title
        )

        self.mplus_layout.addWidget(
            self.mythic_score_label
        )

        self.vault_tile = QFrame()

        self.vault_tile.setFrameShape(
            QFrame.Box
        )

        self.vault_layout = QVBoxLayout(
            self.vault_tile
        )

        self.vault_grid = QGridLayout()

        self.vault_tile_title = QLabel(
            "Vault"
        )

        self.vault_delves_name = QLabel(
            "Delves"
        )

        self.vault_raid_name = QLabel(
            "Raid"
        )

        self.vault_mplus_name = QLabel(
            "M+"
        )

        self.vault_delves_value = QLabel()
        self.vault_raid_value = QLabel()
        self.vault_mplus_value = QLabel()

        self.vault_layout.addWidget(
            self.vault_tile_title
        )

        self.vault_grid.addWidget(
            self.vault_delves_name,
            0,
            0
        )

        self.vault_grid.addWidget(
            self.vault_delves_value,
            0,
            1
        )

        self.vault_grid.addWidget(
            self.vault_raid_name,
            1,
            0
        )

        self.vault_grid.addWidget(
            self.vault_raid_value,
            1,
            1
        )

        self.vault_grid.addWidget(
            self.vault_mplus_name,
            2,
            0
        )

        self.vault_grid.addWidget(
            self.vault_mplus_value,
            2,
            1
        )

        self.vault_grid.setColumnStretch(
            0,
            1
        )

        self.vault_grid.setColumnStretch(
            1,
            0
        )

        self.vault_layout.addLayout(
            self.vault_grid
        )
       

        self.top_row = QHBoxLayout()
        self.bottom_row = QHBoxLayout()

        self.pve_tiles_row = QHBoxLayout()

        self.pve_title = QLabel("<h3>PvE</h3>")


        self.pve_tiles_row.addWidget(
            self.mplus_tile,
            1
        )

        self.pve_tiles_row.addWidget(
            self.vault_tile,
            1
        )

        self.mythic_layout.addWidget(
            self.pve_title
        )

        self.mythic_layout.addLayout(
            self.pve_tiles_row
        )

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

        self.pve_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.pvp_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.resources_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.resource_rows = {}

        self.resources_layout.addWidget(
            self.resources_title
        )

        definitions = []

        for definition in get_overview_currencies():
            definitions.append(
                ("currency", definition)
            )

        for definition in get_overview_item_currencies():
            definitions.append(
                ("item", definition)
            )

        for index, (kind, definition) in enumerate(
            definitions
        ):

            name_label = QLabel()
            value_label = QLabel()

            row = index // 2

            if index % 2 == 0:

                name_column = 0
                value_column = 1

            else:

                name_column = 2
                value_column = 3

            self.resources_grid.addWidget(
                name_label,
                row,
                name_column
            )

            self.resources_grid.addWidget(
                value_label,
                row,
                value_column
            )

            self.resource_rows[
                (kind, definition.key)
            ] = (
                name_label,
                value_label,
            )

            self.resources_grid.setColumnStretch(
                0,
                3
            )

            self.resources_grid.setColumnStretch(
                1,
                1
            )

            self.resources_grid.setColumnStretch(
                2,
                3
            )

            self.resources_grid.setColumnStretch(
                3,
                1
            )


        self.resources_layout.addLayout(
            self.resources_grid
        )

        self.character_layout.addWidget(self.name_label)
        self.character_layout.addWidget(self.info_label)
        self.character_layout.addWidget(self.ilvl_label)

        self.top_row.addWidget(
            self.character_card,
            1
        )

        self.top_row.addWidget(
            self.mythic_card,
            1
        )

        self.bottom_row.addWidget(
            self.resources_card,
            1
        )

        self.bottom_row.addWidget(
            self.pvp_card,
            1
        )

        self.main_layout.addLayout(
            self.top_row
        )

        self.main_layout.addLayout(
            self.bottom_row
        )


        self.main_layout.addStretch()

    def set_character(self, character):

        class_name = getattr(
            character,
            "character_class",
            "-"
        )

        self.name_label.setText(
            f"<h2>{character.name}</h2>"
        )

        self.info_label.setText(
            f"<b>Level {getattr(character, 'level', '-')}</b> "
            f"<b>{getattr(character, 'race', '-')}</b> "
            f"<b>{class_name}</b> "
            f"<b>({getattr(character, 'specialization', '-')})</b>"
        )

        if class_name in CLASS_COLORS:

            adjusted = adjust_class_color(
                CLASS_COLORS[class_name]
            )

            self.info_label.setStyleSheet(
                f"color: {adjusted};"
            )

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

        self.mythic_score_label.setText(
            str(score)
        )

        self.mythic_score_label.setStyleSheet(
            f"""
            color: {get_mplus_color(score)};
            font-size: 28px;
            font-weight: bold;
            """
        )


        self.honor_level_label.setText(
            f"Honor Level: "
            f"{getattr(character, 'honor_level', '-')}"
        )

        if (
            character.honor_progress is not None
            and character.honor_progress_max is not None
        ):

            self.honor_progress_label.setText(
                f"Honor Progress: "
                f"{character.honor_progress}"
                f"/"
                f"{character.honor_progress_max}"
            )

        else:

            self.honor_progress_label.setText(
                "Honor Progress: -"
            )

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

        for definition in get_overview_currencies():

            currency = find_currency(
                definition.key
            )

            name_label, value_label = (
                self.resource_rows[
                    ("currency", definition.key)
                ]
            )

            name_label.setText(
                get_currency_display_name(
                    definition.key,
                    language,
                )
            )

            quantity = (
                currency.quantity
                if currency
                else 0
            )

            if definition.key == "gold":

                value_text = format_gold(
                    quantity
                )

            else:

                value_text = format_number(
                    quantity
                )

            value_label.setText(
                value_text
            )

        for definition in get_overview_item_currencies():

            currency = find_currency(
                definition.key
            )

            name_label, value_label = (
                self.resource_rows[
                    ("item", definition.key)
                ]
            )

            name_label.setText(
                get_item_currency_display_name(
                    definition.key,
                    language,
                )
            )

            quantity = (
                currency.quantity
                if currency
                else 0
            )

            value_label.setText(
                format_number(
                    quantity
                )
            )

        vault = load_user_vault(
            character
        )

        def dots(slots):

            result = []

            for index in range(3):

                if (
                    index < len(slots)
                    and slots[index]
                ):
                    result.append("●")

                else:
                    result.append("○")

            return " ".join(result)

        self.vault_delves_value.setText(
            dots(vault["row3"])
        )

        self.vault_raid_value.setText(
            dots(vault["row1"])
        )

        self.vault_mplus_value.setText(
            dots(vault["row2"])
        )