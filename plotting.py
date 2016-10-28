"""
Created by Petr Yakovlev, 2016
"""

import numpy as np
import matplotlib.pyplot as plot

x =np.linspace(-2 * np.pi,2 * np.pi, 60)
y = np.sin(x)

plot.plot(x,y, 'bo--')
plot.title('Sine Curve')
plot.xlabel('x-axis'); plot.ylabel('y-axis')
#plot.show()
plot.savefig('plot.pdf', bbox_inches='tight')