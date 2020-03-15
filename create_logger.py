
import logging

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('logs/test.log')
    fmt = '%(asctime)s %(module)s %(levelname)s: %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = create_logger()