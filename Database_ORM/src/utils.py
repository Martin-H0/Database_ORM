import logging
import os
from logging.handlers import RotatingFileHandler
import json


def setup_logging():  #level: str, log_file: str
    """
    Set up logging configuration for the application.

    Args:
        level (str): Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file (str): Path to the log file
    """
    level = readconfiglogging("level")
    log_file = readconfiglogging("log_file")
    
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Remove any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create formatters and handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Log the setup completion
    logging.info(f"Logging setup completed. Level: {level}, File: {log_file}")

def readconfiglogging(key):
    with open("./Database_ORM/config.json","r") as f:
        config = json.load(f)
        return config["logging"][key]