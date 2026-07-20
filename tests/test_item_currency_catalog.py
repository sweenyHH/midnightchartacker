from app.game_data.item_currency_catalog import (
    get_item_currency_by_id,
    get_item_currency_by_key,
    get_item_currency_by_name,
    is_featured_item_currency,
    get_item_currency_display_name,
    get_overview_item_currencies,
)

def test_lookup_by_id():

    item = get_item_currency_by_id(
        232875
    )

    assert item is not None
    assert item.key == (
        "spark_of_radiance"
    )


def test_lookup_by_key():

    item = get_item_currency_by_key(
        "spark_of_radiance"
    )

    assert item is not None
    assert item.item_id == 232875


def test_featured_flag():

    item = get_item_currency_by_key(
        "spark_of_radiance"
    )

    assert item.featured is False

def test_lookup_by_english_name():

    item = get_item_currency_by_name(
        "Spark of Radiance"
    )

    assert item is not None
    assert item.key == (
        "spark_of_radiance"
    )

def test_lookup_by_german_name():

    item = get_item_currency_by_name(
        "Funke der Strahlen"
    )

    assert item is not None
    assert item.key == (
        "spark_of_radiance"
    )

def test_lookup_by_french_name():

    item = get_item_currency_by_name(
        "Étincelle de radiance"
    )

    assert item is not None
    assert item.key == (
        "spark_of_radiance"
    )

def test_is_featured_item_currency():

    assert is_featured_item_currency(
        "angler_pearls"
    ) is False

def test_display_name_english():

    assert (
        get_item_currency_display_name(
            "spark_of_radiance",
            "en",
        )
        == "Spark of Radiance"
    )


def test_display_name_german():

    assert (
        get_item_currency_display_name(
            "spark_of_radiance",
            "de",
        )
        == "Funke der Strahlen"
    )


def test_display_name_french():

    assert (
        get_item_currency_display_name(
            "spark_of_radiance",
            "fr",
        )
        == "Étincelle de radiance"
    )

def test_get_overview_item_currencies():

    currencies = (
        get_overview_item_currencies()
    )

    keys = {
        c.key
        for c in currencies
    }

    assert (
        "spark_of_radiance"
        in keys
    )
