# -*- coding: utf-8 -*-
"""
World Plot

Pull down JSON data, and plot on map with color set by variable.
@author: Kalkberg
"""

import requests
import geopandas
import matplotlib
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import seaborn as sns

url = 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson'
countries = geopandas.read_file(url)

# Or pull down JSON data
#countries = requests.get('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson').json()

# Set up color map
fig = plt.figure() 
ax = fig.gca() 
cmap = matplotlib.cm.get_cmap('viridis')

# Get variable normalization
MaxPop = countries['pop_est'].max()

for i in range(len(countries['geometry'])):
    poly = countries['geometry'][i]
    color = cmap(countries['pop_est'][i]/MaxPop)
    ax.add_patch(PolygonPatch(poly, fc=color, ec=color, alpha=0.5, zorder=2))

ax.axis('scaled')
plt.show()
#BLUE = '#6699cc'
#fig = plt.figure() 
#ax = fig.gca() 
#ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))
#ax.axis('scaled')
#plt.show()