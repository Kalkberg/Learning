# -*- coding: utf-8 -*-
"""
Plots earthquake focal mechanism solutions on a map

Set up for yellowstone area.

@author: Kalkberg
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas
from obspy.imaging.beachball import beach


# File Names
InData1 ='Yellowstone_Harvard_CMTs.csv'
InData2 = 'SLU_EQ_Data.csv'
OutPlot = 'Yellowstone_CMTs3.pdf'

# Read data
CMTs1  = pandas.read_csv(InData1)
CMTs2  = pandas.read_csv(InData2)

focmecs1 = CMTs1[['str1','dip1','rake1']].as_matrix().tolist()
focmecs2 = CMTs2.loc[CMTs2['Mw'] >4, ['Stk','Dip','Rake']].as_matrix().tolist()

lons1 = CMTs1[['lon']].as_matrix().squeeze(1).tolist()
lats1 = CMTs1[['lat']].as_matrix().squeeze(1).tolist()
lons2 = CMTs2[['Lon']].as_matrix().squeeze(1).tolist()
lats2 = CMTs2[['Lat']].as_matrix().squeeze(1).tolist()

# Set up figures and background
m = Basemap(projection='merc',
            llcrnrlat=41,
            urcrnrlat=47,
            llcrnrlon=-117,
            urcrnrlon=-108,
            lat_ts=45,
            resolution='h')

m.drawstates(linewidth=0.5, linestyle='solid', color='1')
m.drawparallels(np.arange(40.,51.,2.), linewidth=.25, 
                labels=[1, 1, 0, 0], color='1')
m.drawmeridians(np.arange(-124.,-105.,2.), linewidth=.25, 
                labels=[0, 0, 0, 1], color='1')
#m.shadedrelief()

# Add beachballs
ax = plt.gca()
x1, y1 = m(lons1, lats1)
for i in range(len(focmecs1)):
    b = beach(focmecs1[i], xy=(x1[i], y1[i]), width=25000, linewidth=1)
    b.set_zorder(10)
    ax.add_collection(b)
    
x2, y2 = m(lons2, lats2)
for i in range(len(focmecs2)):
    b = beach(focmecs2[i], xy=(x2[i], y2[i]), width=25000, linewidth=1, facecolor='g')
    b.set_zorder(10)
    ax.add_collection(b)
    
#plt.show()
plt.tight_layout()
plt.savefig(OutPlot)
