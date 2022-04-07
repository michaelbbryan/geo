#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a MODULE that provides and demonstrates functions for generating
geographic plots including choropleths with custom colors defined by some
variable on each geographic shape
"""

import matplotlib.pyplot as plt

def choropleth(geodf, colorcolumn, coloroption):
    """
    :param geodf:         the dataframe to be plotted with a geometry column
    :param colorcolumn:   the column in the dataframe with the color involved
    :param coloroption:   the plotly color range
    :return:
    """
    if 'geometry' not in list(geodf.columns):
        raise TypeError('Dataframe is missing a geometry column; not a geodataframe.')
    if colorcolumn not in list(geodf.columns):
        raise TypeError('colorcolumn'+colorcolumn+' is not in dataframe.')
    fig, ax = plt.subplots(1, 1, )
    fig.set_size_inches(18.5, 10.5)
    geodf.plot(ax=ax,
               column=colorcolumn,
               cmap=coloroption)
    return(fig)
