class PvpBracketCatalogDefinition:

    def __init__(
        self,
        bracket_id,
        key,

        english_name,
        german_name,
        french_name,

        overview=False,
    ):
        self.bracket_id = bracket_id
        self.key = key

        self.english_name = english_name
        self.german_name = german_name
        self.french_name = french_name

        self.overview = overview