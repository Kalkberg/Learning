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
import numpy as np
from matplotlib.collections import PatchCollection
#import geoplot

url = 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson'
countries = geopandas.read_file(url)

# Set up color map
fig = plt.figure() 
ax = fig.gca() 
cmap = matplotlib.cm.get_cmap('viridis')

#geoplot.polyplot(df, figsize=(8, 4))

# Get variable normalization
MaxPop = countries['pop_est'].max()

for i in range(len(countries['geometry'])):
    poly = countries['geometry'][i]
    color = cmap(countries['pop_est'][i]/MaxPop)
    ax.add_patch(PolygonPatch(poly, fc=color))

ax.axis('scaled')
plt.show()
#BLUE = '#6699cc'
#fig = plt.figure() 
#ax = fig.gca() 
#ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))
#ax.axis('scaled')
#plt.show()


#countries = requests.get('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson').json()
#
##
#fig, ax = plt.subplots()
#cmap = matplotlib.cm.get_cmap('viridis')
#
#patches = []
#colors = []
## Get variable normalization
#
#PopList=[]
#
#for i in range(len(countries['features'])):
#    PopList.append(countries['features'][i]['properties']['pop_est'])
#    
#MaxPop=max(PopList)
#
#for i in range(len(countries['features'])):
#    if countries['features'][i]['geometry']['type'] == 'Multipolygon':
#        for j in range(len(countries['features'][i]['geometry']['coordinates'])):
#            patch=matplotlib.patches.Polygon(np.squeeze(np.asarray(countries['features'][i]['geometry']['coordinates'][j])))
#            patches.append(patch)
##            colors.append(cmap(countries['features'][i]['properties']['pop_est']/MaxPop))
#    else:
#        patch=matplotlib.patches.Polygon(np.squeeze(np.asarray(countries['features'][i]['geometry']['coordinates'][0])))
##        colors.append(cmap(countries['features'][i]['properties']['pop_est']/MaxPop))
#        patches.append(patch)
#    
#p=PatchCollection(patches)
##p.set_array(np.array(colors))
#ax.add_collection(p)
#ax.set_xlim(-180,180)
#ax.set_ylim(-90,90)
#plt.show()