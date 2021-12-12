import logging

LOG_FORMATTER = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')

def set_log_config(logger):
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(LOG_FORMATTER)
    logger.addHandler(stream_handler)
    return logger