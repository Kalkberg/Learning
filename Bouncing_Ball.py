# -*- coding: utf-8 -*-
"""
Creates an animation of a bouncing ball

@author: Kalkberg
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Inputs
output = 'ball' # Name of file to create

# Lists describe location and velocity of ball. These are randomly generated.
Ball_Loc = [np.random.randint(1,9),np.random.randint(1,9)] # Vals are 1-9 so ball starts in box
Ball_Vel = [np.random.uniform(-0.2,0.2),np.random.uniform(-0.1,0.1)]

#Ball_Loc = [5,5]
#Ball_Vel = [.1,.5]

# Set up figure
fig = plt.figure()
fig.set_canvas(plt.gcf().canvas)
#ax = fig.add_subplot(111)

# Set up stuff to plot during animation
Ball, = plt.plot([],[],marker='o',color='k', linestyle='none', markersize=5)
time_text = plt.text(4, 10.4, '', backgroundcolor='w')
#plt.axis.get_xaxis().set_ticklabels([])
#plt.axes.get_xaxis().set_visible(False)
#plt.axes.get_yaxis().set_visible(False)


# Set up axes
plt.xlim(0,10)
plt.ylim(0,10)

# Function to create frame for the animation
def init():
    Ball.set_data([],[])
    time_text.set_text('')
    return Ball, time_text,

# Function to plot data for each frame. i is the number of the frame
def animate(i):
    
    # Move ball by velocity
    Ball_Loc[0] = Ball_Loc[0] + Ball_Vel[0]
    Ball_Loc[1] = Ball_Loc[1] + Ball_Vel[1]
    
    # Bounce ball off walls
    if (Ball_Loc[0] <= 0) or (Ball_Loc[0] >= 10):
        Ball_Vel[0] = -Ball_Vel[0]
    if (Ball_Loc[1] <= 0) or (Ball_Loc[1] >= 10):
        Ball_Vel[1] = -Ball_Vel[1]
    
    Ball.set_data(Ball_Loc[0],Ball_Loc[1])
    time_text.set_text('time = %s' %int(i))
    return Ball,

#Animate the figure
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=150, 
                               interval=.1, blit=True)
#kwargs={'bbox_inches':'tight'}
anim.save(output+'.mp4', fps=10, dpi=300,
          extra_args=['-vcodec', 'libx264'])
#anim.save(output+'.gif', writer='imagemagick', fps=30, dpi=100)