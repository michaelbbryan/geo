#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a MODULE that provides and demonstrates functions for downloading, unzipping and opening
geodatabase files. The example below uses the Census' shape files and geodatabase for
block groups and ZCTA files with the American Community Survey
"""

import wget
import zipfile
import geopandas as gpd
import fiona

def get_zipdir(zipdirurl, zipdirfile, destdir="./"):
    # download Census geodatabases and unzip the result
    print("Downloading", zipdirfile, " from ", zipdirurl + zipdirfile)
    filename = wget.download(zipdirurl + zipdirfile, out = destdir, bar=None)
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


