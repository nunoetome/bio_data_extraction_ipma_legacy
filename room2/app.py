# ------------------------- app.py -------------------------
#
# ------------------- Description -------------------------
# This is the main file of the application. 
#
# It is responsible for starting the application and 
# calling the necessary functions to download the data 
# from IPMA RSS sources and extract the information from it.
# ------------------- info -------------------------
# this starts:
# - download_ipma_rss_comunicados
#
# -------------------change log -------------------------
# [2024-10-19] - [Nuno Tomé] - [Initial Version]



from logging_config import LOGGER, ini_logging
from worker_ipma_api_av_met_3 import worker_ipma_api_av_met_3




def main():
    ini_logging()
    LOGGER.info(">>>>>>>>> Starting application IPMA RSS downloader <<<<<<<<<")
    
    LOGGER.debug("starting worker_ipma_api_av_met_3")
    worker_ipma_api_av_met_3()
    LOGGER.debug("finished worker_ipma_api_av_met_3")
    
    LOGGER.info(">>>>>>>>> Application finished <<<<<<<<<")

if __name__ == '__main__':
    main()