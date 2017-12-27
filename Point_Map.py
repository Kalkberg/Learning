# -*- coding: utf-8 -*-
"""
Plots points on a map

@author: pyakovlev
"""

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Inputs
In = 'Tibet_New_Points.csv' # Name of input file
Out = 'Tibet_Points' # Stem name of output file

# Read in data, cut out headers and redistribute
data = np.genfromtxt(In, delimiter=',')
data = np.delete(data, (0), axis=0)
lat, long = data[:,0], data[:,1]

# Remove any nan values
lat = lat[~np.isnan(lat)]
long = long[~np.isnan(long)]

# Set up map boundaries
Lat_Bound = (np.min(lat),np.max(lat)) # Min and max latitude to plot
Long_Bound = (np.min(long),np.max(long)) # Min and max longitude to plot

# Set up basemap
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
ax.autoscale(enable=False)
m = Basemap(projection='merc',llcrnrlat=Lat_Bound[0],urcrnrlat=Lat_Bound[1],
            llcrnrlon=Long_Bound[0],urcrnrlon=Long_Bound[1],
            lat_ts=np.mean((Lat_Bound[0],Lat_Bound[1])),resolution='i')

m.drawcoastlines(linewidth=0.5, color='0.8')
m.drawcountries(linewidth=0.5, linestyle='solid', color='0.8')
m.drawstates(linewidth=0.5, linestyle='solid', color='0.8')
m.drawparallels(np.arange(Lat_Bound[0],Lat_Bound[1],
                          (Lat_Bound[1]-Lat_Bound[0])/4), 
                linewidth=.75, labels=[1, 1, 0, 0], color='0.8')
m.drawmeridians(np.arange(Long_Bound[0],Long_Bound[1],
                          (Long_Bound[1]-Long_Bound[0])/4), 
                linewidth=.75, labels=[0, 0, 0, 1], color='0.8')
x, y = m(long, lat)
m.scatter(x,y,3,marker='o',color='k')

plt.title('Point Locations')

plt.savefig(Out+'.pdf', bbox_inches='tight')