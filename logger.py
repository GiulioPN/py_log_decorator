import logging

_APP_NAME = "monte_carlo_pi"
_DEFAULT_LOG_FILE = f"{_APP_NAME}.log"


# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(_DEFAULT_LOG_FILE),
        logging.StreamHandler(),
    ],
)

# Create a logger specific to this module
app_logger = logging.getLogger(_APP_NAME)
"""Logger for the application."""
