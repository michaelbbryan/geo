#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This project collects example code and other utilities used in geographic analytics.
    main.py    provides the imports and environments needed for the rest of the programs.
"""

# Usual suspects
import os
import logging
import datetime
import pandas as pd

# Big geo packages
import geopandas as gpd
import fiona
import geoplot as gplt

# Homegrown geo tools
import getgeodata as gd
import geocharting as gc

# Install GDAL core and GDAL
#     follow this bat file https://github.com/michaelbbryan/python_gdal_automated_windows/blob/main/Python_GDAL_x64.bat
#     https://download.gisinternals.com/sdk/downloads/release-1930-x64-gdal-3-4-1-mapserver-7-6-4/gdal-304-1930-x64-core.msi
#     https://download.gisinternals.com/sdk/downloads/release-1930-x64-gdal-3-4-1-mapserver-7-6-4/GDAL-3.4.1.win-amd64-py3.9.msi
#     setx /m path "%path%;C:\Program Files\GDAL;
#     setx /m GDAL_DATA "C:\Program Files\GDAL\gdal-data"
#     setx /m GDAL_DRIVER_PATH "C:\Program Files\GDAL\gdalplugins"
#     setx /m GDAL_VERSION "3.4.1"

# Initialize logging
logging.basicConfig(level=logging.INFO)
logging.debug('Initializing debug logging')
logging.info('Initializing info logging')
logging.warning('Initializing warning logging')
logging.error('Initializing error logging')
logging.critical('Initializing critical logging')

# Turn if all off for now
logger.propagate = False


if __name__ == '__main__':
    # Start the clock
    start = datetime.datetime.now()
    logging.info("Starting", start)

    ###############################################
    # Download and unzip Census geodatabases
    ################################################

    workdir = "./"

    zctadata = gd.get_zipdir(
        zipdirurl="https://www2.census.gov/geo/tiger/TIGER_DP/2019ACS/",
        zipdirfile="ACS_2019_5YR_ZCTA.gdb.zip",
        destdir=workdir
    )

    stop = datetime.datetime.now()
    logging.info("Get ZCTA finished. Duration:", stop - start)

    zctashapefile = gd.get_zipdir(
        zipdirurl="https://www2.census.gov/geo/tiger/TIGER2019/ZCTA5/",
        zipdirfile="tl_2019_us_zcta510.zip",
        destdir=workdir
    )

    bgdata = gd.get_zipdir(
        zipdirurl="https://www2.census.gov/geo/tiger/TIGER_DP/2019ACS/",
        zipdirfile="ACS_2019_5YR_BG.gdb.zip",
        destdir=workdir
    )

    print("Getting block group shape files")
    bgshapefiles = ['tl_2019_01_bg.zip', 'tl_2019_02_bg.zip', 'tl_2019_04_bg.zip', 'tl_2019_05_bg.zip',
                    'tl_2019_06_bg.zip', 'tl_2019_08_bg.zip', 'tl_2019_09_bg.zip', 'tl_2019_10_bg.zip',
                    'tl_2019_11_bg.zip', 'tl_2019_12_bg.zip', 'tl_2019_13_bg.zip', 'tl_2019_15_bg.zip',
                    'tl_2019_16_bg.zip', 'tl_2019_17_bg.zip', 'tl_2019_18_bg.zip', 'tl_2019_19_bg.zip',
                    'tl_2019_20_bg.zip', 'tl_2019_21_bg.zip', 'tl_2019_22_bg.zip', 'tl_2019_23_bg.zip',
                    'tl_2019_24_bg.zip', 'tl_2019_25_bg.zip', 'tl_2019_26_bg.zip', 'tl_2019_27_bg.zip',
                    'tl_2019_28_bg.zip', 'tl_2019_29_bg.zip', 'tl_2019_30_bg.zip', 'tl_2019_31_bg.zip',
                    'tl_2019_32_bg.zip', 'tl_2019_33_bg.zip', 'tl_2019_34_bg.zip', 'tl_2019_35_bg.zip',
                    'tl_2019_36_bg.zip', 'tl_2019_37_bg.zip', 'tl_2019_38_bg.zip', 'tl_2019_39_bg.zip',
                    'tl_2019_40_bg.zip', 'tl_2019_41_bg.zip', 'tl_2019_42_bg.zip', 'tl_2019_44_bg.zip',
                    'tl_2019_45_bg.zip', 'tl_2019_46_bg.zip', 'tl_2019_47_bg.zip', 'tl_2019_48_bg.zip',
                    'tl_2019_49_bg.zip', 'tl_2019_50_bg.zip', 'tl_2019_51_bg.zip', 'tl_2019_53_bg.zip',
                    'tl_2019_54_bg.zip', 'tl_2019_55_bg.zip', 'tl_2019_56_bg.zip', 'tl_2019_60_bg.zip',
                    'tl_2019_66_bg.zip', 'tl_2019_69_bg.zip', 'tl_2019_72_bg.zip', 'tl_2019_78_bg.zip']
    for s in bgshapefiles:
        gd.get_zipdir(
            zipdirurl="https://www2.census.gov/geo/tiger/TIGER2019/BG/",
            zipdirfile=s,
            destdir=workdir
        )

    print("Appending shape files")
    bgshapes = gpd.read_file(workdir + bgshapefiles[0]).truncate()
    for s in bgshapefiles:
        bgshapes = bgshapes.append(gpd.read_file(workdir + s))
    print("   Loaded", len(bgshapefiles), "states covering", len(bgshapes.GEOID.unique()), "blockgroups")

    # Try the choropleth
    analyzing = pd.read_pickle("analyzing.pkl")
    gc.choropleth(analyzing,"B01001e1","")
    print('Done.')

