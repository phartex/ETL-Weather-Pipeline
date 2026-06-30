"""
Application logging configuration.
"""
import logging
from src.config import LOG_FILE, LOG_DIR

# Create logs directory if it doesn't exist
LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
