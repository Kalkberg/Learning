# -*- coding: utf-8 -*-
"""
Imports polling data and plots on a map

@author: Kalkberg
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
import pandas
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

Ramen = pandas.read_csv('Ramen_Ratings.csv')

# Create color map


# Calculate min and max values for color bar
stars = np.array([])
for ramencountry in Ramen['Country'].unique():
    stars = np.append(stars,np.mean(Ramen[Ramen['Country'] == ramencountry]['Stars']))

cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=0, vmax=5)


# Load shapefiles
CountriesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_0_countries') 
StatesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_1_states_provinces') 

# Set up figure
#fig = plt.figure()
#fig.set_canvas(plt.gcf().canvas)
#ax = fig.add_subplot(111)
#ax.autoscale(enable=False)
fig = plt.figure(figsize=(15, 7.5))

# Draw map
ax = plt.axes(projection=ccrs.PlateCarree())
#Projection options: PlateCarree Mollweide Robinson

# Draw countries
for country in shpreader.Reader(CountriesShape).records():
    # if country is in the database color by mean 
    if country.attributes['NAME_LONG'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['NAME_LONG']]["Stars"]))
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['NAME_LONG'])
    else:
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor='w',
            edgecolor='k',
            label=country.attributes['NAME_LONG'])

# Draw states
for country in shpreader.Reader(StatesShape).records():
    # if country is in the database color by mean 
    if country.attributes['NAME_LONG'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['NAME_LONG']]["Stars"]))
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['NAME_LONG'])
    else:
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor='w',
            edgecolor='k',
            label=country.attributes['NAME_LONG'])

sm = plt.cm.ScalarMappable(cmap=cmap)
sm._A = []
#divider = make_axes_locatable(ax)
#cax = divider.append_axes("right", size="5%", pad=0.05)
cb = plt.colorbar(sm, fraction=0.0226, pad=-.012)
cb.set_ticks([0,1/5,2/5,3/5,4/5,1])
cb.ax.set_yticklabels([0,1,2,3,4,5]) 
#cb.ax.set_title('Mean Stars')
cb.set_label('Mean Stars', labelpad=-55, fontsize=14, fontweight='bold')

# Plot color bar
#fig.colorbar(ax, cmap=cmap, norm=norm,
#                                orientation='horizontal')
#
#plt.colorbar(ax, ax=ax, cmap=cmap, norm=norm, ticks=[0,2.5,5])
plt.tight_layout()
plt.title('World Ramen Ratings', y=.95, fontsize=14, fontweight='bold')
plt.savefig('Ramen_Map.pdf')
## Color for median stars
#cmap(np.mean(Ramen[Ramen["Country"]=="Vietnam"]["Stars"]))
#
#np.mean(Ramen[Ramen['Variety'].str.contains('Chicken')]['Stars'])