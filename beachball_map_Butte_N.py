# -*- coding: utf-8 -*-
"""
Plots earthquake focal mechanism solutions on a map

Set up for Butte North quadrangle

@author: Kalkberg
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas
from obspy.imaging.beachball import beach
import matplotlib.colors as mcolors
import seaborn as sns
import matplotlib as mpl

# File Names
InData1 ='Butte_North_data_with_blanks.csv'
OutPlot = 'Butte_North_Quakes.pdf'

# Read data
CMTs1  = pandas.read_csv(InData1)

focmecs1 = CMTs1[['Strike','DP','Rak']].as_matrix().tolist()

lons1 = CMTs1[['Long']].as_matrix().squeeze(1).tolist()
lats1 = CMTs1[['Lat']].as_matrix().squeeze(1).tolist()
mag1 = CMTs1['Mag']
depth1 = CMTs1['Depth']

##create custom color map based on data
#def Make_Colormap(seq):
#    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
#    cdict = {'red': [], 'green': [], 'blue': []}
#    for i, item in enumerate(seq):
#        if isinstance(item, float):
#            r1, g1, b1 = seq[i - 1]
#            r2, g2, b2 = seq[i + 1]
#            cdict['red'].append([item, r1, r2])
#            cdict['green'].append([item, g1, g2])
#            cdict['blue'].append([item, b1, b2])
#    return mcolors.LinearSegmentedColormap('CustomMap', cdict)
#    
#c = mcolors.ColorConverter().to_rgb
#ColorMap = Make_Colormap(
#    [(0.0, 0.0, 1.0), c('cyan'), 
#     (np.median(depth1)-2*depth1.std())/depth1.max(), 
#     c('cyan'), (0.2, 0.6, 0.2), 
#     (np.median(depth1)/depth1.max()),
#     (0.2, 0.6, 0.2), c('yellow'),
#     (np.median(depth1)+2*depth1.std())/depth1.max(),
#     c('yellow'),(1.0, 0.0, 0.0)])
fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])

# Set up figures and background
m = Basemap(projection='merc',
            llcrnrlat=46,
            urcrnrlat=46.5,
            llcrnrlon=-113,
            urcrnrlon=-112,
            lat_ts=45,
            resolution='h')

m.drawstates(linewidth=0.5, linestyle='solid', color='1')
m.drawparallels(np.arange(46.,47.,.5), linewidth=.25, 
                labels=[1, 1, 0, 0], color='1')
m.drawmeridians(np.arange(-113.,-112.,1.), linewidth=.25, 
                labels=[0, 0, 0, 1], color='1')
#m.shadedrelief()

# create color map
cmap = mpl.cm.get_cmap('viridis')
sizemin = 3000
sizerange = 3000

# Add beachballs
#ax = plt.gca()
x1, y1 = m(lons1, lats1)
for i in range(len(focmecs1)):
    size = (mag1[i]-mag1.min())*(sizerange/mag1[i].max())+sizemin
    b = beach(focmecs1[i], xy=(x1[i], y1[i]), width=size, linewidth=1, 
              facecolor=cmap(depth1[i]/depth1.max()))
    b.set_zorder(10)
    ax.add_collection(b)

#plt.show()
#plt.tight_layout()
plt.savefig(OutPlot)

# Create a plot showing depth color bar aka legend 1
a = np.outer(np.arange(0,1,0.01),np.ones(10))
legend1, ax1 = plt.subplots()
ax1.imshow(a,cmap=cmap, origin='lower', extent=[0,1,0,depth1.max()], \
                                                 aspect=6/depth1.max())
ax1.axes.get_xaxis().set_visible(False)
ax1.set_ylabel('Depth (km)', fontsize=12)
ax1.locator_params(nbins=6)
ax1.tick_params(axis='y', which='major', labelsize=10)
legend1.set_size_inches(4,1.5)
legend1.savefig('legend1.pdf')
plt.close()
