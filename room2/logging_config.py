# ------------------------- logging_config.py -------------------------
#
# ------------------- Description -------------------------
# This script is responsible for configuring the logging system
# for the application "bio_data_data_extraction_ipma",
# https://github.com/nunoetome/bio_data_extraction_ipma_legacy,
# and it part a larger scope project that aims to extract 
# data from various sources and store it in a database for 
# cientific and technological research purposes.
#
# ------------------- info -------------------------
# This scrip is based on "My Python Logging System"
# https://github.com/nunoetome/my_python_starter_kit
# It was based on the version my_python_starter_kit 2.5 but
# it was adapted to be used in this project
# -------------------change log -------------------------
# [?] - [Nuno Tomé] - [Initial Version]
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version


# - This file is part of the project 
# "bio_data_data_extraction_ipma" 
# and was created by the project organization.


import logging
#import inspect
#import os


# ----------------- LOG CONFIGURATION -----------------
#
# Config here the logging level
# Just uncomment the desired level and comment the others

LOG_LEVEL_GLOBAL = logging.DEBUG
#LOG_LEVEL_GLOBAL = logging.INFO
#LOG_LEVEL_GLOBAL = logging.WARNING
#LOG_LEVEL_GLOBAL = logging.ERROR
#LOG_LEVEL_GLOBAL = logging.CRITICAL

LOG_LEVEL_FILE = logging.DEBUG
#LOG_LEVEL_FILE = logging.INFO
#LOG_LEVEL_FILE = logging.WARNING
#LOG_LEVEL_FILE = logging.ERROR
#LOG_LEVEL_FILE = logging.CRITICAL

#LOG_LEVEL_CONSOLE = logging.DEBUG
LOG_LEVEL_CONSOLE = logging.INFO
#LOG_LEVEL_CONSOLE = logging.WARNING
#LOG_LEVEL_CONSOLE = logging.ERROR
#LOG_LEVEL_CONSOLE = logging.CRITICAL

LOG_OUTPUT_FILE = 'app.log'

#LOG_FORMAT_FILE = '%(asctime)s - %(levelname)s - %(message)s - [%(filename)s - %(funcName)s]' 
# The prefix "<<mpls>>" is a custom string that can be used to identify the beginning 
# of a log messages of this application. This helps the bulk analysis of log files
# preventing the confusion with date and time information
# It stands for "My Python Logging System"
LOG_FORMAT_FILE = '<<mpls>> %(asctime)s - %(levelname)s - %(message)s' 
LOG_FORMAT_CONSOLE = '<<mpls>> %(levelname)s - %(message)s'

# ULTRA_DEBUG mode
# This mode will reinforce the debug messages with a different format
# to add more information to the log in case of extreme debugging
# This mode is useful when you need to debug a specific part of the code
# and you need more information than the usual debug mode
# To enable this mode, just change the following lines

# Change to True to enable the ultra debug mode
FILE_ULTRA_DEBUG = True
CONSOLE_ULTRA_DEBUG = True

# Configure the format of the ultra debug mode
LOG_FORMAT_FILE_ULTRA_DEBUG = LOG_FORMAT_FILE + ' - [%(filename)s - %(funcName)s - %(lineno)d]'
LOG_FORMAT_CONSOLE_ULTRA_DEBUG = LOG_FORMAT_CONSOLE + ' - [%(filename)s - %(funcName)s - %(lineno)d]'
# ----------------- END OF LOG CONFIGURATION -----------------


LOGGER = logging.getLogger(__name__)

def ini_logging():
    
    # GLOBAL LOGGING CONFIGURATION
    LOGGER.setLevel(LOG_LEVEL_GLOBAL) 
    
    # FILE HANDLER LOGGING CONFIGURATION
    file_handler = logging.FileHandler(LOG_OUTPUT_FILE)
    file_handler.setLevel(LOG_LEVEL_FILE)
    file_handler_formatter = logging.Formatter(LOG_FORMAT_FILE)  
    
    if FILE_ULTRA_DEBUG:
        class CustomDebugFormatteFile(logging.Formatter):
            def format(self, record):
                if record.levelno == logging.DEBUG:
                    self._style._fmt = LOG_FORMAT_FILE_ULTRA_DEBUG  # Formato de debug
                else:
                    self._style._fmt = LOG_FORMAT_FILE  # Formato normal
                return super().format(record)        
        file_handler.setFormatter(CustomDebugFormatteFile())
    else:
        file_handler.setFormatter(console_handler_formatter)
        
        
    LOGGER.addHandler(file_handler)
    
    
    # CONSOLE HANDLER LOGGING CONFIGURATION
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL_CONSOLE)
    console_handler_formatter = logging.Formatter(LOG_FORMAT_CONSOLE)    
    
    
    if CONSOLE_ULTRA_DEBUG:
        class CustomDebugFormatter(logging.Formatter):
            def format(self, record):
                if record.levelno == logging.DEBUG:
                    self._style._fmt = LOG_FORMAT_CONSOLE_ULTRA_DEBUG  # Formato de debug
                else:
                    self._style._fmt = LOG_FORMAT_CONSOLE  # Formato normal
                return super().format(record)        
        console_handler.setFormatter(CustomDebugFormatter())
    else:
        console_handler.setFormatter(console_handler_formatter)
        
    
    LOGGER.addHandler(console_handler)

    
    return LOGGER


