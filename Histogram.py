# -*- coding: utf-8 -*-
"""
Creates a histogram from a CSV using matplotlib and pandas

@author: pyakovlev
"""

import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['hatch.linewidth'] = 1.0

# Import data
AllData = pandas.read_csv('Tibet_Volc2.csv')
Table = AllData[(AllData['Zone']=='North') & (AllData['DirectlyDated'] == "Y")]

Column = Table['Nd_Model_Age_DM'][np.isfinite(Table['Nd_Model_Age_DM'])] #drop NA in column

# Describe frequency states of data
ColumnRed = Column/10**6 # Reduce to Myr from yr
Max = np.max(ColumnRed)

# Break into bins
Cat1 = Table[(Table['Type']=='Intrusive') & (Table['MgO']<6) 
    & (Table['Age_Ma']>46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat2 = Table[(Table['Type']=='Intrusive') & (Table['MgO']<6) 
    & (Table['Age_Ma']<46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat3 = Table[(Table['Type']=='Intrusive') & (Table['MgO']>6) 
    & (Table['Age_Ma']>46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat4 = Table[(Table['Type']=='Intrusive') & (Table['MgO']>6) 
    & (Table['Age_Ma']<46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat5 = Table[(Table['Type']=='Extrusive') & (Table['MgO']<6) 
    & (Table['Age_Ma']>46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat6 = Table[(Table['Type']=='Extrusive') & (Table['MgO']<6) 
    & (Table['Age_Ma']<46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat7 = Table[(Table['Type']=='Extrusive') & (Table['MgO']>6) 
    & (Table['Age_Ma']>46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']
Cat8 = Table[(Table['Type']=='Extrusive') & (Table['MgO']>6) 
    & (Table['Age_Ma']<46) & (Table['Nd_Model_Age_DM']>0)]['Nd_Model_Age_DM']

# make histogram
n, bins, patches = plt.hist([Cat1/10**6,Cat2/10**6,Cat3/10**6,Cat4/10**6,
                             Cat5/10**6,Cat6/10**6,Cat7/10**6,Cat8/10**6],
                           color=['#70CDDD','#70CDDD','#70CDDD','#70CDDD','#282A74','#282A74','#282A74','#282A74'],
                           stacked=True,bins=np.arange(0,int(Max),10**2))

# set edge colors to color hashes
edgecolors=['#70CDDD','#70CDDD','#70CDDD','#70CDDD','#282A74','#282A74','#282A74','#282A74']
for patch_set, edgecolor in zip(patches, edgecolors):
    plt.setp(patch_set, edgecolor=edgecolor)
# remove fills for hatched columns       
fills=[False,False,True,True,False,False,True,True]
for patch_set, fill in zip(patches, fills):
    plt.setp(patch_set, fill=fill)
# add hatches for unfilled columns
hatches=['/','/','','','/','/','','']
for patch_set, hatch in zip(patches, hatches):
    plt.setp(patch_set, hatch=hatch)

# Replot histogram for black hatches
n, bins, patches = plt.hist([Cat1/10**6,Cat2/10**6,Cat3/10**6,Cat4/10**6,
                             Cat5/10**6,Cat6/10**6,Cat7/10**6,Cat8/10**6],
                           color=['none','none','none','none','none','none','none','none'],
                           stacked=True,bins=np.arange(0,int(Max),10**2))

# Add black hatches on top
hatches=['-','','-','','-','','-','']
for patch_set, hatch in zip(patches, hatches):
    plt.setp(patch_set, hatch=hatch)
        
plt.xlabel('Nd Model Age')
plt.ylabel('Number')
plt.axis([0, np.max(bins),0,np.max(n)])
plt.legend()

plt.savefig('ModelAge_North_Dated.pdf')