# -*- coding: utf-8 -*-
"""
Plots vectors on a map

@author: Kalkberg
"""
import pandas
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

InData ='GPS_Velocities_edited.csv'
OutPlot = 'GPS_Vel.pdf'

AllData = pandas.read_csv(InData)

# Set up figure and background
m = Basemap(projection='merc',
            llcrnrlat=40,
            urcrnrlat=49,
            llcrnrlon=-125,
            urcrnrlon=-109,
            lat_ts=45,
            resolution='i')

#m.shadedrelief()
#m.etopo()
#m.warpimage()
#m.drawcoastlines(linewidth=0.5, color='0.8')
m.drawcountries(linewidth=0.5, linestyle='solid', color='1')
m.drawstates(linewidth=0.5, linestyle='solid', color='1')
m.drawparallels(np.arange(40.,51.,4.), linewidth=.75, 
                labels=[1, 1, 0, 0], color='1')
m.drawmeridians(np.arange(-124.,-105.,4.), linewidth=.75, 
                labels=[0, 0, 0, 1], color='1')
m.readshapefile('qfaults','qfaults', color='0.2') # Plot a shape file (qfaults)
m.drawmapboundary(fill_color='white', color='0.8')
#x,y = m(AllData['Longitude'].values,AllData['Latitude'].values)
#m.scatter(x,y,1,marker='o',color='k')
m.quiver(AllData['Longitude'].values,AllData['Latitude'].values,
         AllData['Ve (mm/yr)'].values,AllData['Vn  (mm/yr)'].values,
         latlon=True,scale=100) # Plot velocities
plt.title('GPS Velocities')
plt.tight_layout()

plt.savefig(OutPlot)

