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
from obspy.imaging.beachball import beachball
import matplotlib.pyplot as plot
from numpy import genfromtxt
import numpy as np
import shutil
import zipfile 

# Create function describing usage and terminating program for errors
def error():
    print("Usage: python3 beachball.py working_dir data.csv output.kmz")
    print("Where working_dir is the full path to the data")
    print("e.g. C://users//beachballs")
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
data = genfromtxt('data.csv', delimiter=',')
data = np.delete(data, (0), axis=0)
long, lat, depth, magnitude, strike, dip, rake, date = data[:,0], data[:,1], \
    data[:,2], data[:,3], data[:,4], data[:,5], data[:,6], data[:,7]

# Import jet color bar to color by depth
jet = plot.get_cmap('jet')    
    
# Toss balls in ballbin, i.e. create png files of moment tensors for kmz
os.chdir('ballbin')
for i in range(0,data.shape[0]):
    ball = beachball([strike[i], dip[i], rake[i]], size=200, linewidth=2, 
                     facecolor=jet(depth[i]/depth.max()), outfile='%s.png' % i)
    plot.close()
os.chdir('..')

# Start writing kml file
kml = open('temp.kml','w')
kml.write('<?xml version="1.0" encoding="UTF-8"?>\n') # header
kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n') # namespan declaration
kml.write('<Document>/n')

# Gnerate icon styles for each beachball
for i in range(0,data.shape[0]):
    kml.write('\t<Style id="%s">\n' %i)
    kml.write('\t\t<IconStyle>\n')
    kml.write('\t\t\t<scale>%s</scale>\n' %(.5+magnitude[i]/magnitude.max())) # size normalized to max eq
    kml.write('\t\t\t<Icon>\n')
    kml.write('\t\t\t\t<href>ballbin/%s.png</href>\n' %i)
    kml.write('\t\t\t</Icon>\n')
    kml.write('\t\t\t</IconStyle>\n')
    kml.write('\t</Style>\n')
# Write placemarks
for i in range(0,data.shape[0]):
    kml.write('\t<Placemark>\n')
    kml.write('\t\t<description>date=%s, depth=%s km, magnitude=%s </description>\n' %(date[i], depth[i], magnitude[i]))
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
#shutil.make_archive(output, 'zip', 'ballbin')
#z =  zipfile.ZipFile(output, 'a')
#z.write('temp.kml')
#z.close()

# Delete temporary files
#shutil.rmtree('ballbin')
#os.remove('temp.kml')