import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    filename="app.log",
    filemode="a",
    encoding="utf-8"
)

logging.debug("Debugging details")
logging.info("Application started")
logging.warning("This is a warning")
logging.error("An error occurred")