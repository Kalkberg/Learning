# -*- coding: utf-8 -*-
"""
Learning how to make a custom color ramp.

Modified from answer on StackOverflow:
http://stackoverflow.com/questions/16834861/create-own-colormap-using-matplotlib-and-plot-color-scale    

@author: pyakovlev
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

N = 1000
Color = np.random.normal(10,1,N)
x = np.random.uniform(-1,1,N)
y = np.random.uniform(-1,1,N)

#cdict = {'red':   ((0.0, 0.0, 1.0), # blue 
#                   (0.3, 0.0, 1.0), # cyan 
#                   (0.6, 0.0, 1.0), # green 
#                   (0.9, 1.0, 1.0), # yellow 
#                   (1.0, 1.0, 1.0)), # red
#
#         'green': ((0.0, 0.0, 1.0), # blue
#                   (0.3, 1.0, 1.0), # cyan 
#                   (0.6, 0.5, 1.0), # green 
#                   (0.9, 1.0, 1.0), # yellow 
#                   (1.0, 0.0, 1.0)), # red
#
#         'blue':  ((0.0, 1.0, 1.0),
#                   (0.3, 1.0, 1.0), # cyan 
#                   (0.6, 0.0, 1.0), # green 
#                   (0.9, 0.0, 1.0), # yellow 
#                   (1.0, 0.0, 1.0)), # red
#          }
def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)
    
c = mcolors.ColorConverter().to_rgb
ColorMap = make_colormap(
    [c('blue'), c('cyan'), (Color.mean()-Color.std())/Color.max(), 
     c('cyan'), c('green'), (Color.mean())/Color.max(),
     c('green'),c('yellow'),(Color.mean()+Color.std())/Color.max(),
     c('yellow'),c('red')])
#ColorMap = mcolors.LinearSegmentedColormap('CustomMap',cdict)
plt.scatter(x, y, c=Color, cmap=ColorMap)
plt.colorbar()
plt.show()