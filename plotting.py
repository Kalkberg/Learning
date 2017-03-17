"""
Created by Petr Yakovlev, 2016
"""

import numpy as np
import matplotlib.pyplot as plot

# Input paramaters
data = 'Tibet_All.csv'
output = 'Tibet_All'

# Read in data, cut out headers and redistribute
data = np.genfromtxt(data, delimiter=',')
data = np.delete(data, (0), axis=0)
age, lat, long = data[:,0], data[:,1], data[:,2]

plot.plot(age,lat, 'ko')
plot.title('Tibet Volcanicsm')
plot.xlabel('Age (Ma)'); plot.ylabel('Latitude')
#plot.show()
plot.savefig(output+'.pdf', bbox_inches='tight')