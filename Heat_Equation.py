# -*- coding: utf-8 -*-
"""
Solves the 1D heat equation with 0 temp on outside, and a constant temp inside

Doesn't work, if I remember correctly

@author: Kalkberg
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Wp = 1000 # Width of object (m)
Uo = 400 # Constant temp on outside of object (C)
Ui = 1200 # Initial temp of object (constant throughout)
a = 8.49*10**-7 # Thermal diffusivity (m^2/s)
n = 10**2 # Number of terms in expansion (increase for higher accuracy)
x2 = np.arange(0,1,1/100) # Distance along rod
x_center = 0.5
t_end = 20 # Number of ka to run model for
a2 = a/Wp**2 # Non-dimentionalize thermal diffusivity

# Set up integral
def integrand(x,k):
    return np.sin(k*np.pi*x)

# Solve heat equation for temperature in center of pluton over time
Upoint = []
for i in range(t_end):
    t = i*10**3*365.25*24*3600 # Convert time steps to s from ka
    Ustep = []
    for k in range(1,n):
        An = 2*((Ui-Uo)/Ui)*quad(integrand,0,1,k)[0]
        Ustep.append(An*np.exp(-t*(k*np.pi*a)**2)*np.sin(k*np.pi*x_center))
    Upoint.append(sum(Ustep)*Ui+Uo) # Make sure to convert back to original coords

plt.plot(np.arange(0,t_end,1),Upoint)
plt.xlabel('Time (ka)')
plt.ylabel('Temp (C)')

## Set up figure
#fig = plt.figure()
#fig.set_canvas(plt.gcf().canvas)
#plt.xlim(0,Wp)
#plt.ylim(Uo,Ui)
#
## Set up stuff to plot during animation
#temp, = plt.plot([],[],color='k')
#time_text = plt.text(4, 10.4, '', backgroundcolor='w')
#

#
## Function to create frame for the animation
#def init():
#    temp.set_data([],[])
#    time_text.set_text('')
#    return temp, time_text,

## Function to plot data for each frame. i is the number of the frame
#def animate(i):
#    
#    # Solve heat equation for temp at this time step
#    t = i*10**3*365.25*24*3600 # Number of seconds in a ka
#    U = []
#    for j in range(len(x2)):
#        Upoint = []
#        for k in range(1,n):
#            An = 2*Ui*quad(integrand,0,1,k)[0]
#            Ustep = An*np.exp(-t*(k*np.pi*a)**2)*np.sin(k*np.pi*j)
#            Upoint.append(Ustep)
#        U.append(sum(Upoint))
#    
#    temp.set_data(x2*Wp,U)
#    time_text.set_text('time = %s ka' %int(i))
#    return temp,
#    
##Animate the figure
#anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, 
#                               interval=1, blit=True)
#anim.save('Heat.mp4', fps=10, dpi=300,
#          extra_args=['-vcodec', 'libx264'])