import logging
from config.config import LOG_FILE_PATH

# def get_logger(name=__name__):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)

#     if not logger.handlers:  # Prevent adding multiple handlers
#         file_handler = logging.FileHandler("test_logs.log")
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)

#     return logger

def setup_logging(name=__name__, log_file=LOG_FILE_PATH, level=logging.INFO):
    """ 
    Set up and return a logger with both console and file handlers.
    Prevents handler duplication on repeated calls.

    Args:
        name (str): Name of the logger (default: __name__).
        log_file (str): Path to the log file.
        level (int): Logging level (default: logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

# Example usage
logger = setup_logging()
logger.info("Logger initialized successfully.")
