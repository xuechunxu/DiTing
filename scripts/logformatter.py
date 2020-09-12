import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)-8s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

# Using FileHandler writing log to file
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Using StreamHandler writing to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# Add the two Handlers
logger.addHandler(ch)
logger.addHandler(fh)
logger.info('this is info message')
logger.warning('this is warn message')
