import logging


logging.basicConfig(
    filename="app.log",
    filemode="w",  # 'w' to overwrite, 'a' to append
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# log messages with timestamp and level
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


def add(x, y):
    logging.info(f"Adding {x} and {y}")
    return x + y

add(5, 10)