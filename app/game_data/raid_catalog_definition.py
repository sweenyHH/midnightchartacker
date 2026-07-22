class RaidCatalogDefinition:

    def __init__(
        self,
        raid_id,
        key,

        english_name,
        german_name,
        french_name,

        content_type,
        featured=False,
    ):
        self.raid_id = raid_id
        self.key = key

        self.english_name = english_name
        self.german_name = german_name
        self.french_name = french_name

        self.content_type = content_type

        self.featured = featured