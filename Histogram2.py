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
AllData = pandas.read_csv('Tibet_Volc_for_plotting9.csv')
AllData['Age_Ma'] = pandas.to_numeric(AllData['Age_Ma'])
#Table = AllData[(AllData['Directly_Dated'] == "Y") & (AllData['Age_Ma']<60)]
Table = AllData[AllData['Age_Ma']<60]

Column = Table['Nd_Model_Age_DM_NoCalc'][np.isfinite(Table['Nd_Model_Age_DM_NoCalc'])] #drop NA in column

# Describe frequency states of data
ColumnRed = Column/10**6 # Reduce to Myr from yr
Max = np.max(ColumnRed)

# Break into bins
#Cat1 = Table[(Table['Type']=='Extrusive') & (Table['MgO']<6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='North')]['Nd_Model_Age_DM_NoCalc']
#Cat2 = Table[(Table['Type']=='Extrusive') & (Table['MgO']>6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='North')]['Nd_Model_Age_DM_NoCalc']
#Cat3 = Table[(Table['Type']=='Extrusive') & (Table['MgO']<6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='Central')]['Nd_Model_Age_DM_NoCalc']
#Cat4 = Table[(Table['Type']=='Extrusive') & (Table['MgO']>6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='Central')]['Nd_Model_Age_DM_NoCalc']
#Cat5 = Table[(Table['Type']=='Extrusive') & (Table['MgO']<6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='South')]['Nd_Model_Age_DM_NoCalc']
#Cat6 = Table[(Table['Type']=='Extrusive') & (Table['MgO']>6) 
#    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='South')]['Nd_Model_Age_DM_NoCalc']
Cat1 = Table[(Table['MgO']<6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='North')]['Nd_Model_Age_DM_NoCalc']
Cat2 = Table[(Table['MgO']>6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='North')]['Nd_Model_Age_DM_NoCalc']
Cat3 = Table[(Table['MgO']<6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='Central')]['Nd_Model_Age_DM_NoCalc']
Cat4 = Table[(Table['MgO']>6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='Central')]['Nd_Model_Age_DM_NoCalc']
Cat5 = Table[(Table['MgO']<6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='South')]['Nd_Model_Age_DM_NoCalc']
Cat6 = Table[(Table['MgO']>6) 
    & (Table['Nd_Model_Age_DM_NoCalc']>0) & (Table['Zone']=='South')]['Nd_Model_Age_DM_NoCalc']
# make histogram
n, bins, patches = plt.hist([Cat1/10**6,Cat2/10**6,Cat3/10**6,Cat4/10**6,Cat5/10**6,Cat6/10**6],
                           color=['#33ccff','#0000ff','#66ff33','#009933','#ff0000','#800000'],
                           stacked=True,bins=np.arange(0,int(Max),10**2))
#                           color=['#0000ff','#0000ff','#0000ff','#0000ff', north
#                                  '#00cc00','#00cc00','#00cc00','#00cc00', central
#                                  '#ff0000','#ff0000','#ff0000','#ff0000'], south
## set edge colors to color hashes
#edgecolors=['#0000ff','#33ccff']
#for patch_set, edgecolor in zip(patches, edgecolors):
#    plt.setp(patch_set, edgecolor=edgecolor)
### remove fills for hatched columns       
##fills=[False,True]
##for patch_set, fill in zip(patches, fills):
##    plt.setp(patch_set, fill=fill)
## add hatches for unfilled columns
#hatches=['/','/','','','/','/','','']
#for patch_set, hatch in zip(patches, hatches):
#    plt.setp(patch_set, hatch=hatch)

## Replot histogram for black hatches
#n, bins, patches = plt.hist([Cat5/10**6,Cat6/10**6,Cat7/10**6,Cat8/10**6],
#                           color=['none','none','none','none','none','none','none','none'],
#                           stacked=True,bins=np.arange(0,int(Max),10**2))
#
## Add black hatches on top
#hatches=['-','','-','','-','','-','']
#for patch_set, hatch in zip(patches, hatches):
#    plt.setp(patch_set, hatch=hatch)
        
plt.xlabel('Nd Model Age')
plt.ylabel('Number')
#plt.axis([0, np.max(bins),0,np.max(n)])
plt.axis([0,4000,0,np.max(n)])
plt.legend()

plt.savefig('ModelAge_North_All_MgO_New2.pdf')