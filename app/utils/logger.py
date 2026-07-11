from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


# --------------------------------------------------
# LOG DIRECTORY
# --------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "mct.log"


# --------------------------------------------------
# LOGGER
# --------------------------------------------------

logger = logging.getLogger("mct")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:

    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)