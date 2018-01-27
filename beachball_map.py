# -*- coding: utf-8 -*-
"""
Plots earthquake focal mechanism solutions on a map

Set up for yellowstone area.

@author: Kalkberg
"""
import pandas
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from obspy.imaging.beachball import beachball

# File Names
InData ='Yellowstone_Harvard_CMTs.csv'
OutPlot = 'Yellowstone_CMTs.pdf'

# Read data
CMTs  = pandas.read_csv(InData)

NPs = CMTs[['str1','dip1','rake1']].as_matrix()

Locs = CMTs[['lon','lat']].as_matrix()

# Set up figure and background
m = Basemap(projection='merc',
            llcrnrlat=41,
            urcrnrlat=47,
            llcrnrlon=-117,
            urcrnrlon=-108,
            lat_ts=45,
            resolution='i')

m.shadedrelief()
#m.etopo()
#m.warpimage()
#m.drawcoastlines(linewidth=0.5, color='0.8')
m.drawcountries(linewidth=0.5, linestyle='solid', color='1')
m.drawstates(linewidth=0.5, linestyle='solid', color='1')
m.drawparallels(np.arange(40.,51.,2.), linewidth=.25, 
                labels=[1, 1, 0, 0], color='1')
m.drawmeridians(np.arange(-124.,-105.,2.), linewidth=.25, 
                labels=[0, 0, 0, 1], color='1')
#m.readshapefile('qfaults','qfaults', color='0.2') # Plot a shape file (qfaults)
#m.drawmapboundary(fill_color='white', color='0.8')
#x,y = m(AllData['Longitude'].values,AllData['Latitude'].values)
#m.scatter(x,y,1,marker='o',color='k')

ax = plt.gca() # get axis

# Plot beachballs
for i in range(len(NPs[1])):
    x,y = m(Locs[i][0],Locs[i][1])
    beach = beachball(NPs[i], xy=(x,y), width=100)
    ax.add_collection(beach)

plt.title('GPS Velocities')
plt.tight_layout()
#plt.legend(loc='lower left')

plt.savefig(OutPlot)

