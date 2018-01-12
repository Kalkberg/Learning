# -*- coding: utf-8 -*-
"""
Imports polling data and plots on a map

@author: Kalkberg
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
import pandas
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

#Read data
Ramen = pandas.read_csv('Ramen_Ratings.csv')

# Calculate average ranking by country
stars = np.array([])
for ramencountry in Ramen['Country'].unique():
    stars = np.append(stars,np.mean(Ramen[Ramen['Country'] == ramencountry]['Stars']))

# Sort countries by ranking
CountryAvg=np.array([Ramen['Country'].unique(),stars])
CountryAvg=CountryAvg[:,CountryAvg[1,:].argsort()]

# Calculate averages by flavor, using country indexing from above
chicken = np.array([[],[]])
beef = np.array([[],[]])
fish = np.array([[],[]])
shrimp = np.array([[],[]])
pork = np.array([[],[]])
mushroom = np.array([[],[]])
for ramencountry in Ramen['Country'].unique():
    index = np.argwhere(CountryAvg[0]==ramencountry)[0,0]    
    chicken = np.append(chicken,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Chicken'))]['Stars'])],
                                [index]],axis=1)
    beef = np.append(beef,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Beef'))]['Stars'])],
                                [index]],axis=1)
    fish = np.append(fish,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Fish'))]['Stars'])],
                                [index]],axis=1)
    shrimp = np.append(shrimp,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Shrimp'))]['Stars'])],
                                [index]],axis=1)
    pork = np.append(pork,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Pork'))]['Stars'])],
                                [index]],axis=1)
    mushroom = np.append(mushroom,[[np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Mushroom'))]['Stars'])],
                                [index]],axis=1)

# Calculate average flavor rankings by country
chicken = np.array([])
for ramencountry in Ramen['Country'].unique():
    stars = np.append(stars,np.mean(Ramen[(Ramen['Country'] == ramencountry)&
                                          (Ramen['Variety'].str.contains('Chicken'))]['Stars']))


# Create color bar
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=0, vmax=5)

#%% Create map
# Load shapefiles
CountriesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_0_countries') 
StatesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_1_states_provinces') 

# Set up figure
fig = plt.figure(figsize=(15, 7.5))

# Draw map
ax = plt.axes(projection=ccrs.PlateCarree())
#Projection options: PlateCarree Mollweide Robinson

# Draw countries
for country in shpreader.Reader(CountriesShape).records():
    # if country is in the database color by mean 
    if country.attributes['NAME_LONG'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['NAME_LONG']]["Stars"]))
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['NAME_LONG'])
    else:
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor='w',
            edgecolor='k',
            label=country.attributes['NAME_LONG'])

# Draw states, but only specified ones
for country in shpreader.Reader(StatesShape).records():
    # if country is in the database color by mean 
    if country.attributes['name'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['name']]["Stars"]))
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['name'])

# Create color bar
sm = plt.cm.ScalarMappable(cmap=cmap)
sm._A = []
cb = plt.colorbar(sm, fraction=0.0226, pad=-.012)
cb.set_ticks([0,1/5,2/5,3/5,4/5,1])
cb.ax.set_yticklabels([0,1,2,3,4,5]) 
cb.set_label('Mean Stars', labelpad=-55, fontsize=14, fontweight='bold')

# Neaten up figure and save
plt.tight_layout()
plt.title('World Ramen Ratings', y=.95, fontsize=14, fontweight='bold')
plt.savefig('Ramen_Map.pdf')
plt.close()

#np.mean(Ramen[Ramen['Variety'].str.contains('Chicken')]['Stars'])

#%% Create plots
plt.figure(num=2, figsize=(2, 10), dpi=300, facecolor='w', edgecolor='k')
plt.xlim([0,5.5])
plt.xticks([1,5])
plt.yticks(np.arange(len(CountryAvg[0])),CountryAvg[0])

# Sort countries by ranking
plt.plot(beef[0],beef[1],'or')
#plt.plot(chicken[0],chicken[1],'o',color='orange')
plt.plot(pork[0],pork[1],'o',color='pink')
plt.plot(fish[0],fish[1],'ob')
plt.plot(fish[0],fish[1],'oc')
plt.plot(mushroom[0],mushroom[1],'o',color='brown')
plt.scatter(CountryAvg[1,:],range(len(CountryAvg[1,:])),
            c=CountryAvg[1,:],vmin=0,vmax=5,s=35,cmap=cmap)
plt.tight_layout()
plt.savefig('Ramen_Plot.pdf')
plt.close()
        


