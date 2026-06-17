import pytest
from app.model.character import Character, Currency


def test_currency_initialization():
    currency = Currency("Gold", 100, max_value=1000, category="Money")

    assert currency.name == "Gold"
    assert currency.quantity == 100
    assert currency.max_value == 1000
    assert currency.category == "Money"


def test_currency_without_max():
    currency = Currency("Shard", 5)

    assert currency.name == "Shard"
    assert currency.quantity == 5
    assert currency.max_value is None


def test_character_initialization():
    character = Character("TestChar")

    assert character.name == "TestChar"
    assert character.location == {}
    assert character.currencies == []


def test_add_currency():
    character = Character("TestChar")
    currency = Currency("Gold", 200)

    character.add_currency(currency)

    assert len(character.currencies) == 1
    assert character.currencies[0].name == "Gold"