from pathlib import Path

from app.parser.base_parser import parse_txt


DATA_DIR = (
    Path(__file__).parent
    / "data"
)

def test_dornogal_reputation_key_is_language_independent():

    english = parse_txt(
        str(DATA_DIR / "full_character.txt")
    )

    german = parse_txt(
        str(DATA_DIR / "german_character.txt")
    )

    french = parse_txt(
        str(DATA_DIR / "french_character.txt")
    )

    def find_dornogal(character):

        return next(
            (
                r
                for r in character.reputations
                if r.reputation_key
                == "council_of_dornogal"
            ),
            None,
        )

    english_rep = find_dornogal(
        english
    )

    german_rep = find_dornogal(
        german
    )

    french_rep = find_dornogal(
        french
    )

    assert english_rep is not None
    assert german_rep is not None
    assert french_rep is not None

    assert (
        english_rep.reputation_key
        == german_rep.reputation_key
    )

    assert (
        english_rep.reputation_key
        == french_rep.reputation_key
    )

def test_currency_key_is_language_independent():

    english = parse_txt(
        str(DATA_DIR / "full_character.txt")
    )

    german = parse_txt(
        str(DATA_DIR / "german_character.txt")
    )

    french = parse_txt(
        str(DATA_DIR / "french_character.txt")
    )

    def find_brimming_arcana(character):

        return next(
            (
                c
                for c in character.currencies
                if c.currency_key
                == "brimming_arcana"
            ),
            None,
        )

    english_currency = find_brimming_arcana(
        english
    )

    german_currency = find_brimming_arcana(
        german
    )

    french_currency = find_brimming_arcana(
        french
    )

    assert english_currency is not None
    assert german_currency is not None
    assert french_currency is not None

    assert (
        english_currency.currency_key
        == german_currency.currency_key
    )

    assert (
        english_currency.currency_key
        == french_currency.currency_key
    )