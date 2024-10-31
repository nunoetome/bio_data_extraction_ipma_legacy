# -------------- worker_ipma_api_av_met_3.py --------------
#
#TODO: #2 review the heather for worker_ipma_api_av_met_3.py
# ------------------- Description -------------------------
# This script downloads api data from IPMA and saves it to a file
# It es part of a set of scripts dedicated to IPMA, and very similar
# between them, with some changes in the constants and the 
# functions that are called, as much as some minor customizations.
#
# This is part of the application "bio_data_data_extraction_ipma",
# https://github.com/nunoetome/bio_data_extraction_ipma_legacy,
# and it part a larger scope project that aims to extract 
# data from various sources and store it in a database for 
# scientific and technological research purposes.
#
# ------------------- info -------------------------
# Category: Worker
# api NAME: Avisos Meteorológicos até 3 dias
# -------------------change log -------------------------
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version


# ------------------- Description -------------------------
# This script downloads api data from IPMA and saves it to a file
# ------------------- info -------------------------
# its based on the original worker script from the room1:
# worker_ipma_api_news.py - alpha version
# -------------------change log -------------------------
# version: alpha
# [2024-10-06] - [Nuno Tomé] - [Initial Version]
# changed: header



#import feedparser
import requests
from logging_config import LOGGER
#from datetime import datetime
#import xml.etree.ElementTree as ET
import json
import os


# ----------------- In code constant definition -----------------

API_URL = "https://api.ipma.pt/open-data/forecast/warnings/warnings_www.json"

DATASET_ID = 'ipma_api_av_met_3'
DATASET_DESCRIPTION = 'Dataset containing api data from IPMA'
DATASET_FOLDER = 'datasets/ipma_api_av_met_3'
HISTORIC_FILE = 'datasets/ipma_api_av_met_3/ipma_api_av_met_3_history.txt'
DATASET_FILE_NAME = f"{DATASET_ID}.txt"
DATASET_FILE_PATH = DATASET_FILE_NAME
#DATASET_FILE_PATH = f"{DATASET_FOLDER}/{DATASET_FILE_NAME}"
FILE_MAX_NUMBER_REGISTERS = 100 # 1MB
# ---------------------------------------------------------------

#TODO: implement the following functions
# Function to check if the purged response is empty
def __purged_api_response_is_empty(purged_api_response):
    return False


# Main function, the one that is called by the exterior
# This function is responsible for downloading api information
# from IPMA and saving it to a file
def worker_ipma_api_av_met_3():
    LOGGER.info("Downloading api data from %s", DATASET_ID)
    
    # get the data from the API to a temporary variable
    try:
        LOGGER.debug("Trying to download API data from %s", API_URL)
        api_response = requests.get(API_URL, timeout=10)
        LOGGER.debug("API Response is empty: %s", api_response.text == "")
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        LOGGER.critical("Failed to download API from %s: %s", API_URL, e)
        return
    LOGGER.debug("API Response: %s", api_response)
    LOGGER.debug("API Response size: %s", len(api_response.text))
        
        
    # If the purged response is empty, ends the process
    #TODO: verify if the purged response is empty
    if not __purged_api_response_is_empty(api_response):
        LOGGER.warning("Purged API response is empty, no need to save it to a file")
  
    # adds the response to the existing data file
    #TODO: #5 implement the function to add the new info to the file
    # don't add duplicated information
    # limit the number of items in the file to a parameter
    # given in the configuration
    
    
    # Save the final file to the disk, replacing the oll one
    # to ensure that the information is not lost, keep a copy
    # of the old file in a historic folder
    # the file name should include the ordinal number 
    # so that the most recent file is always the one with the
    # highest number.
    #TODO: #6 change saving process to save the file with a new name
    try:
        LOGGER.debug("Saving API data to file: %s", DATASET_FILE_PATH)
        with open(DATASET_FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(json.dumps(purged_api_response))
    except (IOError, OSError, json.JSONDecodeError) as e:
        LOGGER.critical("Failed to save API data to file %s: %s", DATASET_FILE_NAME, e)
        return
 
# Test function
# This is not going to used in production
# FOR DEBUGGING ONLY
if __name__ == '__main__':
    LOGGER.warning(">>>> Starting SELF RUNNING TEST for %s <<<<", __file__)
    worker_ipma_api_av_met_3()
    LOGGER.warning(">>>> Ending SELF RUNNING TEST for %s <<<<", __file__)
