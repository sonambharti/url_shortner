# app/core/log_config.py
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
import sys

log_queue = Queue()

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
))

# Queue listener
listener = QueueListener(log_queue, console_handler)
listener.start()

# Logger setup function
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(QueueHandler(log_queue))
    logger.propagate = False  # Avoid duplicate logs
    return logger


    """
    from app.core.log_config import setup_logger
    logger = setup_logger(__name__)
    logger.warning(f"Registration attempt with existing email: {data.email}")
    logger.info(f"New user registered: {data.email}")
    
    """