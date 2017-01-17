# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:16:50 2017

Computes P, T and B axes from strkike dip and rake of a single nodal plane

Adapted from MATLAB scripts found in SEIZMO toolbox by Garrett Euler:
https://github.com/g2e
http://epsc.wustl.edu/~ggeuler/codes/m/seizmo/

@author: pyakovlev
"""
import numpy as np

# Dummy Data
strk = 100
dip = 45
rake = 20

def strikedip2norm(strk, dip):
    normal = np.array([[-np.sin(dip)*np.sin(strk),
              np.sin(dip)*np.cos(strk),
              np.cos(dip)]])
    return normal

def sdr2slip(strk, dip, rake):
    slip = np.array([[np.cos(rake)*np.cos(strk)+
                     np.sin(rake)*np.cos(dip)*np.sin(strk),
            np.cos(rake)*np.sin(strk)-np.sin(rake)*np.cos(dip)*np.cos(strk),
            np.sin(rake)*np.sin(dip)]])
    return slip

def cart2sph(e, n, u):
    a = np.arctan2(n, e)
    p = np.arctan2(u, np.sqrt(e**2+n**2))
    v = np.sqrt(e**2+n**2+u**2)
    return a, p, v
    
def neu2vpa(neu):
    a, p, v = cart2sph(neu[1], neu[0], neu[2])
    a = (180/np.pi)*(np.pi/2-a)
    p = -(180/np.pi)*p
    vpa = np.array([v, p, a])
    return vpa

def sdr2null(strk, dip, rake):
    n = -np.sin(rake)*np.cos(strk) + np.cos(rake)*np.cos(dip)*np.sin(strk)
    e = -np.sin(rake)*np.sin(strk) - np.cos(rake)*np.cos(dip)*np.cos(strk)
    u = np.cos(rake)*np.sin(dip)
    neu = np.array([n,e,u])
    return neu

def sdr2tpb(strk,dip,rake):
    strk = strk*np.pi/180
    dip = dip*np.pi/180
    rake = rake*np.pi/180
    
    normal = strikedip2norm(strk,dip)
    slip = sdr2slip(strk,dip,rake)
    
    t = neu2vpa(np.squeeze(normal+slip))
    p = neu2vpa(np.squeeze(normal-slip))
    b = neu2vpa(sdr2null(strk,dip,rake))

    # Delete magnitudes of vectors and convolve to single output matrix
    tpb = np.array([np.delete(t,0,0), np.delete(p,0,0), np.delete(b,0,0)])

    # Make sure all trends and plunges are positive values between 0 and 360
    for i in range(0,3):
        if tpb[i,0]<0:
            tpb[i,0] = np.abs(tpb[i,0])
            if tpb[i,1] > 180:
                tpb[i,1] = tpb[i,1] - 180
            else:
                tpb[i,1] = tpb[i,1] + 180
        elif tpb[i,1]<0:
           tpb[i,1] = tpb[i,1] + 360
    return tpb

#print("T axis orientation %s->%s" 
#      %(np.round(tpb[0,0],1), np.round(tpb[0,1],1)))
#print("P axis orientation %s->%s" 
#      %(np.round(tpb[1,0],1), np.round(tpb[1,1],1)))
#print("B axis orientation %s->%s" 
#      %(np.round(tpb[2,0],1), np.round(tpb[2,1],1)))