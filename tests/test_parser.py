import os
from app.parser.txt_parser import parse_txt


def create_test_file(tmp_path):
    content = """Character: Arthas
Class: Paladin
Level: 80

Gold: 500

Shard of Dundun (ID: 3376) - Quantity: 4/8
"""

    file_path = tmp_path / "arthas.txt"
    file_path.write_text(content, encoding="utf-8")
    return file_path


def test_parse_basic_character(tmp_path):
    file_path = create_test_file(tmp_path)

    character = parse_txt(str(file_path))

    assert character.name == "Arthas"
    assert character.location["Class"] == "Paladin"
    assert character.location["Level"] == "80"


def test_parse_currency_with_max(tmp_path):
    file_path = create_test_file(tmp_path)

    character = parse_txt(str(file_path))

    assert len(character.currencies) == 1

    currency = character.currencies[0]
    assert currency.name == "Shard of Dundun"
    assert currency.quantity == 4
    assert currency.max_value == 8


def test_ignores_non_allowed_lines(tmp_path):
    content = """Character: Testy
RandomStuff: ShouldBeIgnored
Unknown: 123
"""

    file_path = tmp_path / "test.txt"
    file_path.write_text(content, encoding="utf-8")

    character = parse_txt(str(file_path))

# Only Characters should be used
    assert character.name == "Testy"
    assert "RandomStuff" not in character.location
    assert "Unknown" not in character.location


def test_filename_fallback(tmp_path):
    content = """Class: Mage"""

    file_path = tmp_path / "fallback_name.txt"
    file_path.write_text(content, encoding="utf-8")

    character = parse_txt(str(file_path))

    assert character.name == "fallback_name"