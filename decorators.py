import functools
import logging
from datetime import datetime

from logger import app_logger


def log_execution_time(operation_name: str, logger: logging.Logger = app_logger):
    """Decorator to log the execution time of a function.

    Parameters
    ----------
    operation_name : str
        The name of the operation to log.
    logger : logging.Logger, optional
        The logger to use, by default app_logger
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            execution_time = end_time - start_time
            logger.info(f"{operation_name} execution time {execution_time}")
            return result

        return wrapper

    return decorator
