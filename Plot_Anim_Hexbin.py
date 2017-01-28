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
import matplotlib.animation as animation
import sys
import os
import shutil
import subprocess
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
#

#Input paramaters for debuging
data = 'NAM_Volc.csv'
output = 'NAM_Volc_Hex_36Ma'
ffmpeg = 'C:/FFMPEG/bin/'
workdir = 'D:/GitHub/Learning/'
lat_min = 29
lat_max = 50
long_min = -128
long_max = -101
age_min = 0
age_max = 144
hexsize = (25, 24)
step = 1 # Controlls length of animation
plt_int = 5 # Controlls how long to keep points on plot
max_dens = 100 # Defines maximum density expected in dataset

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

# Move to ffmpeg directory
os.chdir(ffmpeg)

# Set up figure and projection
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
ax = fig.add_subplot(111)
ax.autoscale(enable=False)
m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,\
            llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')
#m.drawcoastlines(linewidth=0.5)
#m.drawcountries(linewidth=0.5, linestyle='solid', color='k')
#m.drawstates(linewidth=0.5, linestyle='solid', color='k')
#m.drawparallels(np.arange(30.,50.,5.), linewidth=.75, labels=[1, 1, 0, 0])
#m.drawmeridians(np.arange(-125.,-105.,10.), linewidth=.75, labels=[0, 0, 0, 1])
#m.drawmapboundary(fill_color='white')
#plt.title('Western US Igneous Activity')

# Define colormap
cmap = cm.get_cmap('cubehelix')

# Convert data to projection coordinates and make into array for hexbin
x, y = m(long, lat)
x = np.array(x)
y = np.array(y)

## Get axis limits from basemap plot
#xlim = ax.get_xlim()
#ylim = ax.get_ylim()
#
## Make contour plot of the entire interval to get its colorbar
#hb1 = m.hexbin(x,y, gridsize = hexsize, mincnt=1,
#               bins = (0, 10, 100, 1000, 10000),
#               extent = (xlim[0],xlim[1],ylim[0],ylim[1]))
#cb = fig.colorbar(hb1, ax=ax)
#cb.set_label('Relative Density')
#
#plt.cla() # Clear axes gets rid of everything except color bar

for i in range(0,int(age.max()),step):   
    
    # Counter for age instance to make sure you go from old to young    
    age_int = (int(age.max())-i)
         
    #Redraw the base map
    m = Basemap(projection='merc',llcrnrlat=29,urcrnrlat=50,
                llcrnrlon=-128,urcrnrlon=-101,lat_ts=40,resolution='i')
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5, linestyle='solid', color='k')
    m.drawstates(linewidth=0.5, linestyle='solid', color='k')
    m.drawparallels(np.arange(30.,50.,5.), linewidth=.75, labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-125.,-104.,10.), linewidth=.75, labels=[0, 0, 0, 1])
    m.drawmapboundary(fill_color='white')
    plt.title('Western US Igneous Activity')
    
    # Collect data for this time interval
    x_plot = np.array([x[j] for j in range(0,len(age)) \
        if (age[j] < age_int + plt_int and age[j] > age_int)])
    y_plot = np.array([y[j] for j in range(0,len(age)) \
        if (age[j] < age_int + plt_int and age[j] > age_int)])
     
    # Get axis limits from basemap plot
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

#    # Append x and y values outside of bounding box to keep hexes same size
#    x_ul, y_ul = m(long_min-1, lat_max+1)
#    x_ur, y_ur = m(long_max+1, lat_max+1)
#    x_ll, y_ll = m(long_min-1, lat_min-1)
#    x_lr, y_lr = m(long_max+1, lat_min-1)
#    xplot = np.r_[x_plot,x_ul,x_ur,x_ll,x_lr]
#    yplot = np.r_[y_plot,y_ul,y_ur,y_ll,y_lr]
       
    # Make Plot
    hb_plot = m.hexbin(x_plot,y_plot, gridsize=hexsize, linewidths=0.2, 
                extent=(xlim[0],xlim[1],ylim[0],ylim[1]), mincnt=1,)
    
    # Force draw so that get colors works    
    ax.figure.canvas.draw()

    # Get counts for each bin and assigned color
    counts = hb_plot.get_array() # counts are (n, )
    colors = hb_plot.get_facecolors() # colors are (n, 4)
    
    # Make a blank array for new colors    
    colors_new = np.array([])
    
    # Redefine colors using color bar    
    for i in range(0,len(counts)):
        if counts[i] ==0:
            colors_new = np.r_[colors_new, np.zeros([1,4])] 
        colors_new = np.r_[colors_new, np.array(cmap(counts[i]/max_dens))]    
      
    hb_plot.set_facecolors(colors_new)
    
    # Make color bar
    cb = fig.colorbar(hb_plot, ax=ax)
    cb.set_label('Number of Samples')
    
    # Make text box
    time_text = ax.text(0.035, 0.035, 'Age = %s Ma' %int(age_int), 
                    transform=ax.transAxes, backgroundcolor='w')
                                      
    # Save plot to name padded to five digits and save everything
    fig.savefig('Frame'+str(i).zfill(5)+'.png', dpi=300)
    
    # Delete hexplot and color bar   
    plt.cla()
    cb.remove()
    
    
#Run FFmpeg
subprocess.Popen(['ffmpeg -f image2 -r 2 -i Frame%%05d.png -vcodec mpeg4'\
                ' -y %smovie.mp4' %output]).wait()

# Clean up
#for j in range(0,int(age.max()),step):
#    os.remove('Frame'+str(j).zfill(5)+'.png')

#shutil.copyfile(ffmpeg+output+'movie.mp4',workdir+output+'movie.mp4')


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
print("All done!")
#
#plt.show()
