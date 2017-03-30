"""
Created by Petr Yakovlev, 2016
"""

import numpy as np
import matplotlib.pyplot as plot

# Input paramaters
data = 'Tibet_Dated.csv'
output = 'Tibet_Dated'

# Read in data, cut out headers and redistribute
data = np.genfromtxt(data, delimiter=',')
data = np.delete(data, (0), axis=0)
lat, long, age = data[:,0], data[:,1], data[:,2]

plot.plot(age,lat, 'ko')
plot.title('Tibet Volcanicsm')
plot.xlabel('Age (Ma)'); plot.ylabel('Latitude')
plot.xlim(0,65)
plot.ylim(28,38)
#plot.show()
plot.savefig(output+'.pdf', bbox_inches='tight')