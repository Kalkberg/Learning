# -*- coding: utf-8 -*-
"""
Code for ingesting moment tensor solutions and generating KMZ files with 
"beachball" diagrams at epicenter locations, colored by depth and sized by
magnitude

@author: pyakovlev
"""
# Import needed modules
import os
import sys
import pylab
import shutil
import zipfile 
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from numpy import outer
from numpy import arange
from numpy import ones
from obspy.imaging.beachball import beachball

# Create function describing usage and terminating program for errors
def error():
    print("Usage: python3 beachball.py working_dir data.csv output.kmz")
    print("Where working_dir is the full path to the data")
    print("e.g. C:/users/beachball")
    print("data.csv contains comma delimited files of long, lat, depth, \
    magnitude, strke, dip, rake and date")
    print("output.kmz is the name of the kmz file to generate from data")
    sys.exit()

# Check number of arguments and import, if not three, return error
if len(sys.argv) == 4:
    # Import directory to work on and satellite type from input arguments
    workdir = sys.argv[1]
    data = sys.argv[2]
    output = sys.argv[3]
    print("Current working directory is set to %s" % workdir)
    print("Data file set to %s" % data)
    print("Output file set to %s" % output)
else:
    print("Error: Wrong number of input arguments!")
    error()    

# Move to working directory and create a bin for beachballs
os.chdir(workdir)
os.mkdir('ballbin')

# Read in data, cut out headers and redistribute
data = genfromtxt(data, delimiter=',')
data = np.delete(data, (0), axis=0)
long, lat, depth, magnitude, strike, dip, rake, date = data[:,0], data[:,1], \
    data[:,2], data[:,3], data[:,4], data[:,5], data[:,6], data[:,7]

# Echo progress
print("Making beach balls...")    
    
# Import jet color bar to color by depth
jet = plt.get_cmap('jet')    
    
# Toss balls in ballbin, i.e. create png files of moment tensors for kmz
os.chdir('ballbin')
for i in range(0,data.shape[0]):
    ball = beachball([strike[i], dip[i], rake[i]], 
                     size=1000*(magnitude[i]/magnitude.max()), linewidth=2, 
                     facecolor=jet(depth[i]/depth.max()), outfile='%s.png' % i)
    plt.close()

# Create a plot showing depth color bar aka legend 1
a = outer(arange(0,1,0.01),ones(10))
legend1, ax1 = plt.subplots()
ax1.imshow(a,cmap='jet', origin='lower', extent=[0,1,0,depth.max()], \
                                                 aspect=6/depth.max())
ax1.axes.get_xaxis().set_visible(False)
ax1.set_ylabel('Depth (km)', fontsize=12)
ax1.locator_params(nbins=6)
ax1.tick_params(axis='y', which='major', labelsize=10)
legend1.set_size_inches(4,1.5)
legend1.savefig('legend1.png', transparent=False, bbox_inches='tight')
plt.close()

# Create a plot showing different beachball sizes aka legend 2
circley = arange(np.rint(magnitude.min()), np.rint(magnitude.max()), 1)
circlex = ones(circley.size)
legend2, ax2 = plt.subplots()
ax2.scatter(circlex, circley,s=(55+25*circley*circley), 
            facecolor='None', edgecolor='k', linewidth=1) # Size formula scaled to GE
