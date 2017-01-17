# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:33:21 2017

Script to convert strk, dip and rake of a double couple earthquake to a 
moment tensor

Doesn't work right!

@author: pyakovlev
"""

import numpy as np

def MomentTensor(strk, dip, rake, mag):

    # Import data, making sure to convert to radians
    strk = strk*np.pi/180
    dip = dip*np.pi/180
    rake = rake*np.pi/180
    Mo = np.exp(1.5*(mag+10.73))

Mxx = -Mo*(np.sin(dip)*np.cos(rake)*np.sin(2*strk) +
        np.sin(2*dip)*np.sin(rake)*np.sin(strk)**2)
Mxy = Myx = Mo*(np.sin(dip)*np.cos(rake)*np.cos(2*strk) +
        np.sin(2*dip)*np.sin(rake)*np.sin(strk)*np.cos(strk))
Myy = Mo*(np.sin(dip)*np.cos(rake)*np.sin(2*strk) -
        np.sin(2*dip)*np.sin(rake)*np.cos(strk)**2)
Mxz = Mzx = -Mo*(np.cos(dip)*np.cos(rake)*np.cos(2*strk) +
        np.cos(2*dip)*np.sin(rake)*np.sin(strk))
Myz = Mzy = -Mo*(np.cos(dip)*np.cos(rake)*np.sin(strk) +
        np.cos(2*dip)*np.sin(rake)*np.cos(strk))
Mzz = Mo*(np.sin(2*dip)*np.sin(rake))

    mt = np.array([[Mxx, Mxy, Mxz],
                  [Myx, Myy, Myz],
                  [Mzx, Mzy, Mzz]])
    return;
Mxx = -Mo*(np.sin(dip)*np.cos(rake)*np.sin(2*strk) +
        np.sin(2*dip)*np.sin(rake)*np.sin(strk))
Mxy = Myx = Mo*(np.sin(dip)*np.cos(rake)*np.cos(2*strk) +
        np.sin(2*dip)*np.sin(rake)*np.sin(strk)*np.cos(strk))
Myy = Mo*(np.sin(dip)*np.cos(rake)*np.sin(2*strk) -
        np.sin(2*dip)*np.sin(rake)*np.cos(strk))
Mxz = Mzx = -Mo*(np.cos(dip)*np.cos(rake)*np.cos(2*strk) +
        np.cos(2*dip)*np.sin(rake)*np.sin(strk))
Myz = Mzy = -Mo*(np.cos(dip)*np.cos(rake)*np.sin(strk) +
        np.cos(2*dip)*np.sin(rake)*np.cos(strk))
Mzz = Mo*(np.sin(2*dip)*np.sin(rake))