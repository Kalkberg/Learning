# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:45:45 2017

@author: pyakovlev
"""

from joblib import Parallel, delayed
import multiprocessing
import numpy as np


# Check available cores, leave one for OS
NumCores = multiprocessing.cpu_count()-1

#Create list of means to iterate over
mean = [1,2,5,-2,1,0.5,.996]

# Define function that will iterate
def iterate(mean):
    means=[]
    for n in range(len(mean)):
        means.append(np.random.uniform(mean[n],1))
    return means,

dist = AgeRandDist  = Parallel(n_jobs=NumCores, verbose=100, backend='threading')(delayed(iterate)(mean) for i in range(10^1))
