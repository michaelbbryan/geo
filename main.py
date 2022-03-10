#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This project collects example code and other utilities used in geographic analytics.
    main.py    provides the imports and environments needed for the rest of the programs.
"""

###############################################################
# Major geo packages
#

# Usual suspects
import os
import logging
import datetime
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# For data downloads from Census eg
import wget
import zipfile

# Big geo packages
import geopandas as gpd
import fiona
import geoplot as gplt
# To install geopandas you need to (In this case, using the geo conda environment)
#  1. configure the GDAL package's sys envars
#       setx GDAL_DATA        "C:\Users\michael\anaconda3\envs\geo\Library\share\gdal"
#       setx GDAL_DRIVER_PATH "C:\Users\michael\anaconda3\envs\geo\Library\share\gdal"
#       setx PROJ_LIB         "C:\Users\michael\anaconda3\envs\geo\Library\share\proj"
#  2. install the proj-data package
#       conda install -c conda-forge proj-data
# setx PYTHONPATH "C:\Program Files\GDAL\"  - not sure if this is really necessary

# Initialize logging
logging.basicConfig(level=logging.INFO)
logging.debug('Initializing debug logging')
logging.info('Initializing info logging')
logging.warning('Initializing warning logging')
logging.error('Initializing error logging')
logging.critical('Initializing critical logging')

# Start the clock
start = datetime.datetime.now()
logging.info("Starting", start)
stop = datetime.datetime.now()
logging.info("Step 1 finished. Duration:", stop - start)

if __name__ == '__main__':
    print('Done.')

