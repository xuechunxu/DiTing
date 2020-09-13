import logging
from scripts.variables import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)-8s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

# Using FileHandler writing log to file
logfile = os.path.join(OUT_DIR, 'log.txt')
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Using StreamHandler writing to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# Add the two Handlers
logger.addHandler(ch)
logger.addHandler(fh)
