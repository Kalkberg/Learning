# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:29:59 2017

Script to plot Lat Long data over a time interval.

Made and currently set to plot volcanic data from North America.

@author: Kalkberg
"""

# Import needed packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os
from mpl_toolkits.basemap import Basemap


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
## Move to working directory
#os.chdir(workdir)
#
# Input paramaters for debuging
data = 'NAM_Ig3.csv'
output = 'NAM_Ig_Hex'

# Read in data, cut out headers and redistribute
data = np.genfromtxt(data, delimiter=',')
data = np.delete(data, (0), axis=0)
age, lat, long = data[:,0], data[:,1], data[:,2]

# Dummy Data
#size = 300
#lat = np.random.uniform(34,48,size)
#long = np.random.uniform(-117,-124,size)
#age = np.random.uniform(1,100,size)


# Parameter that affects length of animation
p = 6 # Controlls length of animation
plt_int = 5 # Controlls how long to keep on plot

# Set up figure and projection
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,\
            llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')

# Convert data to projection coordinates
x, y = m(long, lat)

# Make contour plot of the entire interval to get its colorbar
cp1 = m.contour(x,y)
cb = fig.colorbar(cp1, ax=ax)
cb.set_label('counts')
#plt.cla() # Clear axes gets rid of everything except color bar

#Redraw the base map
m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,\
            llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.5, linestyle='solid', color='k')
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.drawparallels(np.arange(30.,50.,5.), linewidth=.75, labels=[1, 1, 0, 0])
m.drawmeridians(np.arange(-125.,105.,10.), linewidth=.75, labels=[0, 0, 0, 1])
m.drawmapboundary(fill_color='white')
plt.title('Western US Igneous Activity')

## Set up stuff to plot during animation
#hb = m.hexbin(a,b, gridsize=(100,100), mincnt=1)
#time_text = ax.text(0.035, 0.035, '', 
#                    transform=ax.transAxes, backgroundcolor='w')
#                    
## Function to create frame for the animation
#def init():
#    hb.set_data(a,b)
#    time_text.set_text('')
#    return hb, time_text,
#
## Function to plot data for each frame. i is the number of the frame
#def animate(i):
#    age_int = (int(age.max())-i/p)
#    # Only plot within plt_int Myr of eruption
#    x = [x[j] for j in range(0,len(age)) \
#        if (age[j] < age_int + plt_int and age[j] > age_int)]
#    y = [y[j] for j in range(0,len(age)) \
#        if (age[j] < age_int + plt_int and age[j] > age_int)]
#    hb.set_data(x,y)
#    time_text.set_text('Age = %s Ma' %int(age_int))
#    return hb, time_text,
#
##Animate the figure
#anim = animation.FuncAnimation(fig, animate, init_func=init, 
#                               frames=int(age.max())*p, interval=20,  blit=True)
#
#anim.save(output+'.mp4', fps=30, dpi=300,
#          extra_args=['-vcodec', 'libx264'])
#          
#print("All done!")
#
#plt.show()
