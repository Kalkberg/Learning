# -*- coding: utf-8 -*-
"""
Plot netCDF data

modified from: 
http://www.hydro.washington.edu/~jhamman/hydro-logic/blog/2013/10/12/plot-netcdf-data/

@author: Kalkber
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#Read in data
file = 'bandpass_topo2_clip4.nc'
filedata = Dataset(file, moder='r')

# Pull variables
lons = filedata.variables['x'][:]
lats = filedata.variables['y'][:]
topo = filedata.variables['z'][:]

filedata.close()

# Make projection
# m = Basemap(projection='moll',lon_0=0,resolution='c') #Mollweide world
m = Basemap(projection='merc',llcrnrlat=lats.min(),urcrnrlat=lats.max(),\
            llcrnrlon=lons.min(),urcrnrlon=lons.max(),lat_ts=40,resolution='i')
            # Mercador
#m = Basemap(width=7500000,height=5000000, resolution='l',projection='stere',\
#            lat_ts=40,lat_0=lats.mean(),lon_0=lons.mean())

# Create lat long arrays and convert to map coordinates
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon,lat)

# Plot data
topo_data = m.pcolor(xi,yi,np.squeeze(topo))


# Draw lines
m.drawcoastlines(linewidth=0.25, color='0.8')
m.drawcountries(linewidth=0.25, linestyle='solid', color='0.8')
m.drawstates(linewidth=0.25, linestyle='solid', color='0.8')
m.drawparallels(np.arange(lats.min(),lats.max(),10.), linewidth=.5,
                labels=[1, 0, 0, 0], color='0.8')
m.drawmeridians(np.arange(lons.min(),lons.max(),10.), linewidth=.5,
                labels=[0, 0, 0, 1], color='0.8')

# Plot Contours
levels = np.arange(-200,201,100)
contour_data = m.contour(xi, yi, np.squeeze(topo),levels,linewidths=0.5, colors='k')
plt.clabel(contour_data,inline=1,fontsize=6, fmt='%1.0f')


# Add colorbar
cbar = m.colorbar(topo_data, location='right', pad='5%')
cbar.set_label('Dynamic Topography (m)')

# Add title and save
plt.title('Dynamic Topography from Molnar et al., 2015')

plt.savefig('Dynamic_topo6.png',dpi=300)
plt.show()
