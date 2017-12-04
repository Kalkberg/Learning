# -*- coding: utf-8 -*-
"""
Takes a set of points with values at lat and long coordinates and creates a map
in the region of interest

@author: Kalkberg
"""

import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Inputs
Lat_Bound = (44,50) # Min and max latitude to plot
Long_Bound = (-118,-102) # Min and max longitude to plot
In = 'Tibet_New_Points.csv' # Name of input file
Out = 'Locations' # Stem name of output file

# Read in data, cut out headers and redistribute
data = np.genfromtxt(In, delimiter=',')
data = np.delete(data, (0), axis=0)
lat, long, thickness, error = data[:,0], data[:,1], data[:,2], data[:,3]

# Set up basemap
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
ax.autoscale(enable=False)
m = Basemap(projection='merc',llcrnrlat=Lat_Bound[0],urcrnrlat=Lat_Bound[1],
            llcrnrlon=Long_Bound[0],urcrnrlon=Long_Bound[1],
            lat_ts=np.mean((Lat_Bound[0],Lat_Bound[1])),resolution='i')

#lat = (45,46,47)
#long = (-115,-113,-108)

# Redefine data and map boundaries in 
Long_BoundM, Lat_BoundM = m(Long_Bound,Lat_Bound)
latM, longM = m(lat,long)
points = np.array([[longM[:],latM[:]]])

# Create grid over which to interpolate
grid_x, grid_y = np.mgrid[Long_BoundM[0]:Long_BoundM[1]:500j,
                          Lat_BoundM[0]:Lat_BoundM[1]:500j]

# Interpolate - data needs to be 2D numpy array
grid = griddata(np.squeeze(np.dstack((latM.T,longM.T))),
                thickness, (grid_x, grid_y), method='nearest')

# Plot interpolated image then add map elements
plt.imshow(grid.T, extent=(Long_BoundM[0],Long_BoundM[1],
                         Lat_BoundM[0],Lat_BoundM[1]), origin='lower')
#m.plot(longM,latM,'ko')
m.drawcoastlines(linewidth=0.5, color='0.8')
m.drawcountries(linewidth=0.5, linestyle='solid', color='0.8')
m.drawstates(linewidth=0.5, linestyle='solid', color='0.8')
m.drawparallels(np.arange(Lat_Bound[0],Lat_Bound[1],
                          (Lat_Bound[1]-Lat_Bound[0])/4), 
                linewidth=.75, labels=[1, 1, 0, 0], color='0.8')
m.drawmeridians(np.arange(Long_Bound[0],Long_Bound[1],
                          (Long_Bound[1]-Long_Bound[0])/4), 
                linewidth=.75, labels=[0, 0, 0, 1], color='0.8')


plt.title('Crustal Thickness (km)')

plt.savefig(Out+'.pdf', bbox_inches='tight')



