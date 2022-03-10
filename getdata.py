#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program provides and demonstrates functions for downloading, unzipping and openning
geodatabase files.  The example below uses the Census' shape files and geodatabase for
block group
"""

import wget
import zipfile
import geopandas as gpd
import fiona

def get_zipdir(zipdirurl, zipdirfile, destdir="./"):
    # download Census geodatabases and unzip the result
    print("Downloading", zipdirfile, " from ", zipdirurl + zipdirfile)
    filename = wget.download(zipdirurl + zipdirfile, out = destdir, bar=None)
    print(">>>",filename,"<<<")
    print("Unzipping", zipdirfile)
    with zipfile.ZipFile(destdir + zipdirfile, 'r') as z:
        z.extractall(destdir)
    print("Done!")
    return(destdir + zipdirfile[:zipdirfile.index(".zip")])

def get_metadata(geofilename):  # geofilename is the string file name of the gdb
    """
    Each Census geodatabase includes a layer titled
        {geography}_METADATA_{vintage} that lists column names and descriptions
        In this study case the layer is called ZCTA_METADATA_2019
    This metadata, however, does not tell you which layer has the selected column.
    So you need to make your own lookup spreadsheet, e.g.

    :param geofilename: string of the geodatabase file name
    :return: print output of every layer.column name
    """
    layers = fiona.listlayers(geofilename)
    for layer in layers:
        df = gpd.read_file(geofilename, layer=layer)
        for c in df.columns:
            print(layer,":",c)   # list is delimited by : for excel text to columns e.g.
    return()

###############################################
# Download and unzip Census geodatabases
################################################

workdir = "./"

zctadata = get_zipdir(
    zipdirurl = "https://www2.census.gov/geo/tiger/TIGER_DP/2019ACS/",
    zipdirfile = "ACS_2019_5YR_ZCTA.gdb.zip",
    destdir = workdir
    )

zctashapefile = get_zipdir(
    zipdirurl ="https://www2.census.gov/geo/tiger/TIGER2019/ZCTA5/",
    zipdirfile ="tl_2019_us_zcta510.zip",
    destdir = workdir
    )

bgdata = get_zipdir(
    zipdirurl = "https://www2.census.gov/geo/tiger/TIGER_DP/2019ACS/",
    zipdirfile = "ACS_2019_5YR_BG.gdb.zip",
    destdir = workdir
    )

print("Getting block group shape files")
bgshapefiles = ['tl_2019_01_bg.zip','tl_2019_02_bg.zip','tl_2019_04_bg.zip','tl_2019_05_bg.zip','tl_2019_06_bg.zip','tl_2019_08_bg.zip','tl_2019_09_bg.zip','tl_2019_10_bg.zip','tl_2019_11_bg.zip','tl_2019_12_bg.zip','tl_2019_13_bg.zip','tl_2019_15_bg.zip','tl_2019_16_bg.zip','tl_2019_17_bg.zip','tl_2019_18_bg.zip','tl_2019_19_bg.zip','tl_2019_20_bg.zip','tl_2019_21_bg.zip','tl_2019_22_bg.zip','tl_2019_23_bg.zip','tl_2019_24_bg.zip','tl_2019_25_bg.zip','tl_2019_26_bg.zip','tl_2019_27_bg.zip','tl_2019_28_bg.zip','tl_2019_29_bg.zip','tl_2019_30_bg.zip','tl_2019_31_bg.zip','tl_2019_32_bg.zip','tl_2019_33_bg.zip','tl_2019_34_bg.zip','tl_2019_35_bg.zip','tl_2019_36_bg.zip','tl_2019_37_bg.zip','tl_2019_38_bg.zip','tl_2019_39_bg.zip','tl_2019_40_bg.zip','tl_2019_41_bg.zip','tl_2019_42_bg.zip','tl_2019_44_bg.zip','tl_2019_45_bg.zip','tl_2019_46_bg.zip','tl_2019_47_bg.zip','tl_2019_48_bg.zip','tl_2019_49_bg.zip','tl_2019_50_bg.zip','tl_2019_51_bg.zip','tl_2019_53_bg.zip','tl_2019_54_bg.zip','tl_2019_55_bg.zip','tl_2019_56_bg.zip','tl_2019_60_bg.zip','tl_2019_66_bg.zip','tl_2019_69_bg.zip','tl_2019_72_bg.zip','tl_2019_78_bg.zip']
for s in bgshapefiles:
    get_zipdir(
        zipdirurl = "https://www2.census.gov/geo/tiger/TIGER2019/BG/",
        zipdirfile = s,
        destdir = workdir
        )
print("Appending shape files")
bgshapes = gpd.read_file(workdir + bgshapefiles[0]).truncate()
for s in bgshapefiles:
    bgshapes = bgshapes.append(gpd.read_file(             workdir + s)
print("   Loaded",len(bgshapefiles),"states covering", len(bgshapes.GEOID.unique()),"blockgroups")
