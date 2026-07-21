from app.localization.ui_strings import (
    get_ui_string,
)


def test_pve_english():

    assert (
        get_ui_string(
            "pve",
            "en",
        )
        == "PvE"
    )


def test_vault_german():

    assert (
        get_ui_string(
            "vault",
            "de",
        )
        == "Tresor"
    )


def test_vault_french():

    assert (
        get_ui_string(
            "vault",
            "fr",
        )
        == "Coffre"
    )


def test_unknown_key_returns_key():

    assert (
        get_ui_string(
            "unknown_key",
            "en",
        )
        == "unknown_key"
    )

def test_character_resources_german():

    assert (
        get_ui_string(
            "character_resources",
            "de",
        )
        == "Charakterressourcen"
    )


def test_raid_french():

    assert (
        get_ui_string(
            "raid",
            "fr",
        )
        == "Raid"
    )


def test_mythic_plus_english():

    assert (
        get_ui_string(
            "mythic_plus",
            "en",
        )
        == "Mythic+"
    )

def test_overview_german():

    assert (
        get_ui_string(
            "overview",
            "de",
        )
        == "Übersicht"
    )


def test_currencies_french():

    assert (
        get_ui_string(
            "currencies",
            "fr",
        )
        == "Monnaies"
    )

def test_settings_german():

    assert (
        get_ui_string(
            "settings",
            "de",
        )
        == "Einstellungen"
    )


def test_save_french():

    assert (
        get_ui_string(
            "save",
            "fr",
        )
        == "Enregistrer"
    )


def test_open_log_folder_german():

    assert (
        get_ui_string(
            "open_log_folder",
            "de",
        )
        == "Log-Ordner öffnen"
    )

def test_delete_character_german():

    assert (
        get_ui_string(
            "delete_character",
            "de",
        )
        == "Charakter löschen"
    )


def test_delete_confirmation_french():

    text = get_ui_string(
        "delete_character_confirmation",
        "fr",
    )

    assert "Supprimer" in text

def test_back_german():

    assert (
        get_ui_string(
            "back",
            "de",
        )
        == "Zurück"
    )


def test_renown_french():

    assert (
        get_ui_string(
            "renown",
            "fr",
        )
        == "Renom"
    )


def test_warband_resources_english():

    assert (
        get_ui_string(
            "warband_resources",
            "en",
        )
        == "Warband Resources"
    )

def test_notes_german():

    assert (
        get_ui_string(
            "notes",
            "de",
        )
        == "Notizen"
    )


def test_clear_all_french():

    assert (
        get_ui_string(
            "clear_all",
            "fr",
        )
        == "Tout effacer"
    )


def test_weekly_duties_english():

    assert (
        get_ui_string(
            "weekly_duties",
            "en",
        )
        == "Weekly Duties"
    )

def test_paste_character_data_german():

    assert (
        get_ui_string(
            "paste_character_data",
            "de",
        )
        == "Charakterdaten einfügen"
    )


def test_paste_label_french():

    assert (
        get_ui_string(
            "paste_character_export_here",
            "fr",
        )
        == "Collez l'export de votre personnage ici :"
    )


def test_paste_placeholder_english():

    assert (
        get_ui_string(
            "paste_wow_export_here",
            "en",
        )
        == "Paste your WoW export text here..."
    )

def test_add_german():

    assert (
        get_ui_string(
            "add",
            "de",
        )
        == "Hinzufügen"
    )


def test_close_french():

    assert (
        get_ui_string(
            "close",
            "fr",
        )
        == "Fermer"
    )


def test_delete_task_english():

    assert (
        get_ui_string(
            "delete_task",
            "en",
        )
        == "Delete Task"
    )

def test_character_german():

    assert (
        get_ui_string(
            "character",
            "de",
        )
        == "Charakter"
    )


def test_item_level_french():

    assert (
        get_ui_string(
            "item_level",
            "fr",
        )
        == "Niveau d'objet"
    )


def test_specialization_english():

    assert (
        get_ui_string(
            "specialization",
            "en",
        )
        == "Specialization"
    )

def test_equipment_german():

    assert (
        get_ui_string(
            "equipment",
            "de",
        )
        == "Ausrüstung"
    )


def test_yes_french():

    assert (
        get_ui_string(
            "yes",
            "fr",
        )
        == "Oui"
    )


def test_combat_ratings_english():

    assert (
        get_ui_string(
            "combat_ratings",
            "en",
        )
        == "Combat Ratings"
    )

def test_faction_german():

    assert (
        get_ui_string(
            "faction",
            "de",
        )
        == "Fraktion"
    )


def test_progress_french():

    assert (
        get_ui_string(
            "progress",
            "fr",
        )
        == "Progression"
    )


def test_renown_prefix_german():

    assert (
        get_ui_string(
            "renown_prefix",
            "de",
        )
        == "Ruhm"
    )

def test_expand_all_german():

    assert (
        get_ui_string(
            "expand_all",
            "de",
        )
        == "Alle ausklappen"
    )


def test_collapse_all_french():

    assert (
        get_ui_string(
            "collapse_all",
            "fr",
        )
        == "Tout réduire"
    )


def test_amount_german():

    assert (
        get_ui_string(
            "amount",
            "de",
        )
        == "Anzahl"
    )

def test_number_format_german_french():

    assert (
        get_ui_string(
            "number_format_german",
            "fr",
        )
        == "Allemand (1.234.567)"
    )


def test_number_format_english_german():

    assert (
        get_ui_string(
            "number_format_english",
            "de",
        )
        == "Englisch (1,234,567)"
    )

def test_other_german():

    assert (
        get_ui_string(
            "other",
            "de",
        )
        == "Sonstige"
    )


def test_miscellaneous_french():

    assert (
        get_ui_string(
            "miscellaneous",
            "fr",
        )
        == "Divers"
    )


def test_player_vs_player_german():

    assert (
        get_ui_string(
            "player_vs_player",
            "de",
        )
        == "Spieler gegen Spieler"
    )