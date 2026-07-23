from app.services.display_language import get_display_language


UI_STRINGS = {
    "pve": {
        "en": "PvE",
        "de": "PvE",
        "fr": "JcE",
    },
    "pvp": {
        "en": "PvP",
        "de": "PvP",
        "fr": "JcJ",
    },
    "vault": {
        "en": "Vault",
        "de": "Tresor",
        "fr": "Coffre",
    },
    "character_resources": {
    "en": "Character Resources",
    "de": "Charakterressourcen",
    "fr": "Ressources du personnage",
    },

    "mythic_plus": {
        "en": "Mythic+",
        "de": "Mythisch+",
        "fr": "Mythique+",
    },

    "delves": {
        "en": "Delves",
        "de": "Tiefen",
        "fr": "Gouffres",
    },

    "raid": {
        "en": "Raid",
        "de": "Schlachtzug",
        "fr": "Raid",
    },

    "honor_level": {
        "en": "Honor Level",
        "de": "Ehrenstufe",
        "fr": "Niveau d'honneur",
    },

    "honor_progress": {
        "en": "Honor Progress",
        "de": "Ehrenfortschritt",
        "fr": "Progression d'honneur",
    },

    "overview": {
        "en": "Overview",
        "de": "Übersicht",
        "fr": "Vue d'ensemble",
    },

    "tracking": {
        "en": "Tracking",
        "de": "Tracking",
        "fr": "Suivi",
    },

    "currencies": {
        "en": "Currencies",
        "de": "Währungen",
        "fr": "Monnaies",
    },

    "stats": {
        "en": "Stats",
        "de": "Werte",
        "fr": "Statistiques",
    },

    "reputation": {
        "en": "Reputation",
        "de": "Ruf",
        "fr": "Réputation",
    },

    "debug": {
        "en": "Debug",
        "de": "Debug",
        "fr": "Debug",
    },
    "settings": {
    "en": "Settings",
    "de": "Einstellungen",
    "fr": "Paramètres",
    },

    "application_settings": {
        "en": "Application Settings",
        "de": "Anwendungseinstellungen",
        "fr": "Paramètres de l'application",
    },

    "theme": {
        "en": "Theme",
        "de": "Design",
        "fr": "Thème",
    },

    "dark": {
        "en": "Dark",
        "de": "Dunkel",
        "fr": "Sombre",
    },

    "light": {
        "en": "Girly Power",
        "de": "Girly Power",
        "fr": "Girly Power",
    },

    "wow": {
        "en": "WoW",
        "de": "WoW",
        "fr": "WoW",
    },

    "modern": {
        "en": "Modern",
        "de": "Modern",
        "fr": "Moderne",
    },

    "daddy_gamer": {
        "en": "Daddy Gamer",
        "de": "Daddy Gamer",
        "fr": "Daddy Gamer",
    },    

        "cherry_blossom": {
        "en": "Cherry Blossom",
        "de": "Cherry Blossom",
        "fr": "Cherry Blossom",
    },    

    "number_format": {
        "en": "Number Format",
        "de": "Zahlenformat",
        "fr": "Format numérique",
    },

    "display_language": {
        "en": "Display Language",
        "de": "Anzeigesprache",
        "fr": "Langue d'affichage",
    },

    "english": {
        "en": "English",
        "de": "Englisch",
        "fr": "Anglais",
    },

    "german": {
        "en": "German",
        "de": "Deutsch",
        "fr": "Allemand",
    },

    "french": {
        "en": "French",
        "de": "Französisch",
        "fr": "Français",
    },

    "open_log_folder": {
        "en": "Open Log Folder",
        "de": "Log-Ordner öffnen",
        "fr": "Ouvrir le dossier des journaux",
    },

    "save": {
        "en": "Save",
        "de": "Speichern",
        "fr": "Enregistrer",
    },

    "cancel": {
        "en": "Cancel",
        "de": "Abbrechen",
        "fr": "Annuler",
    },

    "delete_character": {
    "en": "Delete Character",
    "de": "Charakter löschen",
    "fr": "Supprimer le personnage",
    },

    "delete_character_confirmation": {
        "en": (
            'Delete "{name}"?\n\n'
            "This will permanently remove "
            "the character export file."
        ),
        "de": (
            'Charakter "{name}" löschen?\n\n'
            "Dadurch wird die exportierte "
            "Charakterdatei dauerhaft entfernt."
        ),
        "fr": (
            'Supprimer le personnage "{name}" ?\n\n'
            "Cela supprimera définitivement "
            "le fichier d'export du personnage."
        ),
    },
    "paste_character_data": {
    "en": "Paste Character Data",
    "de": "Charakterdaten einfügen",
    "fr": "Coller les données du personnage",
    },

    "warband_tasks": {
        "en": "Warband Tasks",
        "de": "Warband-Aufgaben",
        "fr": "Tâches de bataillon",
    },

    "back": {
        "en": "Back",
        "de": "Zurück",
        "fr": "Retour",
    },

    "renown": {
        "en": "Renown",
        "de": "Ruhm",
        "fr": "Renom",
    },

    "warband_resources": {
        "en": "Warband Resources",
        "de": "Warband-Ressourcen",
        "fr": "Ressources du bataillon",
    },

    "no_reputation_data_available": {
        "en": "No reputation data available",
        "de": "Keine Rufdaten verfügbar",
        "fr": "Aucune donnée de réputation disponible",
    },

    "notes": {
        "en": "Notes",
        "de": "Notizen",
        "fr": "Notes",
    },

    "notes_placeholder": {
        "en": "Enter notes (max 512 characters)...",
        "de": "Notizen eingeben (maximal 512 Zeichen)...",
        "fr": "Saisir des notes (512 caractères maximum)...",
    },

    "vault_progress": {
        "en": "Vault Progress",
        "de": "Tresorfortschritt",
        "fr": "Progression du coffre",
    },

    "raid_slots": {
        "en": "Raid Slots",
        "de": "Schlachtzug-Slots",
        "fr": "Emplacements de raid",
    },

    "mplus_slots": {
        "en": "M+ Slots",
        "de": "M+-Slots",
        "fr": "Emplacements Mythique+",
    },

    "delve_slots": {
        "en": "Delve Slots",
        "de": "Tiefen-Slots",
        "fr": "Emplacements de gouffres",
    },

    "weekly_duties": {
        "en": "Weekly Duties",
        "de": "Wöchentliche Aufgaben",
        "fr": "Tâches hebdomadaires",
    },

    "clear_all": {
        "en": "Clear All",
        "de": "Alles löschen",
        "fr": "Tout effacer",
    },

    "paste_character_data": {
        "en": "Paste Character Data",
        "de": "Charakterdaten einfügen",
        "fr": "Coller les données du personnage",
    },

    "paste_character_export_here": {
        "en": "Paste your character export here:",
        "de": "Charakterexport hier einfügen:",
        "fr": "Collez l'export de votre personnage ici :",
    },

    "paste_wow_export_here": {
        "en": "Paste your WoW export text here...",
        "de": "WoW-Exporttext hier einfügen...",
        "fr": "Collez ici le texte d'export WoW...",
    },

    "new_task_name": {
        "en": "New task name...",
        "de": "Neuer Aufgabenname...",
        "fr": "Nouveau nom de tâche...",
    },

    "add": {
        "en": "Add",
        "de": "Hinzufügen",
        "fr": "Ajouter",
    },

    "delete_selected": {
        "en": "Delete Selected",
        "de": "Ausgewählte löschen",
        "fr": "Supprimer la sélection",
    },

    "close": {
        "en": "Close",
        "de": "Schließen",
        "fr": "Fermer",
    },

    "task_exists": {
        "en": "Task Exists",
        "de": "Aufgabe existiert bereits",
        "fr": "La tâche existe déjà",
    },

    "task_already_exists": {
        "en": "\"{name}\" already exists.",
        "de": "\"{name}\" existiert bereits.",
        "fr": "\"{name}\" existe déjà.",
    },

    "delete_task": {
        "en": "Delete Task",
        "de": "Aufgabe löschen",
        "fr": "Supprimer la tâche",
    },

    "delete_task_confirmation": {
        "en": "Delete \"{name}\"?",
        "de": "\"{name}\" löschen?",
        "fr": "Supprimer \"{name}\" ?",
    },

    "character": {
        "en": "Character",
        "de": "Charakter",
        "fr": "Personnage",
    },

    "class": {
        "en": "Class",
        "de": "Klasse",
        "fr": "Classe",
    },

    "item_level": {
        "en": "Item Level",
        "de": "Gegenstandsstufe",
        "fr": "Niveau d'objet",
    },

    "level": {
        "en": "Level",
        "de": "Stufe",
        "fr": "Niveau",
    },

    "specialization": {
        "en": "Specialization",
        "de": "Spezialisierung",
        "fr": "Spécialisation",
    },

    "coffer_keys": {
        "en": "Coffer Keys",
        "de": "Schlüssel",
        "fr": "Clés de coffre",
    },

    "radiant_spark_dust": {
        "en": "R. Spark Dust",
        "de": "Funkenstaub",
        "fr": "Poussière d'étincelle",
    },

    "delete_character_menu": {
        "en": "Delete {name}...",
        "de": "{name} löschen...",
        "fr": "Supprimer {name}...",
    },
    "attribute": {
        "en": "Attribute",
        "de": "Attribut",
        "fr": "Attribut",
    },

    "value": {
        "en": "Value",
        "de": "Wert",
        "fr": "Valeur",
    },

    "primary_attributes": {
        "en": "Primary Attributes",
        "de": "Primärattribute",
        "fr": "Attributs principaux",
    },

    "combat_ratings": {
        "en": "Combat Ratings",
        "de": "Kampfwerte",
        "fr": "Statistiques de combat",
    },

    "stat": {
        "en": "Stat",
        "de": "Wert",
        "fr": "Statistique",
    },

    "rating": {
        "en": "Rating",
        "de": "Wertung",
        "fr": "Score",
    },

    "equipment": {
        "en": "Equipment",
        "de": "Ausrüstung",
        "fr": "Équipement",
    },

    "slot": {
        "en": "Slot",
        "de": "Platz",
        "fr": "Emplacement",
    },

    "name": {
        "en": "Name",
        "de": "Name",
        "fr": "Nom",
    },

    "type": {
        "en": "Type",
        "de": "Typ",
        "fr": "Type",
    },

    "enchanted": {
        "en": "Enchanted",
        "de": "Verzaubert",
        "fr": "Enchanté",
    },

    "yes": {
        "en": "Yes",
        "de": "Ja",
        "fr": "Oui",
    },

    "no": {
        "en": "No",
        "de": "Nein",
        "fr": "Non",
    },

    "search_reputations": {
        "en": "Search reputations (min 3 letters)...",
        "de": "Ruf suchen (mindestens 3 Buchstaben)...",
        "fr": "Rechercher une réputation (3 lettres minimum)...",
    },

    "faction": {
        "en": "Faction",
        "de": "Fraktion",
        "fr": "Faction",
    },

    "progress": {
        "en": "Progress",
        "de": "Fortschritt",
        "fr": "Progression",
    },

    "renown_prefix": {
        "en": "Renown",
        "de": "Ruhm",
        "fr": "Renom",
    },

    "name": {
        "en": "Name",
        "de": "Name",
        "fr": "Nom",
    },

    "amount": {
        "en": "Amount",
        "de": "Anzahl",
        "fr": "Quantité",
    },

    "max": {
        "en": "Max",
        "de": "Max",
        "fr": "Max",
    },

    "expand_all": {
        "en": "Expand All",
        "de": "Alle ausklappen",
        "fr": "Tout développer",
    },

    "collapse_all": {
        "en": "Collapse All",
        "de": "Alle einklappen",
        "fr": "Tout réduire",
    },

    "number_format_german": {
        "en": "German (1.234.567)",
        "de": "Deutsch (1.234.567)",
        "fr": "Allemand (1.234.567)",
    },

    "number_format_english": {
        "en": "English (1,234,567)",
        "de": "Englisch (1,234,567)",
        "fr": "Anglais (1,234,567)",
    },

    "player_vs_player": {
        "en": "Player vs. Player",
        "de": "Spieler gegen Spieler",
        "fr": "Joueur contre Joueur",
    },

    "miscellaneous": {
        "en": "Miscellaneous",
        "de": "Verschiedenes",
        "fr": "Divers",
    },

    "other": {
        "en": "Other",
        "de": "Sonstige",
        "fr": "Autre",
    },

    "season_1": {
        "en": "Season 1",
        "de": "Saison 1",
        "fr": "Saison 1",
    },

    "raid_progress": {
        "en": "Raid Progress",
        "de": "Raidfortschritt",
        "fr": "Progression de raid",
    },

    "instance": {
        "en": "Instance",
        "de": "Instanz",
        "fr": "Instance",
    },

    "lfr": {
        "en": "LFR",
        "de": "LFR",
        "fr": "LFR",
    },

    "normal": {
        "en": "Normal",
        "de": "Normal",
        "fr": "Normal",
    },

    "heroic": {
        "en": "Heroic",
        "de": "Heroisch",
        "fr": "Héroïque",
    },

    "mythic": {
        "en": "Mythic",
        "de": "Mythisch",
        "fr": "Mythique",
    },




}


def get_ui_string(
    key,
    language=None,
):
    if language is None:
        language = (
            get_display_language()
        )

    entry = UI_STRINGS.get(key)

    if entry is None:
        return key

    return entry.get(
        language,
        entry["en"],
    )