# -*- coding: utf-8 -*-
"""
Plot chosen indices of WDI data

@author: Kalkberg
"""
#%% Imports
import requests
import pandas
import geopandas
import matplotlib
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import numpy as np
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

#%% Database operations

# Get admin 0 JSON data from web and put in geopandas database
url = 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson'
NatShape = geopandas.read_file(url)

# Load WDI data from csv then convert to geopandas dataframe
WDI = pandas.read_csv('WDIData.csv')
WDI = geopandas.GeoDataFrame(WDI)

# Average years 2008-2018 and add new column for indexing
WDI['2008-2018AVG'] = np.nanmean(np.vstack((WDI['2008'].values,
   WDI['2009'].values,WDI['2010'].values,WDI['2011'].values,WDI['2012'].values,
   WDI['2013'].values,WDI['2014'].values,WDI['2015'].values,WDI['2016'].values,
   WDI['2017'].values,WDI['2018'].values)),axis=0)

WDI.loc[WDI['Indicator Code']=='EG.ELC.ACCS.ZS',['Country Code','2008-2018AVG']]

NatShape.rename(columns={'adm0_a3':'Country Code'},inplace=True)

NatShape=NatShape.merge(WDI.loc[WDI['Indicator Code']=='EG.ELC.ACCS.ZS',['Country Code','2008-2018AVG']], on='Country Code', how='left')

#%% Do figure stuff

### Set up color map
fig = plt.figure() 
ax = fig.gca() 
cmap = matplotlib.cm.get_cmap('viridis')
border = (.6,.6,.6,.1)

# Get variable normalization
Max = NatShape['2008-2018AVG'].max()

for i in range(len(NatShape['geometry'])):
    poly = NatShape['geometry'][i]
    if np.isnan(NatShape['2008-2018AVG'][i]) == True:
        color = (.74, .76, .73, 1)
    else:
        color = cmap(NatShape['2008-2018AVG'][i]/Max)
    ax.add_patch(PolygonPatch(poly, fc=color, ec=border, alpha=1, zorder=2))

ax.axis('scaled')
ax.set_xlim(-180,180)
ax.set_ylim(-90,90)
# add colorbar
fig = ax.get_figure()
cax = fig.add_axes([0.92, 0.225, 0.03, 0.55])
sm = plt.cm.ScalarMappable(cmap='viridis', 
                           norm=plt.Normalize(vmin=np.nanmin(NatShape['2008-2018AVG'].values), 
                                              vmax=np.nanmax(NatShape['2008-2018AVG'].values)))
# fake up the array of the scalar mappable
sm._A = []
fig.colorbar(sm, cax=cax)
plt.show()