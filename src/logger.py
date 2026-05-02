import logging, os
from logging.handlers import RotatingFileHandler
from src.config import LOG_DIR


def _setup_logs() -> logging.Logger:
    """
    Loggin configuration for the application.

    Returns:
        - logging.Logger: A configured logger instance name "TSF"
    """
    log = logging.getLogger("TSF")

    # Already initialised
    if log.handlers:
        return log

    os.makedirs(LOG_DIR, exist_ok=True)

    handler = RotatingFileHandler(
        filename=LOG_DIR / "app.log",
        mode="a",
        encoding="utf-8",
        maxBytes=1024**2 * 5, # 5 MB file 
        backupCount=3,
    )

    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
        )
    )

    log.addHandler(handler)
    log.setLevel(logging.INFO)
    log.propagate = False

    log.info("Logger initialised (singleton)")
    return log


logger = _setup_logs()
