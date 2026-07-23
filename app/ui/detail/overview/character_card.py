from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

from app.ui.colors import CLASS_COLORS
from app.ui.character_table_helpers import (
    adjust_class_color,
)


class CharacterCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName(
            "overviewCard"
        )

        self.setFrameShape(
            QFrame.Box
        )

        layout = QVBoxLayout(self)

        self.data_area = QFrame()
        self.data_area.setObjectName(
            "overviewDataArea"
        )

        data_layout = QVBoxLayout(
            self.data_area
        )

        self.name_label = QLabel()

        self.realm_label = QLabel()

        self.class_label = QLabel()

        self.spec_label = QLabel()

        self.level_label = QLabel()

        self.ilvl_label = QLabel()

        data_layout.addWidget(
            self.name_label
        )

        data_layout.addWidget(
            self.realm_label
        )

        data_layout.addSpacing(8)

        data_layout.addWidget(
            self.class_label
        )

        data_layout.addWidget(
            self.spec_label
        )

        data_layout.addSpacing(8)

        data_layout.addWidget(
            self.level_label
        )

        data_layout.addWidget(
            self.ilvl_label
        )

        layout.addWidget(
            self.data_area
        )     

    def set_character(
        self,
        character,
    ):

        class_name = getattr(
            character,
            "character_class",
            "-"
        )

        full_name = getattr(
            character,
            "name",
            "-"
        )

        name_parts = full_name.split(
            "-",
            1
        )

        character_name = (
            name_parts[0]
        )

        realm_name = (
            name_parts[1]
            if len(name_parts) > 1
            else "-"
        )

        self.name_label.setText(
            f"<h2>{character_name}</h2>"
        )

        self.realm_label.setText(
            f"<b>{realm_name}</b>"
        )

        self.class_label.setText(
            f"<b>{getattr(character, 'race', '-')}</b> "
            f"<b>{class_name}</b>"
        )

        self.spec_label.setText(
            f"<b>{getattr(character, 'specialization', '-')}</b>"
        )

        self.level_label.setText(
            f"<b>Level:</b> "
            f"{getattr(character, 'level', '-')}"
        )

        if class_name in CLASS_COLORS:

            adjusted = adjust_class_color(
                CLASS_COLORS[class_name]
            )

            self.class_label.setStyleSheet(
                f"color: {adjusted};"
            )

            self.spec_label.setStyleSheet(
                f"color: {adjusted};"
            )

        else:

            self.class_label.setStyleSheet(
                ""
            )

            self.spec_label.setStyleSheet(
                ""
            )

        self.ilvl_label.setText(
            f"<b>Item Level:</b> "
            f"{getattr(character, 'avg_item_level', '-')}"
        )