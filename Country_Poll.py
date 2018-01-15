# -*- coding: utf-8 -*-
"""
Imports polling data and plots on a map

@author: Kalkberg
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
import pandas
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

#Read data
Ramen = pandas.read_csv('Ramen_Ratings.csv')
JDiaspora = pandas.read_csv('JDiaspora.csv')

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

# Create color bar
cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=np.nanmin(stars), vmax=np.max(stars))

#%% Create map
# Load shapefiles
CountriesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_0_countries') 
StatesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_1_states_provinces') 

# Set up figure
fig = plt.figure(figsize=(15, 7.5))
gs = gridspec.GridSpec(1, 2, width_ratios=[30, 100], wspace=0) 

# Draw map
ax1 = plt.subplot(gs[1],projection=ccrs.PlateCarree(),)
#Projection options: PlateCarree Mollweide Robinson

# Draw countries
for country in shpreader.Reader(CountriesShape).records():
    # if country is in the database color by mean 
    if country.attributes['NAME_LONG'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['NAME_LONG']]["Stars"]))
        ax1.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['NAME_LONG'])
    else:
        ax1.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor='w',
            edgecolor='k',
            label=country.attributes['NAME_LONG'])

# Draw states, but only specified ones
for country in shpreader.Reader(StatesShape).records():
    # if country is in the database color by mean 
    if country.attributes['name'] in Ramen['Country'].unique():
        color = norm(np.mean(Ramen[Ramen["Country"]==country.attributes['name']]["Stars"]))
        ax1.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=cmap(color),
            edgecolor='k',
            label=country.attributes['name'])

## Create color bar
#sm = plt.cm.ScalarMappable(cmap=cmap)
#sm._A = []
#cb = plt.colorbar(sm, fraction=0.0226, pad=-.012)
#cb.set_ticks([0,1/5,2/5,3/5,4/5,1])
#cb.ax.set_yticklabels([0,1,2,3,4,5]) 
#cb.set_label('Mean Stars', labelpad=-55, fontsize=14, fontweight='bold')

# Neaten up figure and save
#plt.tight_layout()
ax1.set_title('World Ramen Ratings', y=.95, fontsize=14, fontweight='bold')
#plt.savefig('Ramen_Map.pdf')
#plt.close()

#np.mean(Ramen[Ramen['Variety'].str.contains('Chicken')]['Stars'])

#%% Create plots
ax2 = plt.subplot(gs[0])
#plt.figure(num=2, figsize=(2, 10), dpi=300, facecolor='w', edgecolor='k')
ax2.set_xlim([0,5.5])
ax2.set_xticks([1,5])
ax2.set_yticks(np.arange(len(CountryAvg[0])))
ax2.set_yticklabels(CountryAvg[0])

# Sort countries by ranking
ax2.plot(beef[0],beef[1],'or',label='beef')
ax2.plot(chicken[0],chicken[1],'o',color='orange',label='chicken')
ax2.plot(pork[0],pork[1],'o',color='pink',label='pork')
ax2.plot(fish[0],fish[1],'ob',label='fish')
ax2.plot(shrimp[0],shrimp[1],'oc',label='shrimp')
ax2.plot(mushroom[0],mushroom[1],'o',color='brown',label='mushroom')
ax2.scatter(CountryAvg[1,:],range(len(CountryAvg[1,:])),
            c=CountryAvg[1,:],vmin=np.min(stars),vmax=np.max(stars),
            s=50,cmap=cmap, zorder=10,label='all',marker='d')
ax2.legend()
#plt.tight_layout()
plt.savefig('Ramen_Chart.pdf')
#plt.close()

#%%
RamenDict = dict(zip(CountryAvg.tolist()[0], CountryAvg.tolist()[1]))

RamenDis =[[],[],[],[]]
for country in JDiaspora['Country'].unique():
    if country in RamenDict:
        people=JDiaspora[JDiaspora['Country']==country]['People'].unique()[0]
        RamenDis=np.append(RamenDis,
                           [[float(RamenDict[country])], 
                             [float(people)],
                             [len(Ramen[(Ramen['Country']==country)&(Ramen['Stars']>3)])],
                             [country]],axis=1)
ax3 = plt.subplot()       
sns.regplot(x=RamenDis[1],y=RamenDis[0],ax=ax3)
ax3.set_ylim([0,5])
ax3.set_xlabel('Number of Japanese Nationals')
ax3.set_ylabel('Average Ramen Rating')
for tick in ax3.get_xticklabels():
    tick.set_rotation(30)
plt.tight_layout()
plt.savefig('Ramen_Corr.png')

ax4 = plt.subplot()  
sns.regplot(x=RamenDis[1],y=RamenDis[2], ax=ax4)
ax4.set_ylim([0,300])
ax4.set_xlabel('# of Japanese Nationals')
ax4.set_ylabel('# of Ramen Rated >3 Stars')
for tick in ax4.get_xticklabels():
    tick.set_rotation(30)
plt.tight_layout()
plt.savefig('Ramen_Corr2.png')