# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:29:59 2017

Script to plot Lat Long data over a time interval.

Made and currently set to plot volcanic data from North America.

@author: Kalkberg
"""

# Import needed packages
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
#import sys
import os
#import shutil
#import subprocess
from mpl_toolkits.basemap import Basemap
from moviepy.editor import *


## Create function describing usage and terminating program for errors
#def error():
#    print("Usage: python3 Plot_Anim.py working_dir data.csv Output")
#    print("Where working_dir is the full path to the data")
#    print("e.g. C:/users/animation")
#    print("data.csv contains comma delimited files of age, lat, and long")
#    print("Output is the name of the pdf map to generate from data")
#    sys.exit()
#
## Check number of arguments and import, if not three, return error
#if len(sys.argv) == 4:
#    # Import directory to work on and satellite type from input arguments
#    workdir = sys.argv[1]
#    data = sys.argv[2]
#    output = sys.argv[3]
#    print("Current working directory is set to %s" % workdir)
#    print("Data file set to %s" % data)
#    print("Output file set to %s" % output)
#else:
#    print("Error: Wrong number of input arguments!")
#    error()
#    
#

#Input paramaters for debuging
data = 'NAM_Volc.csv'
output = 'NAM_Volc_Hex_144Ma_2Myr_200samples_2frames'
workdir = 'D:/GitHub/Learning/'
lat_min = 29
lat_max = 50
long_min = -128
long_max = -101
age_min = 0
age_max = 144
hexsize = (25, 20)
step = 2 # Frames per Myr
plt_int = 1 # 0.5 x Myr of data to count for each cell
max_dens = 200 # Defines maximum density expected in dataset
fps_mov = 4 # Fps of final video

# Move to working directory
os.chdir(workdir)

# Read in data, cut out headers and redistribute
data = np.genfromtxt(data, delimiter=',')
data = np.delete(data, (0), axis=0)
age_in, lat_in, long_in = data[:,0], data[:,1], data[:,2]

# Create blank arrays for later use
age = np.array([])
lat = np.array([])
long = np.array([])

# Cut data outside region and time of interest so hexplot polygons are same size
for i in range(0,len(age_in)):
    if (age_in[i] > age_min and age_in[i] < age_max and 
    lat_in[i] > lat_min and lat_in[i] < lat_max and
    long_in[i] > long_min and long_in[i] < long_max):
        age = np.r_[age, age_in[i]]
        lat = np.r_[lat, lat_in[i]]
        long = np.r_[long, long_in[i]]

# Set up figure and projection
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
ax.autoscale(enable=False)
m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,\
            llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')

# Convert data to projection coordinates and make into array for hexbin
x, y = m(long, lat)
x = np.array(x)
y = np.array(y)

# Create empty list of frames
frames = []

for i in range(0,int(age.max())*step,1):   
    
    # Counter for age instance to make sure you go from old to young    
    age_int = (int(age.max())-i/step)
         
    #Redraw the base map
    m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,
                llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5, linestyle='solid', color='k')
    m.drawstates(linewidth=0.5, linestyle='solid', color='k')
    m.drawparallels(np.arange(30.,50.,5.), linewidth=.75, labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-125.,-104.,10.), linewidth=.75, labels=[0, 0, 0, 1])
    m.drawmapboundary(fill_color='white')
    plt.title('Western US Volcanic Activity')
    
    # Collect data for this time interval
    x_plot = np.array([x[j] for j in range(0,len(age)) \
        if (age[j] < age_int + plt_int and age[j] > age_int - plt_int)])
    y_plot = np.array([y[j] for j in range(0,len(age)) \
        if (age[j] < age_int + plt_int and age[j] > age_int - plt_int)])
     
    # Get axis limits from basemap plot
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Make Plot
    hb_plot = m.hexbin(x_plot,y_plot, gridsize=hexsize, linewidths=0.2, 
                extent=(xlim[0],xlim[1],ylim[0],ylim[1]), mincnt=1,
                vmin=1, vmax=max_dens, cmap='viridis')
   
    # Make color bar
    cb = fig.colorbar(hb_plot, ax=ax)
    cb.set_label('Number of Samples')
    
    # Make text box
    time_text = ax.text(0.035, 0.035, 'Age = %s Ma' %int(age_int), 
                    transform=ax.transAxes, backgroundcolor='w')
                                      
    # Save plot to name padded to five digits and save everything
    fig.savefig('Frame'+str(i).zfill(5)+'.png', dpi=300)
    
    # Add to list of frames
    frames.insert(len(frames),'Frame'+str(i).zfill(5)+'.png')  
    
    # Delete hexplot and color bar   
    plt.cla()
    cb.remove()


animation = ImageSequenceClip(frames, fps = fps_mov)
animation.write_videofile('%s.mp4' %output)
#animation.write_gif('%s.gif' %output) 
    
# Clean up
for j in range(0,len(frames)):
    os.remove(frames[j])
          
print("All done!")
