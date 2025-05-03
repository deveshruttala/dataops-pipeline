import logging
import os

def setup_logging(log_file="logs/pipeline.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    logging.getLogger().addHandler(logging.StreamHandler())  # For console output too
    logging.info("Logging setup complete.")