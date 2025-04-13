import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def example_function():
    logger.debug("Logger")
    print(os.getcwd())
    return "Hello world"
