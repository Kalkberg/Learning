# -*- coding: utf-8 -*-
"""
Plots vectors on a map using pandas and matplotlib

Set up for yellowstone area, and to plot poles in Snake River Plain reference 
frame.

@author: Kalkberg
"""
import pandas
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# File Names
InData ='GPS_Vel_YS_Rot.csv'
OutPlot = 'GPS_Vel_YS_Rot3.pdf'

# Rotation Pole
Wx = 0.0865
Wy = 0.1771
Wz = -0.2173
W = .30*(np.pi/180)*10**-6 # Make sure to covert deg/myr to rad/yr
#W = 9.6*10**-9

# Constants
ERad = 6371*10**6

# Convert to spherical coordinates
PoleLatRad = np.arctan(Wz/np.sqrt(Wx**2+Wy**2))
PoleLongRad = np.arctan2(Wy,Wx)
#PoleLatRad = 48*(np.pi/180)
#PoleLongRad = -116*(np.pi/180)

# Read in csv
AllData = pandas.read_csv(InData)

# Create empty lists
APole = []
VPole = []
VePole = []
VnPole = []
VeTotal = []
VnTotal = []

#Calculate new poles
for i in range(len(AllData['Longitude'].values)):
    PointLatRad = AllData['Latitude'].values[i]*(np.pi/180)
    PointLongRad = AllData['Longitude'].values[i]*(np.pi/180)
    APole += [np.arccos(np.sin(PointLatRad)*np.sin(PoleLatRad) 
                +np.cos(PointLatRad)*np.cos(PoleLatRad)
                *np.cos(PoleLongRad-PointLongRad))]
    VPole += [np.sin(APole[i])*ERad*W]
    AzPole = np.pi/2 - np.arcsin( 
            (np.cos(PoleLatRad)*np.sin(PoleLongRad-PointLongRad))
            /np.sin(APole[i]))
    VePole += [VPole[i]*np.sin(AzPole)]
    VnPole += [VPole[i]*np.cos(AzPole)]
    VeTotal += [AllData['Ve'].values[i]+VePole[i]]
    VnTotal += [AllData['Vn'].values[i]+VnPole[i]]
    
# Set up figure and background
m = Basemap(projection='merc',
            llcrnrlat=40,
            urcrnrlat=47,
            llcrnrlon=-121,
            urcrnrlon=-109,
            lat_ts=45,
            resolution='i')

m.shadedrelief()
#m.etopo()
#m.warpimage()
#m.drawcoastlines(linewidth=0.5, color='0.8')
m.drawcountries(linewidth=0.5, linestyle='solid', color='1')
m.drawstates(linewidth=0.5, linestyle='solid', color='1')
m.drawparallels(np.arange(40.,51.,2.), linewidth=.25, 
                labels=[1, 1, 0, 0], color='1')
m.drawmeridians(np.arange(-124.,-105.,2.), linewidth=.25, 
                labels=[0, 0, 0, 1], color='1')
#m.readshapefile('qfaults','qfaults', color='0.2') # Plot a shape file (qfaults)
#m.drawmapboundary(fill_color='white', color='0.8')
#x,y = m(AllData['Longitude'].values,AllData['Latitude'].values)
#m.scatter(x,y,1,marker='o',color='k')
#m.quiver(AllData['Longitude'].values,AllData['Latitude'].values,
#         AllData['Ve'].values,AllData['Vn'].values,
#         latlon=True) # Plot velocities
#m.quiver(AllData['Longitude'].values,AllData['Latitude'].values,
#         AllData['VeTotal'].values,AllData['VnTotal'].values,
#         latlon=True, color='b') # Plot calculated velocities
m.quiver(AllData['Longitude'].values,AllData['Latitude'].values,
         VeTotal,VnTotal,
         latlon=True, color='r') # Plot calculated velocities
plt.title('GPS Velocities')
plt.tight_layout()

plt.savefig(OutPlot)

