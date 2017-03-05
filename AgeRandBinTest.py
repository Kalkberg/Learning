# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:22:56 2017

Code to help with debugging of Point_Poly
Generates a random list of minema and maxima
Then attempts to calculate probability of counts in each bin

@author: Kalkberg
"""
import numpy as np
import matplotlib.pyplot as plt

PointAgeMin = np.random.normal(0,5,200)
PointAgeMax = np.random.normal(40,5,200)
AgeMin = 0
AgeMax = 50
AgeInt = 5

AgeBins = np.linspace(AgeMin,AgeMax,(AgeMax/AgeInt)+1)
AgeBinsPlot = np.linspace(AgeMin,AgeMax-AgeInt,(AgeMax/AgeInt))

AgeCount = [[]for i in range(len(AgeBins)-1)]

for _ in range(10**3):
    
    AgeRand = []
    # Generate a random age for each point
    for i in range(0,len(PointAgeMin)):
        Age = np.random.uniform(PointAgeMin[i],PointAgeMax[i],1)
        Age = Age.tolist()
        AgeRand.append(Age)
    
    
    AgesBinned = [[] for i in range(len(AgeBins)-1)]
    # Divide generated values into bins of each age
    for i in range(0,len(AgeRand)):    
        for j in range(0,len(AgeBins)-1):
            if (AgeRand[i][0] > AgeBins[j]) and (AgeRand[i][0] <AgeBins[j+1]):
                AgesBinned[j].append(AgeRand[i][0])
        
        
    
#    for j in range(0,len(AgeBins)-1):
#        AgesBinned[j] = [AgeRand[i] for i in range(0,len(AgeRand)) if \
#                   (AgeRand[i] > AgeBins[j]) and (AgeRand[i] < AgeBins[j])] 
        
    # Count number of ages in each bin
    for i in range(0,len(AgeBins)-1):
        AgeCount[i].append(len(AgesBinned[i]))
        

Median = []
Mean = []
Pctile5 = []
Pctile95 = []
# Do stats on each age bin
for i in range(0,len(AgeBins)-1):
    Median.append(np.median(AgeCount[i]))
    Mean.append(np.mean(AgeCount[i]))
    Pctile5.append(np.percentile(AgeCount[i],5))
    Pctile95.append(np.percentile(AgeCount[i],95))    
        
        
f = plt.figure()
plt.plot(AgeBinsPlot,Median,'r',AgeBinsPlot,Mean,'b', 
         AgeBinsPlot,Pctile5,'0.8',AgeBinsPlot,Pctile95,'0.8')
plt.xlabel('Age (Ma)')
plt.ylabel('Counts')
plt.savefig('Test.png',bbox_inches='tight',dpi=300)
plt.close()                                  

        