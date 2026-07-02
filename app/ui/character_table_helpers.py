from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QColor

from app.ui.theme_manager import ThemeManager


class NumericItem(QTableWidgetItem):
    def __init__(self, display_value, sort_value):
        super().__init__(display_value)
        self.sort_value = sort_value

    def __lt__(self, other):
        if isinstance(other, NumericItem):
            return self.sort_value < other.sort_value
        return super().__lt__(other)


def format_vault_values(values):
    if not values:
        return ""

    return " | ".join(str(v) for v in values if v)


def get_attr(char, attr_name):
    value = getattr(char, attr_name, None)
    return str(value) if value is not None else "-"


def get_currency_value(char, name):
    for c in char.currencies:
        if c.name == name:
            return c
    return None


def adjust_class_color(color_hex):
    theme = (ThemeManager.current_theme or "").lower()

    if theme in ("light", "modern"):

        if color_hex.lower() == "#ffffff":
            return "#333333"

        color = QColor(color_hex)

        brightness = (
            0.299 * color.red()
            + 0.587 * color.green()
            + 0.114 * color.blue()
        )

        if brightness > 220:
            return "#333333"

    return color_hex