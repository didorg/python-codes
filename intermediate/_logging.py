# from loguru import logger
# loguru is a Library Ready to use out of the box without boilerplate
# https://loguru.readthedocs.io/en/stable/index.html
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# ************************************************************
# The following example configures a very simple logger, a console handler, and a simple formatter using Python code:
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.info('------------------- A very simple logger --------------------')
logger.debug('debug message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
# ************************************************************

# ********************************************
# python-json-logger
# https://github.com/madzak/python-json-logger
# ********************************************
