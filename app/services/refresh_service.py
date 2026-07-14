# Centralizes application refresh and reload logic.
#
# This service will gradually become responsible for:
# - Reload coordination
# - Reload protection
# - Watcher integration
# - Selection preservation
# - Refresh notifications
#
# The service remains UI-agnostic.


from app.utils.logger import logger
from app.services.warband_currency_service import (
    get_warband_currency_totals
)

class RefreshService:
    """
    Coordinates application refresh operations.

    This is currently a skeleton implementation and
    will be expanded incrementally during the reload
    architecture refactor.
    """

    def __init__(self, data_service):
        # Service responsible for loading character data.
        self.data_service = data_service

        # Prevent concurrent refresh operations.
        self._reload_running = False

        logger.info(
            "RefreshService initialized"
        )

    def is_reload_running(self):
        return self._reload_running

    def start_reload(self):

        self._reload_running = True

    def finish_reload(self):

        self._reload_running = False

    def refresh_data(self):
        """
        Reloads character data and returns
        all information required by the UI.
        """

        logger.info(
            "Refreshing application data"
        )

        self.data_service.load_data()

        characters = (
            self.data_service.get_characters()
        )

        currency_totals = (
            get_warband_currency_totals(
                characters
            )
        )

        reputations = (
            self.data_service.get_top_reputations()
        )

        return (
            characters,
            reputations,
            currency_totals,
        )