ax2.axes.get_xaxis().set_visible(False)
ax2.set_ylabel('Magnitude', fontsize=12)
ax2.locator_params(nbins=np.rint(magnitude.max())-np.rint(magnitude.min())+1)
ax2.tick_params(axis='y', which='major', labelsize=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.yaxis.set_ticks_position('none')
pylab.ylim([circley.min()-.5,circley.max()+.5]) # Eliminate extra labels
legend2.set_size_inches(.75,1.59)
legend2.savefig('legend2.png', transparent=False, bbox_inches='tight')
plt.close()

# Echo progress
print("Making Google Earth Files...")

# Start writing kml file in root directory
os.chdir('..')
kml = open('beachballs.kml','w')
kml.write('<?xml version="1.0" encoding="UTF-8"?>\n') # header
kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n') # namespan declaration
kml.write('<Document>\n')

# Define region
kml.write('\t<Region>\n')
kml.write('\t<LatLonAltBox>\n')
kml.write('\t\t<north>%s</north>\n' %lat.max())
kml.write('\t\t<south>%s</south>\n' %lat.min())
kml.write('\t\t<east>%s</east>\n' %long.max())
kml.write('\t\t<west>%s</west>\n' %long.min())
kml.write('\t</LatLonAltBox>\n')
kml.write('\t</Region>\n')

# Plot legend 1, depth color bar
kml.write('\t<ScreenOverlay>\n')
kml.write('\t\t<Icon>\n')
kml.write('\t\t\t<href>legend1.png</href>')
kml.write('\t\t</Icon>\n')
kml.write('\t\t<overlayXY x="0" y="1" xunits="fraction" yunits="fraction"/>')
kml.write('\t\t<screenXY x="0" y="1" xunits="fraction" yunits="fraction"/>')
kml.write('\t\t<rotationXY x="0" y="0" xunits="fraction" yunits="fraction"/>')
kml.write('\t\t<size x="0" y="0" xunits="fraction" yunits="fraction"/>')
kml.write('\t</ScreenOverlay>\n')

# Plot legend 2, magnitude size
kml.write('\t<ScreenOverlay>\n')
kml.write('\t\t<Icon>\n')
kml.write('\t\t\t<href>legend2.png</href>')
kml.write('\t\t</Icon>\n')
kml.write('\t\t<overlayXY x="0" y="1" xunits="fraction" yunits="fraction"/>')
kml.write('\t\t<screenXY x="88" y="1" xunits="pixels" yunits="fraction"/>')
kml.write('\t\t<rotationXY x="0" y="0" xunits="fraction" yunits="fraction"/>')
kml.write('\t\t<size x="0" y="0" xunits="fraction" yunits="fraction"/>')
kml.write('\t</ScreenOverlay>\n')

# Gnerate icon styles for each beachball
for i in range(0,data.shape[0]):
    kml.write('\t<Style id="%s">\n' %i)
    kml.write('\t\t<IconStyle>\n')
    kml.write('\t\t\t<heading>.00001</heading>\n')
    kml.write('\t\t\t<scale>%s</scale>\n' %(.3+magnitude[i]/magnitude.max()))
    kml.write('\t\t\t<Icon>\n')
    kml.write('\t\t\t\t<href>%s.png</href>\n' %i)
    kml.write('\t\t\t</Icon>\n')
    kml.write('\t\t\t</IconStyle>\n')
    kml.write('\t</Style>\n')
    
# Write placemarks
for i in range(0,data.shape[0]):
    kml.write('\t<Placemark>\n')
    kml.write('\t\t<description>YrMoDy = %s<br/>Depth = %s km<br/>Magnitude = %s </description>\n' 
              %(date[i].astype(int), depth[i], magnitude[i]))
    kml.write('\t\t<styleUrl>#%s</styleUrl>\n' %i)
    kml.write('\t\t<Point>\n')
    kml.write('\t\t<coordinates>%s,%s,0</coordinates>\n' % (long[i], lat[i]))
    kml.write('\t\t</Point>\n')
    kml.write('\t</Placemark>\n')

# End KML file
kml.write('</Document>/n')
kml.write('</kml>')
kml.close()

# Create kmz file
shutil.make_archive(output, 'zip', 'ballbin')
os.rename(output+'.zip',output) # shutil appends ".zip" to all files
z =  zipfile.ZipFile(output, 'a')
z.write('beachballs.kml')
z.close()

# Echo progress
print("Cleaning up...")

# Delete temporary files
shutil.rmtree('ballbin')
os.remove('beachballs.kml')

# Echo progress
print("All done!")